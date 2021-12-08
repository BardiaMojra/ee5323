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
# import seaborn as sns
# sns.set()
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



def dtplot01(df:pd.DataFrame,
           fignum:str,
           output_dir:str,
           title='_',
           figname=None,
           show=False,
            save=True,
            start=0,
            end=1000,
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

  # plot_colors = iter(cmap(np.linspace(0, 1, 15)))
  #plot_colors = iter([plt.cm.tab100(i) for i in range(20)])

  # fig = df.plot(figsize=figsize)
  fig = plt.figure(figsize=figsize)
  ax = plt.axes()
  xy= df.to_numpy(copy=True)
  # y= df.loc[:,1:].to_numpy()
  # plt.plot(xy[:,0], xy[:,1],label=labels[1])
  plt.plot(xy[:,0], xy[:,2],label=labels[2])
  # plt.plot(xy[:,0], xy[:,3],label=labels[3])
  plt.plot(xy[:,0], xy[:,4],label=labels[4])
  # plt.plot(xy[:,0], xy[:,5],label=labels[5])
  plt.plot(xy[:,0], xy[:,6],label=labels[6])
  plt.legend(loc='best')
  plt.grid()

  plt.xlabel('time')
  plt.ylabel('magnitude')


  # set title
  if title != '_':
    tit = fignum+' - '+title
    plt.title('{}'.format(tit), y = 0.95)
  # plt.title(title)
  title = title.replace(' ', '_')
  title = title.replace('.', '-')
  # save and show image
  if save==True and output_dir is not None:
    # st()
    fig_name = output_dir+fignum+'_'+title
    plt.savefig(fig_name, bbox_inches='tight',dpi=400)
    print(longhead+'saving figure: '+fig_name+'.png')
    csv_name = output_dir+fignum+'_'+title
    df.to_csv(csv_name+'.csv', columns=df.columns)
    print(longhead+'saving figure: '+csv_name)
  if show==True: plt.show()
  else: plt.close()
  return

def plot_losses(df:pd.DataFrame,
           fignum:str,
           output_dir:str,
           title='_',
           figname=None,
           show=False,
            save=True,
            start=0,
            end=1000,
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

  # plot_colors = iter(cmap(np.linspace(0, 1, 15)))
  #plot_colors = iter([plt.cm.tab100(i) for i in range(20)])

  # fig = df.plot(figsize=figsize)
  fig = plt.figure(figsize=figsize)
  ax = plt.axes()
  xy= df.to_numpy(copy=True)
  # y= df.loc[:,1:].to_numpy()
  # plt.plot(xy[:,0], xy[:,1],label=labels[1])
  # plt.plot(xy[:,0], xy[:,2],label=labels[2])
  # plt.plot(xy[:,0], xy[:,3],label=labels[3])
  # plt.plot(xy[:,0], xy[:,4],label=labels[4])
  # plt.plot(xy[:,0], xy[:,5],label=labels[5])
  # plt.plot(xy[:,0], xy[:,6],label=labels[6])
  plt.plot(xy[:,0], xy[:,7],label=labels[7])
  plt.plot(xy[:,0], xy[:,8],label=labels[8])
  plt.legend(loc='best')
  plt.grid()

  plt.xlabel('time')
  plt.ylabel('magnitude')


  # set title
  if title != '_':
    tit = fignum+' - '+title
    plt.title('{}'.format(tit), y = 0.95)
  # plt.title(title)
  title = title.replace(' ', '_')
  title = title.replace('.', '-')
  # save and show image
  if save==True and output_dir is not None:
    # st()
    fig_name = output_dir+fignum+'_'+title
    plt.savefig(fig_name, bbox_inches='tight',dpi=400)
    print(longhead+'saving figure: '+fig_name+'.png')
    csv_name = output_dir+fignum+'_'+title
    df.to_csv(csv_name+'.csv', columns=df.columns)
    print(longhead+'saving figure: '+csv_name)
  if show==True: plt.show()
  else: plt.close()
  return


def get_losses(res:pd.DataFrame, output_dir:str, save_en:bool=True, prt_en:bool=True):
    L1 = list()
    L2 = list()
    # nprint_2('get_L2loss: res', res.head(5))

    # L2 = np.zeros((len(res.index), len(res.columns)))
    for i in range(len(res.index)):
      state_l1 = 0.0
      state_l2 = 0.0
      for j in range(len(res.columns)):
        # st()
        l1 = abs(res.iloc[i,j])
        l2 = res.iloc[i,j] ** 2
        state_l1 = l1
        state_l2 = l2
        # nprint(shorthead+'row sum ', res.iloc[i,:].sum())
      L1.append(state_l1)
      L2.append(state_l2)
    L1_df = pd.DataFrame(L1, columns=['L1'])
    L2_df = pd.DataFrame(L2, columns=['L2'])
    res = pd.concat([res,L1_df, L2_df], axis=1)
    # nprint_2('get_L2loss: res', res.head(5))
    # st()
    if save_en==True and  output_dir is not None:
      file_name = output_dir+'losses.txt'
      # if os.path.exists(file_name):
      with open(file_name, 'a+') as f:
        L1_str = shorthead+f"L1 (total): {res['L1'].sum()}"
        L2_str = shorthead+f"L2 (total): {res['L2'].sum()}"
        f.write(L1_str)
        f.write(L2_str+'\n\n')
        f.close()
    return res

def print_losses(df: pd.DataFrame):
  print(shorthead+"L1 (total): ", df['L1'].sum())
  print(shorthead+"L2 (total): ", df['L2'].sum())

  return
