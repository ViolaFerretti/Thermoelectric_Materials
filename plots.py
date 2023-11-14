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
    """
    
    Function that returns a matrix of computed values of the thermoelectric quantity of interest
    
    Parameters
    ----------
    function: TYPE function 
              DESCRIPTION. function to compute the thermoelectric quantity of interest, to vectorize
    variables : TYPE tuple of numpy.array or numpy.meshgrid
                DESCRIPTION tuple of parameters of called function (energy gap, chemical potential, thermal lattic econductivity)
    variable3 : TYPE float or None
                DESCRIPTION. value of the thermal lattice conductivity (when it is not an array, i.e. in the 2nd part of the study)
                             it is float if the thermoelectric quantity depends on it (ZT), while it is None if there is no dependency
         
    Returns
    -------
    f : TYPE tuple of arrays
        DESCRIPTION. tuple of numpy arrays containing computed values of the thermoelectric quantity of interest

    """
    vectorized_function = np.vectorize(function) # vectorize function
    if len(variables) == 1: 
        if variable3 == None: # case of function with 1 array as input variable 
            f = vectorized_function(variables[0]) 
        elif type(variable3) == float: # case of function with 1 array and 1 float as input variables 
            f = vectorized_function(variables[0], variable3)
    elif len(variables) == 2: 
        if variable3 == None: # case of function with 2 arrays as input variables 
            f = vectorized_function(variables[0], variables[1])
        elif type(variable3) == float: # case of function with 2 arrays and 1 float as input variables
            f = vectorized_function(variables[0], variables[1], variable3) 
    elif len(variables) == 3: # case of function with 3 arrays as input variables
        f = vectorized_function(variables[0], variables[1], variables[2])
    
    return f

def generate_arrays(npoint):
    """
    
    Function that returns arrays for energy gap and chemical potential useful in the 2nd part of the study
    
    Parameters
    ----------
    npoint : TYPE int
             DESCRIPTION. number of elements in the arrays to compute
             
    Returns
    -------
    TYPE list
    DESCRIPTION. list containing arrays for energy gap and chemical potential

    """
    
    delta = np.linspace(0.002, 10, npoint) # energy gap array
    eta = np.linspace(-10, 10, npoint) # chemical potential array
    
    return [delta, eta]

# 2D plots
def subplots_2D_graph(fig,
                      Y, 
                      ylabel,
                      sub,
                      delta,
                      eta,
                      rk): 
    """
    
    Function that returns a 2D subplot of the chosen thermoelectric quantity in function of the chemical potential, for different energy gap values 
    
    Parameters
    ----------
    fig: TYPE matplotlib.figure.Figure()
         DESCRIPTION. figure containing this subplot
    Y : TYPE tuple of arrays
        DESCRIPTION. tuple of numpy arrays containing computed values of the thermoelectric quantity of interest
    ylabel : TYPE string
             DESCRIPTION. label of the y-axis, indicating the plotted thermoelectric quantity 
    sub : TYPE int
          DESCRIPTION. position of the subplot in the complete figure (fig) that will be realized later
    delta : TYPE nd.ndarray
            DESCRIPTION. energy gap range
    eta : TYPE nd.ndarray
          DESCRIPTION. chemical potential range
    rk : TYPE float
         DESCRIPTION. r_k parameter for the thermal lattice cnductivity
         

    Returns
    -------
    ax1 : TYPE matplotlib.figure.add_subplot(2, 2, sub)
          DESCRIPTION. subplot of the thermoelectric quantity in function of the chemical potential, for different energy gap values

    """
    
    ax1 = fig.add_subplot(2, 2, sub) # subplot
    ax1.grid() # add grid to subplot
    if delta is not None: #create subplot
        for j in range(delta[0].size):
            ax1.plot(eta, Y, label="\u0394=%f" % delta[0][j]) # and plot it for different chemical potentials
        if sub == 1: # legend with delta values only on the first subplot 
            ax1.legend(fontsize="6", loc="upper right")
    else: 
        ax1.plot(eta, Y, color='orange', linestyle='-', linewidth=1.5) # plot data
    # set ticks on axes
    ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
    # label axes
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
    """
    
    Function that returns a 2D figure containing all the computed thermoelectric quantities in function of the chemical potential, for different energy gap values 
    
    Parameters
    ----------
    Y1 : TYPE tuple of arrays 1
         DESCRIPTION. 1st tuple of numpy arrays containing computed values of the thermoelectric quantity of interest
    Y2 : TYPE tuple of arrays 2
         DESCRIPTION. 2nd tuple of numpy arrays containing computed values of the thermoelectric quantity of interest
    Y3 : TYPE tuple of arrays 3
         DESCRIPTION. 3rd tuple of numpy arrays containing computed values of the thermoelectric quantity of interest
    Y4 : TYPE tuple of arrays 4
         DESCRIPTION. 4th tuple of numpy arrays containing computed values of the thermoelectric quantity of interest
    delta : TYPE nd.ndarray
            DESCRIPTION. energy gap range
    eta : TYPE nd.ndarray
          DESCRIPTION. chemical potential range
    rk : TYPE float
         DESCRIPTION. r_k parameter
    title : TYPE string
            DESCRIPTION. title of the plot    

    Returns
    -------
    fig : TYPE matplotlib.figure.Figure()
        DESCRIPTION. figure containing all the computed thermoelectric quantities in function of the chemical potential, for different energy gap values 

    """
    
    fig = Figure(figsize=(10, 4)) # figure
    fig.suptitle(title) # title of the figure
    # insert subplots in the figure
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
    """
    
    Function that returns the maximum value of ZT wrt chemical potential
    
    Parameters
    ----------
    X1 : TYPE np.meshgrid
         DESCRIPTION. meshgrid of energy gap values
    X2 : TYPE np.meshgrid
        DESCRIPTION. meshgrid of chemical potential values
    rk : TYPE np.meshgrid
         DESCRIPTION. meshgrid of r_k parameter values
    ZT : TYPE tuple of arrays
         DESCRIPTION. tuple of numpy arrays containing computed values of the figure of merit

    Returns
    -------
    ZTmax : TYPE ZT.amax
        DESCRIPTION. tuple of arrays containing maximum values of ZT wrt chemical potential

    """
    ZTmax = np.amax(ZT, axis=1) # keep maximum values of ZT wrt to chemical potential (2D matrix delta x rk)
    
    return ZTmax

def plot_anim_3d(X1,
                 X2,
                 Z,
                 xlabel,
                 ylabel,
                 zlabel,
                 title): 
    """function to do plots that rotate in 3D

    Parameters
    ----------
    X1 : TYPE numpy.ndarray
        DESCRIPTION. X data in the space (X,Y)
    X2 : TYPE numpy.ndarray
        DESCRIPTION. Y data in the space (X,Y)
    Z : TYPE tuple of arrays
        DESCRIPTION. tuple of numpy arrays containing computed values of the thermoelectric quantity of interest
    xlabel : TYPE string
        DESCRIPTION: Label of the x axis 
    ylabel : TYPE string 
        DESCRIPTION. Label of the y axis
    zlabel : TYPE string
        DESCRIPTION. Label of the z axis
    title : TYPE string
        DESCRIPTION. title of the graph 
    
    Returns
    -------
    fig : TYPE matplotlib.figure.Figure()
        DESCRIPTION. 3D figure 

    """
    
    fig = Figure(figsize=(5, 2.7)) # figure  
    ax = fig.add_subplot(projection='3d') # subplot
    ax.plot_surface(X1, X2, Z, cmap=cm.nipy_spectral_r, rstride=2, cstride=2) # plot surface
    # label axes
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
        
    return fig