''' dip
  @author Bardia Mojra - 1000766739
  @brief ee-5323 - project -
  @date 10/31/21

  code based on below YouTube tutorial and Pymotw.com documentation for socket mod.
  @link https://www.youtube.com/watch?v=3QiPPX-KeSc
  @link https://pymotw.com/2/socket/tcp.html

  python socket module documentation
  @link https://docs.python.org/3/library/socket.html
  @link https://docs.python.org/3/howto/sockets.html

'''
import csv
import math
import os
import pyglet
import pymunk
import pymunk.constraints

''' NBUG
'''
from nbug import *

''' MOD CONFIG
'''
_REC_DATA = True
OUT_DIR = '../out/'
TEST_ID = 'test_000'
OUT_FILE_PATH = OUT_DIR+TEST_ID+'_dip.csv'

''' MODEL CONFIG
'''
# cart
cart_mass = 0.5
cart_size = 0.3, 0.2
'''   pendulum 1   '''
pend_1_length = 0.6
pend_1_mass = 0.2
pend_1_moment = 0.001
pend_1_radius = 0.05
'''   pendulum 2  '''
pend_2_length = 0.6
pend_2_mass = 0.3
pend_2_moment = 0.001
pend_2_radius = 0.05


''' main
'''
SCREEN_HEIGHT = 700
window = pyglet.window.Window(1000, SCREEN_HEIGHT, vsync=False, caption='Double Inverted Pendulum Simulator')

# setup the space
space = pymunk.Space()
space.gravity = 0, -9.81

fil = pymunk.ShapeFilter(group=1)

# ground
ground = pymunk.Segment(space.static_body, (-4, -0.1), (4, -0.1), 0.1)
ground.friction = 0.1
ground.filter = fil
space.add(ground)

cart_moment = pymunk.moment_for_box(cart_mass, cart_size)
cart_body = pymunk.Body(mass=cart_mass, moment=cart_moment)
cart_body.position = 0.0, cart_size[1] / 2
cart_shape = pymunk.Poly.create_box(cart_body, cart_size)
cart_shape.friction = ground.friction
space.add(cart_body, cart_shape)

pend_1_body = pymunk.Body(mass=pend_1_mass, moment=pend_1_moment)
pend_1_body.position = cart_body.position[0], cart_body.position[1] + cart_size[1] / 2 + pend_1_length
pend_shape = pymunk.Circle(pend_1_body, pend_1_radius)
pend_shape.filter = fil
space.add(pend_1_body, pend_shape)

# joint
joint = pymunk.constraints.PivotJoint(cart_body, pend_1_body, cart_body.position + (0, cart_size[1] / 2))
joint.collide_bodies = False
space.add(joint)

# pendulum 2
pend_2_body = pymunk.Body(mass=pend_2_mass, moment=pend_2_moment)
pend_2_body.position = cart_body.position[0], cart_body.position[1] + cart_size[1] / 2 + (2 * pend_2_length)
pend_shape2 = pymunk.Circle(pend_2_body, pend_2_radius)
pend_shape2.filter = fil
space.add(pend_2_body, pend_shape2)

# joint2
joint2 = pymunk.constraints.PivotJoint(pend_1_body, pend_2_body, cart_body.position + (0, cart_size[1] / 2 + pend_2_length))
joint2.collide_bodies = False
space.add(joint2)

print(f"cart mass = {cart_body.mass:0.1f} kg")
print(f"pendulum 1 mass = {pend_1_body.mass:0.1f} kg, pendulum moment = {pend_2_body.moment:0.3f} kg*m^2")
print(f"pendulum 2 mass = {pend_2_body.mass:0.1f} kg, pendulum moment = {pend_2_body.moment:0.3f} kg*m^2")

# K gain matrix and Nbar found from modelling via Jupyter
# K = [16.91887353, 21.12423935, 137.96378003, -3.20040325, -259.72220049,  -50.48383455]
# Nbar = 17.0

K = [51.43763708, 54.12690472, 157.5467596, -21.67111679, -429.11603909, -88.73125241]
Nbar = 51.5

# simulation stuff
force = 0.0
MAX_FORCE = 25
DT = 1 / 60.0
ref = 0.0

# drawing stuff
# pixels per meter
PPM = 200.0

color = (200, 200, 200, 200)
label_x = pyglet.text.Label(text='', font_size=18, color=color, x=10, y=SCREEN_HEIGHT - 28)
label_theta = pyglet.text.Label(text='', font_size=18, color=color, x=10, y=SCREEN_HEIGHT - 58)
label_alpha = pyglet.text.Label(text='', font_size=18, color=color, x=10, y=SCREEN_HEIGHT - 88)
label_force = pyglet.text.Label(text='', font_size=18, color=color, x=10, y=SCREEN_HEIGHT - 118)

labels = [label_x, label_theta, label_alpha, label_force]

# data recorder so we can compare our results to our predictions
if os.path.exists(OUT_FILE_PATH):
  os.remove(OUT_FILE_PATH)
