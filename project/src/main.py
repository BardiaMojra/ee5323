import matplotlib.animation as animation
import numpy as np
from gekko import GEKKO

''' NBUG
'''

''' MOD CONFIG
'''

''' MODEL CONFIG
'''
_M1 = 10 # the cart
_M2 = 1  # mass 2
_T_END = 6.2

def main():

  sys = GEKKO() # declare an empty model
  sys.time = np.linespace(0,8,100)
  t_end = int(100.0*6,2/8.0)

  # set model parameters
  m1 = sys.Param(value=_M1)
  m2 = sys.Param(value=_M2)
  final = np.zeros(len(sys.time))
  for i in range(len(sys.time))
    if sys.time[i] < _T_END:
      final[i] = 0



  return # end of main

if __name__ == '__main__':
  main()
  print('\n\n\n--- end of main ---\n\n')
