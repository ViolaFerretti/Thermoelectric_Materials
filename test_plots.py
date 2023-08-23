# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:24:35 2023

@author: viola
"""

DBM_Parabolic = __import__('2BM_Parabolic')
from plots import subplots_2D_graph,plot_anim_3d
import matplotlib
import matplotlib.pyplot as plt
# testing functions for data representation
def test_subplots_2D_graph():
    """
    Test the 2D plot for an energy G

    Returns
    -------
    None.

    """
    # test 1: Y=sigma 
    Y = DBM_Parabolic.S
    ylabel = "Y"
    subplot_number = 1
    legend=1

    fig = subplots_2D_graph(Y,ylabel,subplot_number,legend)
    plt.show()
    
    assert isinstance(fig, matplotlib.axes.SubplotBase), "plot_2d test failed"
    # can add more tests
    
def test_plot_anim_3d():
    """
    function to test the ploting of the 3D plot with arrays

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

    fig = plot_anim_3d(X, Y, Z, xlabel, ylabel, zlabel, title)

    assert isinstance(fig, plt.Figure), "plot_anim_3d test failed"

