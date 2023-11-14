# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:34:11 2023

@author: viola
"""
# import necessary modules
from matplotlib import cm
from matplotlib.figure import Figure
from matplotlib.ticker import AutoMinorLocator
import numpy as np

# functions to create necessary matrices/arrays
def create_matrix(function,
                  variables, # array or meshgrid
                  variable3): # float or None
    
    vectorized_function = np.vectorize(function) # vectorize function
    if len(variables) == 1: 
        if variable3 == None:
            f = vectorized_function(variables[0]) # vectorize output
        elif type(variable3) == float:
            f = vectorized_function(variables[0], variable3)
    elif len(variables) == 2:
        #variables[0], variables[1] = np.meshgrid(variables[0], variables[1])
        if variable3 == None:
            f = vectorized_function(variables[0], variables[1]) # vectorize output
        elif type(variable3) == float:
            f = vectorized_function(variables[0], variables[1], variable3) # vectorize output
    elif len(variables) == 3:
        #variables[0], variables[1], variables[2] = np.meshgrid(variables[0], variables[1], variables[2])
        f = vectorized_function(variables[0], variables[1], variables[2])
    
    return f

def generate_arrays(npoint):
    
    delta = np.linspace(0.002, 10, npoint)
    eta = np.linspace(-10, 10, npoint)
    
    return [delta, eta]

# 2D plots
def subplots_2D_graph(fig,
                      Y, # matrix defined outside
                      ylabel,
                      sub,
                      delta,
                      eta,
                      rk): 

    ax1 = fig.add_subplot(2, 2, sub) # subplot
    ax1.grid() # add grid to subplot
    
    #create subplot
    if delta is not None: 
        for j in range(delta[0].size):
            ax1.plot(eta, Y, label="\u0394=%f" % delta[0][j]) # and plot it for different chemical potentials
    
        # legend with delta values only on the first subplot 
        if sub == 1:
            ax1.legend(fontsize="6", loc="upper right")
    else: 
        ax1.plot(eta, Y, color='orange', linestyle='-', linewidth=1.5) # plot data
    
    # label axes
    ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax1.set_ylabel(ylabel)
    if sub == 3 or sub == 4: # label x-axis only for lower subplots 
        ax1.set_xlabel('$\mu$ $(k_B T)$')
    
    return ax1

def complete_2d_plot(Y1,
                     Y2,
                     Y3,
                     Y4,
                     delta,
                     eta,
                     rk,
                     title):
    
    fig = Figure(figsize=(10, 4)) # figure
    fig.suptitle(title) # title of the figure
    # insert subplot in the figure
    subplots_2D_graph(fig, Y1, 'S($S_0$)', 1, delta, eta, 0)
    subplots_2D_graph(fig, Y2, '$\sigma(\sigma_0)$', 2, delta, eta, 0)
    subplots_2D_graph(fig, Y3, '$\kappa_e(\kappa_0)$', 3, delta, eta, 0)
    subplots_2D_graph(fig, Y4, 'ZT(S,$\sigma$,$\kappa_e$)', 4, delta, eta, rk)
    
    return fig


# 3D plots
def find_ZTmax(X1, 
               X2,
               rk,
               ZT):
    
    ZTmax = np.amax(ZT, axis=1) # keep maximum values of ZT wrt to chemical potential (2D matrix delta x rk)
    
    return ZTmax

def plot_anim_3d(X1,
                 X2,
                 Z,
                 xlabel,
                 ylabel,
                 zlabel,
                 title): 
    
    fig = Figure(figsize=(5, 2.7))   
    ax = fig.add_subplot(projection='3d') # subplot
    ax.plot_surface(X1, X2, Z, cmap=cm.nipy_spectral_r, rstride=2, cstride=2)
    # label axes
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
        
    return fig