
''' control systems - ode simulation
  @link https://www.youtube.com/watch?v=yp5x8RMNi7o
'''
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt



def sys_a(x, t):
  # compute state derivative
  dx1 = x[1]*np.sin(x[0]) -x[0]
  dx2 = -x[0]*np.sin(x[0]) -x[1]

  return [dx1, dx2]

def sim():
  # set constants
  t_0 = 0
  t_f = 60
  period = 0.1

  # set state initial condition
  x_init = [0, 0]

  # set a discrete time stamp
  t = np.arange(t_0, t_f, period)
  x = odeint(sys_a, x_init, t)

  x1 = x[:,0]
  x2 = x[:,1]

  plt.plot(x1,x2)
  # plt.plot(t,x2)
  plt.title('Mass-Spring-Damper System')
  plt.xlabel('x_1')
  plt.ylabel('x_2')
  plt.legend(['x1', 'x2'])
  plt.grid()
  plt.show()

if __name__ == '__main__':

  sim()
  print('--- end of main ---')
