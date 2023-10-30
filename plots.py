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

# 2D plots for double band models
def create_matrix_DBM(Y,
                      sub, 
                      delta, 
                      eta, 
                      rk):
    
    """
    
    Function that returns a matrix containing the values
    of the thermoelectric quantity indicated as input with respect to
    the energy gap and the chemical potential indicated as inputs
    (the calculations are done based on double-band-models)
    
    Parameters
    ----------
    Y : TYPE numpy.ndarray
        DESCRIPTION. calculated thermoelectric quantity
    sub : TYPE int
          DESCRIPTION. position of the subplot in the complete figure (fig) that will be realized later
    delta : TYPE nd.ndarray
            DESCRIPTION. energy gap range
    eta : TYPE nd.ndarray
          DESCRIPTION. chemical potential range
    rk : TYPE float
         DESCRIPTION. r_k parameter
         

    Returns
    -------
    y : TYPE nd.array
        DESCRIPTION. matrix containing the values of the thermoelectric quantity in function of energy gap and chemical potential

    """
    
    # initialize matrix to zero
    y = [] 
    for i in range(delta.size):
        y.append(np.zeros(eta.size, float)) #i=delta,j=eta
    y = np.asarray(y)
    
    # calculate values to plot
    if sub == 4:
        for i in range(eta.size):
            for j in range(delta.size):
                y[j][i] = Y(delta[j],eta[i], rk) # calculate ZT
    else:
       for i in range(eta.size):
           for j in range(delta.size):
               y[j][i] = Y(delta[j], eta[i]) # calculate the thermoelectric quantity 
    
    return y

