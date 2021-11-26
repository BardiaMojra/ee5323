''' data visualization mod (viz)
  @author Bardia Mojra - 1000766739
  @brief ee-5323 - nonlinear systems - final project
  @date 11/11/21
'''

import sys
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import os

''' NBUG
'''
from pdb import set_trace as st
from pprint import pprint as pp
from nbug import *

''' matplotlib config
'''
matplotlib.pyplot.ion()
plt.style.use('ggplot')


def dtplot(df:pd.DataFrame,
           fignum:str,
           output_dir:str,
           title='_',
           figname=None,
           show=False,
            save=True,
            start=0,
            end=None,
        labels=None,
  range_padding:float=0.5,
  figsize=[6,6]):
  if end is None:
    end = df.index.size-1
  if labels is None:
    labels = df.columns
  if fignum is None:
    eprint('dtplot(): no fignum given... ')
  if output_dir is None:
    eprint('dtplot(): no output given... ')

  # set plot colors
  cmap = cm.get_cmap('plasma', 15)

  plot_colors = iter(cmap(np.linspace(0, 1, 15)))
  #plot_colors = iter([plt.cm.tab100(i) for i in range(20)])

  fig = df.plot(figsize=figsize)
  fig.xlabel('t')
  plt.ylabel('x(t)')
  plt.legend(loc='best')
  plt.grid()
  # set title
  if title != '_':
    plt.title('{}'.format(title), y = 0.95)
  plt.title(title)
  title = title.replace(' ', '_')
  title = title.replace('.', '-')
  # save and show image
  if save==True and output_dir is not None:
    fig_name = output_dir+'{}'.format(figname+'_'+title)
    plt.savefig(fig_name, bbox_inches='tight',dpi=400)
    print(longhead+'saving figure: '+fig_name+'.png')
    csv_name = output_dir+fignum+'_'+title
    df.to_csv(csv_name+'.csv', columns=df.columns)
    print(longhead+'saving figure: '+csv_name)
  if show==True: plt.show()
  else: plt.close()
  return