f = open(OUT_FILE_PATH, 'w')
out = csv.writer(f)
out.writerow(['time', 'x', 'theta', 'alpha'])
currtime = 0.0
record_data = True

def draw_body(offset, body):
    for shape in body.shapes:
        if isinstance(shape, pymunk.Circle):
            vertices = []
            num_points = 10
            for ii in range(num_points):
                angle = ii / num_points * 2 * math.pi
                vertices.append(body.position + (shape.radius * math.cos(angle), shape.radius * math.sin(angle)))
            points = []
            for v in vertices:
                points.append(int(v[0] * PPM) + offset[0])
                points.append(int(v[1] * PPM) + offset[1])

            data = ('v2i', tuple(points))
            pyglet.graphics.draw(len(vertices), pyglet.gl.GL_LINE_LOOP, data)
        elif isinstance(shape, pymunk.Poly):
            # get vertices in world coordinates
            vertices = [v.rotated(body.angle) + body.position for v in shape.get_vertices()]
            # convert vertices to pixel coordinates
            points = []
            for v in vertices:
                points.append(int(v[0] * PPM) + offset[0])
                points.append(int(v[1] * PPM) + offset[1])
            data = ('v2i', tuple(points))
            pyglet.graphics.draw(len(vertices), pyglet.gl.GL_LINE_LOOP, data)

def draw_line_between(offset, pos1, pos2):
    vertices = [pos1, pos2]
    points = []
    for v in vertices:
        points.append(int(v[0] * PPM) + offset[0])
        points.append(int(v[1] * PPM) + offset[1])
    data = ('v2i', tuple(points))
    pyglet.graphics.draw(len(vertices), pyglet.gl.GL_LINE_STRIP, data)


def draw_ground(offset):
  vertices = [v + (0, ground.radius) for v in (ground.a, ground.b)]
  # convert vertices to pixel coordinates
  points = []
  for v in vertices:
    points.append(int(v[0] * PPM) + offset[0])
    points.append(int(v[1] * PPM) + offset[1])
  data = ('v2i', tuple(points))
  pyglet.graphics.draw(len(vertices), pyglet.gl.GL_LINES, data)


@window.event
def on_draw():
  window.clear()
  # center view x around 0
  offset = (500, 5)
  draw_body(offset, cart_body)
  draw_body(offset, pend_1_body)
  draw_line_between(offset, cart_body.position + (0, cart_size[1] / 2), pend_1_body.position)
  draw_body(offset, pend_2_body)
  draw_line_between(offset, pend_1_body.position, pend_2_body.position)
  draw_ground(offset)
  for label in labels:
    label.draw()


def simulate(_):
    # ensure we get a consistent simulation step - ignore the input dt value
    dt = DT

    # simulate the world
    # NOTE: using substeps will mess up gains
    space.step(dt)

    # populate the current state
    posx = cart_body.position[0]
    velx = cart_body.velocity[0]
    theta = pend_1_body.angle
    thetav = pend_1_body.angular_velocity
    alpha = pend_2_body.angle
    alphav = pend_2_body.angular_velocity

    # dump our data so we can plot
    if record_data:
        global currtime
        out.writerow([f"{currtime:0.4f}", f"{posx:0.3f}", f"{theta:0.3f}", f"{alpha:0.3f}"])
        currtime += dt

    # calculate our gain based on the current state
    gain = K[0] * posx + K[1] * velx + K[2] * theta + K[3] * thetav + K[4] * alpha + K[5] * alphav

    # calculate the force required
    global force
    force = ref * Nbar - gain

    # kill our motors if our angles get out of control
    if math.fabs(pend_1_body.angle) > 1.0 or math.fabs(pend_2_body.angle) > 1.0:
        force = 0.0

    # cap our maximum force so it doesn't go crazy
    if math.fabs(force) > MAX_FORCE:
        force = math.copysign(MAX_FORCE, force)

    # apply force to cart center of mass
    cart_body.apply_force_at_local_point((force, 0.0), (0, 0))


# function to store the current state to draw on screen
def update_state_label(_):
    label_x.text = f'Cart X: {cart_body.position[0]:0.3f} m'
    label_theta.text = f'Pendulum Angle Θ: {pend_1_body.angle:0.3f} radians'
    label_alpha.text = f'Pendulum Angle α: {pend_2_body.angle:0.3f} radians'
    label_force.text = f'Force: {force:0.1f} newtons'


def update_reference(_, newref):
    global ref
    ref = newref


# callback for simulation
pyglet.clock.schedule_interval(simulate, DT)
pyglet.clock.schedule_interval(update_state_label, 0.25)

# schedule some small movements by updating our reference
pyglet.clock.schedule_once(update_reference, 2, 0.2)
pyglet.clock.schedule_once(update_reference, 7, 0.6)
pyglet.clock.schedule_once(update_reference, 12, 0.2)
pyglet.clock.schedule_once(update_reference, 17, 0.0)

pyglet.app.run()
f.close()