def subplots_2D_graph(fig,
                      create_matrix_DBM,
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
    create_matrix_DBM : TYPE function
                        DESCRIPTION function to calculate matrix of values to plot
    Y : TYPE numpy.ndarray
        DESCRIPTION. calculated thermoelectric quantity
    ylabel : TYPE string
             DESCRIPTION. label of the y-axis, indicating the plotted thermoelectric quantity 
    sub : TYPE int
          DESCRIPTION. position of the subplot in the complete figure (fig) that will be realized later
    delta : TYPE nd.ndarray
            DESCRIPTION. energy gap range
    eta : TYPE nd.ndarray
          DESCRIPTION. chemical potential range
    rk : TYPE float
         DESCRIPTION. r_k parameter
         

    Returns
    -------
    ax1 : TYPE matplotlib.figure.add_subplot(2, 2, sub)
        DESCRIPTION. subplot of the thermoelectric quantity in function of the chemical potential, for different energy gap values

    """

    ax1 = fig.add_subplot(2, 2, sub) # subplot
    ax1.grid() # add grid to subplot
    y = create_matrix_DBM(Y, sub, delta, eta, rk) # matrix of values to plot
    
    #create subplot
    for j in range(delta.size):   
        ax1.plot(eta, y[j][:], label="\u0394=%f" % delta[j]) # and plot it for different chemical potentials
    
    # legend only on the first subplot 
    if sub == 1:
        ax1.legend(fontsize="6", loc="upper right")
    
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
    
    """
    
    Function that returns a 2D figure containing all the computed thermoelectric quantities in function of the chemical potential, for different energy gap values 
    
    Parameters
    ----------
    Y1 : TYPE numpy.ndarray
         DESCRIPTION. calculated thermoelectric quantity 1
    Y2 : TYPE numpy.ndarray
         DESCRIPTION. calculated thermoelectric quantity 2
    Y3 : TYPE numpy.ndarray
         DESCRIPTION. calculated thermoelectric quantity 3
    Y4 : TYPE numpy.ndarray
         DESCRIPTION. calculated thermoelectric quantity 4
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
    # insert subplot in the figure
    subplots_2D_graph(fig, Y1, 'S($S_0$)', 1, delta, eta, 0)
    subplots_2D_graph(fig, Y2, '$\sigma(\sigma_0)$', 2, delta, eta, 0)
    subplots_2D_graph(fig, Y3, '$\kappa_e(\kappa_0)$', 3, delta, eta, 0)
    subplots_2D_graph(fig, Y4, 'ZT(S,$\sigma$,$\kappa_e$)', 4, delta, eta, rk)
    
    return fig


# 2D plots for single band model

def create_matrix_SBM(Y, 
                      sub, 
                      eta, 
                      rk):
    
    """
    
    Function that returns a matrix containing the values
    of the thermoelectric quantity indicated as input with respect to
    the chemical potential indicated as input
    (the calculations are done based on the single-band-model)
    
    Parameters
    ----------
    Y : TYPE numpy.ndarray
        DESCRIPTION. calculated thermoelectric quantity
    sub : TYPE int
          DESCRIPTION. position of the subplot in the complete figure (fig) that will be realized later
    eta : TYPE nd.ndarray
          DESCRIPTION. chemical potential range
    rk : TYPE float
         DESCRIPTION. r_k parameter
         

    Returns
    -------
    y : TYPE nd.array
        DESCRIPTION. matrix containing the values of the thermoelectric quantity in function of energy gap and chemical potential

    """
    
    y = np.zeros(eta.size, float) # initialize array to zero
    if sub == 4:
         for i in range(eta.size):
             y[i] = Y(eta[i], rk) #calculate ZT
    else:
        for i in range(eta.size):
              y[i] = Y(eta[i]) # calculate the thermoelectric quantity
    return y

def subplots_2D_graph_SBM(fig,
                          create_matrix_SBM,
                          Y,
                          ylabel,
                          sub,
                          eta,
                          rk): 

    """
    
    Function that returns a 2D subplot of the chosen thermoelectric quantity in function of the chemical potential, for different energy gap values 
    
    Parameters
    ----------
    fig: TYPE matplotlib.figure.Figure()
         DESCRIPTION. figure containing this subplot
    create_matrix_SBM : TYPE function
                        DESCRIPTION function to calculate matrix of values to plot
    Y : TYPE numpy.ndarray
        DESCRIPTION. calculated thermoelectric quantity
    ylabel : TYPE string
             DESCRIPTION. label of the y-axis, indicating the plotted thermoelectric quantity 
    sub : TYPE int
          DESCRIPTION. position of the subplot in the complete figure (fig) that will be realized later
    eta : TYPE nd.ndarray
          DESCRIPTION. chemical potential range
    rk : TYPE float
         DESCRIPTION. r_k parameter
         

    Returns
    -------
    ax1 : TYPE matplotlib.figure.add_subplot(2, 2, sub)
        DESCRIPTION. subplot of the thermoelectric quantity in function of the chemical potential, for different energy gap values

    """

    ax1 = fig.add_subplot(2, 2, sub) # subplot
    ax1.grid()# add grid to subplot
    y = create_matrix_SBM(Y, sub, eta, rk) # matrix of values to plot
    l1, = ax1.plot(eta, y, color='orange', linestyle='-', linewidth=1.5) # plot data
    
    # label axes
    ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax1.set_ylabel(ylabel)
    if sub == 3 or sub == 4: # label x-axis only for lower subplots
        ax1.set_xlabel('$\mu$ $(k_B T)$')
    
    return ax1

def complete_2d_plot_SBM(Y1,
                         Y2,
                         Y3,
                         Y4,
                         eta,
                         rk,
                         title):
    
    """
    
    Function that returns a 2D figure containing all the computed thermoelectric quantities in function of the chemical potential, for different energy gap values 
    
    Parameters
    ----------
    Y1 : TYPE numpy.ndarray
         DESCRIPTION. calculated thermoelectric quantity 1
    Y2 : TYPE numpy.ndarray
         DESCRIPTION. calculated thermoelectric quantity 2
    Y3 : TYPE numpy.ndarray
         DESCRIPTION. calculated thermoelectric quantity 3
    Y4 : TYPE numpy.ndarray
         DESCRIPTION. calculated thermoelectric quantity 4
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
    
    fig = Figure(figsize=(10, 4))# figure
    fig.suptitle(title) # title of the figure
    # insert subplot in the figure
    subplots_2D_graph_SBM(fig, Y1, 'S($S_0$)', 1, eta, 0)
    subplots_2D_graph_SBM(fig, Y2, '$\sigma(\sigma_0)$', 2, eta, 0)
    subplots_2D_graph_SBM(fig, Y3, '$\kappa_e(\kappa_0)$', 3, eta, 0)
    subplots_2D_graph_SBM(fig, Y4, 'ZT(S,$\sigma$,$\kappa_e$)', 4, eta, rk)
    
    return fig

# 3D plot
def plot_anim_3d(X,
                 Y,
                 Z,
                 xlabel,
                 ylabel,
                 zlabel,
                 title,
                 ind): 

    """function to do plots that rotate in 3D

    Parameters
    ----------
    X : TYPE numpy.ndarray
        DESCRIPTION. X data in the space (X,Y)
    Y : TYPE numpy.ndarray
        DESCRIPTION. Y data in the space (X,Y)
    Z : TYPE numpy.ndarray
        DESCRIPTION. Z data in function of the X,Y data 
    xlabel : TYPE string
        DESCRIPTION: Label of the x axis 
    ylabel : TYPE string 
        DESCRIPTION. Label of the y axis
    zlabel : TYPE string
        DESCRIPTION. Label of the z axis
    title : TYPE string
        DESCRIPTION. title of the graph 
    ind : TYPE int
          DESCRIPTION. index parameter to indicate if the graph is related to the first (0) or second (1) part of the simulation

    Returns
    -------
    fig : TYPE matplotlib.figure.Figure()
        DESCRIPTION. 3D figure 

    """
    
    # set dimensions
    if ind == 0: # for first part
        fig = Figure(figsize=(5, 2.7))
    if ind == 1: # for second part
        fig = Figure(figsize=(6, 5))
        
    ax = fig.add_subplot(projection='3d') # subplot
    ax.plot_surface(X, Y, Z, cmap=cm.nipy_spectral_r, rstride=2, cstride=2) # create 3D plot
    
    # label axes
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
        
    return fig

