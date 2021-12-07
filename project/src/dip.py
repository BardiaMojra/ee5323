  #todo:
  # fix the black window issue





import pyglet

class base(pyglet.window.Window):
  def __init__(self):
    # super(base, self).__init__(600, 600, fullscreen = False)
    super(base, self).__init__(1000, SCREEN_HEIGHT, vsync=False, caption='Double Inverted Pendulum Simulator')
    self.alive = 1
    self.label = pyglet.text.Label('Hello, world',
                                  font_name='Times New Roman',
                                  font_size=36,
                                  x=self.width//2, y=self.height//2,
                                  anchor_x='center', anchor_y='center')
  def on_draw(self):
    self.render()

  def render(self):
    self.clear()
    self.label.draw()
    self.flip()

  def on_close(self):
    self.alive = 0

  def on_key_press(self, symbol, modifiers):
    if symbol == pyglet.window.key.ESCAPE: # [ESC]
      self.alive = 0

  def run(self):
    while self.alive == 1:
      self.render()
      # -----------> This is key <----------
      # This is what replaces pyglet.app.run()
      # but is required for the GUI to not freeze
      #
      event = self.dispatch_events()

x = base()
x.run()
