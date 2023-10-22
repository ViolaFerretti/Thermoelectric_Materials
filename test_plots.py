# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:24:35 2023

@author: viola
"""
# import necessary modules
import DBM_Parabolic
import SBM_Parabolic
from plots import subplots_2D_graph,complete_2d_plot,subplots_2D_graph_SBM,complete_2d_plot_SBM,plot_anim_3d

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

# testing of functions for 2D plots for double band models
def test_subplots_2D_graph(): #fig,Y,ylabel,sub,delta,eta,rk
    """
    Test the 2D subplot of the chosen thermoelectric quantity

    Returns
    -------
    None.

    """
    # test 1: Y=sigma 
    Y = DBM_Parabolic.S_DBMP
    ylabel = "Y"
    subplot_number = 1
    #legend=1
    delta = np.arange(0, 2, 0.5)
    eta = np.arange(0,2,0.5)
    rk = 1
    fig = Figure(figsize=(10, 4))
    
    fig1 = subplots_2D_graph(fig, Y, ylabel, subplot_number, delta, eta, rk)
    plt.show()
    
    assert isinstance(fig1, matplotlib.axes.SubplotBase), "subplots_2d_graph test failed"
    
   
    
def test_complete_2d_plot(): 
    
    """
    Test the 2D figure containing all the computed thermoelectric quantities

    Returns
    -------
    None.

    """
    
    Y1 = DBM_Parabolic.S_DBMP
    Y2 = DBM_Parabolic.sigma_DBMP
    Y3 = DBM_Parabolic.ke_DBMP
    Y4 = DBM_Parabolic.ZT_DBMP
    delta = np.arange(0, 2, 0.5)
    eta = np.arange(0, 2, 0.5)
    rk = 1
    title = 'plot'
    
    fig2=complete_2d_plot(Y1, Y2, Y3, Y4, delta, eta, rk, title)
    
    assert isinstance(fig2, plt.Figure), "complete_2d_plot test failed"

# testing of functions for 2D plots for single band model
def test_subplots_2D_graph_SBM(): 
    
    """
    Test the 2D subplot of the chosen thermoelectric quantity

    Returns
    -------
    None.

    """
    
    # test 1: Y=sigma 
    Y = SBM_Parabolic.S_SBMP
    ylabel = "Y"
    subplot_number = 1
    #legend=1
    eta = np.arange(0, 2, 0.5)
    rk = 1
    fig = Figure(figsize=(10, 4))
    
    fig1 = subplots_2D_graph_SBM(fig, Y, ylabel, subplot_number, eta, rk)
    plt.show()
    
    assert isinstance(fig1, matplotlib.axes.SubplotBase), "subplots_2d_graph_SBM test failed"

def test_complete_2d_plot_SBM():
    
    """
    Test the 2D figure containing all the computed thermoelectric quantities

    Returns
    -------
    None.

    """
    
    Y1 = SBM_Parabolic.S_SBMP
    Y2 = SBM_Parabolic.sigma_SBMP
    Y3 = SBM_Parabolic.ke_SBMP
    Y4 = SBM_Parabolic.ZT_SBMP
    eta = np.arange(0, 2, 0.5)
    rk = 1
    title = 'plot'
    
    fig2=complete_2d_plot_SBM(Y1, Y2, Y3, Y4, eta, rk, title)
    
    assert isinstance(fig2, plt.Figure), "complete_2d_plot_SBM test failed"

# testing of function for 3D plot
def test_plot_anim_3d():
    """
    function to test the 3D plot 

    Returns
    -------
    None.

    """
    X = np.array([[0, 1], [0, 1]])
    Y = np.array([[0, 0], [1, 1]])
    Z = np.array([[0, 1], [1, 0]])
    xlabel = "X"
    ylabel = "Y"
    zlabel = "Z"
    title = "3D Plot"
    i = 1
    
    fig = plot_anim_3d(X, Y, Z, xlabel, ylabel, zlabel, title, i)

    assert isinstance(fig, plt.Figure), "plot_anim_3d test failed"

