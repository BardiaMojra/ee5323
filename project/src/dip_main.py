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
import pyglet
import pymunk

''' NBUG
'''

''' MOD CONFIG
'''

''' MODEL CONFIG
'''





def main():
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

  # cart
  cart_mass = 0.5
  cart_size = 0.3, 0.2
  cart_moment = pymunk.moment_for_box(cart_mass, cart_size)
  cart_body = pymunk.Body(mass=cart_mass, moment=cart_moment)
  cart_body.position = 0.0, cart_size[1] / 2
  cart_shape = pymunk.Poly.create_box(cart_body, cart_size)
  cart_shape.friction = ground.friction
  space.add(cart_body, cart_shape)

  # pendulum properties
  pend_length = 0.6
  pend_mass = 0.2
  pend_moment = 0.001
  pend_radius = 0.05
  pend_body = pymunk.Body(mass=pend_mass, moment=pend_moment)
  pend_body.position = cart_body.position[0], cart_body.position[1] + cart_size[1] / 2 + pend_length
  pend_shape = pymunk.Circle(pend_body, pend_radius)
  pend_shape.filter = fil
  space.add(pend_body, pend_shape)

  # joint
  joint = pymunk.constraint.PivotJoint(cart_body, pend_body, cart_body.position + (0, cart_size[1] / 2))
  joint.collide_bodies = False
  space.add(joint)

  # pendulum 2
  pend_body2 = pymunk.Body(mass=pend_mass, moment=pend_moment)
  pend_body2.position = cart_body.position[0], cart_body.position[1] + cart_size[1] / 2 + (2 * pend_length)
  pend_shape2 = pymunk.Circle(pend_body2, pend_radius)
  pend_shape2.filter = fil
  space.add(pend_body2, pend_shape2)

  # joint2
  joint2 = pymunk.constraint.PivotJoint(pend_body, pend_body2, cart_body.position + (0, cart_size[1] / 2 + pend_length))
  joint2.collide_bodies = False
  space.add(joint2)

  print(f"cart mass = {cart_body.mass:0.1f} kg")
  print(f"pendulum1 mass = {pend_body.mass:0.1f} kg, pendulum moment = {pend_body.moment:0.3f} kg*m^2")
  print(f"pendulum2 mass = {pend_body2.mass:0.1f} kg, pendulum moment = {pend_body2.moment:0.3f} kg*m^2")

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
  f = open('data/dinvpend.csv', 'w')
  out = csv.writer(f)
  out.writerow(['time', 'x', 'theta', 'alpha'])
  currtime = 0.0
  record_data = False


  # callback for simulation
  pyglet.clock.schedule_interval(simulate, DT)
  pyglet.clock.schedule_interval(update_state_label, 0.25)

  # schedule some small movements by updating our reference
  pyglet.clock.schedule_once(update_reference, 2, 0.2)
  pyglet.clock.schedule_once(update_reference, 7, 0.6)
  pyglet.clock.schedule_once(update_reference, 12, 0.2)
  pyglet.clock.schedule_once(update_reference, 17, 0.0)

  pyglet.app.run()

  # close the output file
  f.close()



  return # end of main

if __name__ == '__main__':
  main()
  print('\n\n\n--- end of main ---\n\n')
