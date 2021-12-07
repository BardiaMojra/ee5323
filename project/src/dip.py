
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
  draw_body(offset, pend_body)
  draw_line_between(offset, cart_body.position + (0, cart_size[1] / 2), pend_body.position)
  draw_body(offset, pend_body2)
  draw_line_between(offset, pend_body.position, pend_body2.position)
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
  theta = pend_body.angle
  thetav = pend_body.angular_velocity
  alpha = pend_body2.angle
  alphav = pend_body2.angular_velocity
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
  if math.fabs(pend_body.angle) > 1.0 or math.fabs(pend_body2.angle) > 1.0:
      force = 0.0
  # cap our maximum force so it doesn't go crazy
  if math.fabs(force) > MAX_FORCE:
      force = math.copysign(MAX_FORCE, force)
  # apply force to cart center of mass
  cart_body.apply_force_at_local_point((force, 0.0), (0, 0))


# function to store the current state to draw on screen
def update_state_label(_):
  label_x.text = f'Cart X: {cart_body.position[0]:0.3f} m'
  label_theta.text = f'Pendulum Angle Θ: {pend_body.angle:0.3f} radians'
  label_alpha.text = f'Pendulum Angle α: {pend_body2.angle:0.3f} radians'
  label_force.text = f'Force: {force:0.1f} newtons'


def update_reference(_, newref):
  global ref
  ref = newref
