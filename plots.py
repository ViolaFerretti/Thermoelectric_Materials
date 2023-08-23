# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:34:11 2023

@author: viola
"""
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d,Axes3D
import numpy as np
from matplotlib.ticker import AutoMinorLocator

# plots for double band models
def subplots_2D_graph(Y,ylabel,sub,delta_min,delta_max,delta_st,eta_min,eta_max,eta_st): #eta, Y
    #npoint=101
    delta=np.arange(delta_min, delta_max, delta_st)
    eta=np.arange(eta_min,eta_max,eta_st)
    #delta=np.array([0 , 2 , 4 , 6 , 8 , 10])
    ax1=plt.subplot(2,2,sub)
    plt.grid()
    y0 = np.zeros(eta.size,float)
    y1 = np.zeros(eta.size,float)
    y2 = np.zeros(eta.size,float)
    y3 = np.zeros(eta.size,float)
    y4 = np.zeros(eta.size,float)
    if sub==4:
        for i in range(eta.size):
             y0[i] = Y(delta[0],eta[i],1)
             y1[i] = Y(delta[1],eta[i],1)
             y2[i] = Y(delta[2],eta[i],1)
             y3[i] = Y(delta[3],eta[i],1)
             y4[i] = Y(delta[4],eta[i],1)
    else:
        for i in range(eta.size):
             y0[i] = Y(delta[0],eta[i])
             y1[i] = Y(delta[1],eta[i])
             y2[i] = Y(delta[2],eta[i])
             y3[i] = Y(delta[3],eta[i])
             y4[i] = Y(delta[4],eta[i])

    l1, =plt.plot(eta, y0, color='orange', linestyle='-',linewidth=1.5)
    l2, =plt.plot(eta, y1, color='red', linestyle='-',linewidth=1.5)
    l3, =plt.plot(eta, y2, color='fuchsia', linestyle='-',linewidth=1.5)
    l4, =plt.plot(eta, y3, color='royalblue', linestyle='-',linewidth=1.5)
    l5, =plt.plot(eta, y4, color='green', linestyle='-',linewidth=1.5)
    ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
    plt.ylabel(ylabel)
    if sub==1:
        labels1 = ["\u0394=0","\u0394=2","\u0394=4","\u0394=6","\u0394=8","\u0394=10"]
        l=[l1,l2,l3,l4,l5]
        plt.legend(l,labels1,fontsize="6", loc="upper right")
    if sub==3 or sub==4:
        plt.xlabel('$\mu$ $(k_B T)$')
    return ax1

def complete_2d_plot(Y1,Y2,Y3,Y4,delta_min,delta_max,delta_st,eta_min,eta_max,eta_st,title):
    fig=plt.figure(figsize=(10,4))
    plt.suptitle(title)
    subplots_2D_graph(Y1,'S($S_0$)',1,delta_min,delta_max,delta_st,eta_min,eta_max,eta_st)
    subplots_2D_graph(Y2,'$\sigma(\sigma_0)$',2,delta_min,delta_max,delta_st,eta_min,eta_max,eta_st)
    subplots_2D_graph(Y3, '$\kappa_e(\kappa_0)$', 3,delta_min,delta_max,delta_st,eta_min,eta_max,eta_st)
    subplots_2D_graph(Y4, 'ZT(S,$\sigma$,$\kappa_e$)', 4,delta_min,delta_max,delta_st,eta_min,eta_max,eta_st)
    return fig

# plots for single band model
def subplots_2D_graph_SBM(Y,ylabel,sub,eta_min,eta_max,eta_st): #eta, Y
    npoint=101
    eta=np.arange(eta_min,eta_max,eta_st)
    #delta=np.array([0 , 2 , 4 , 6 , 8 , 10])
    ax1=plt.subplot(2,2,sub)
    plt.grid()
    y0 = np.zeros(npoint,float)
    if sub==4:
        for i in range(eta.size):
             y0[i] = Y(eta[i],1)
             
    else:
        for i in range(eta.size):
             y0[i] = Y(eta[i])

    l1, =plt.plot(eta, y0, color='orange', linestyle='-',linewidth=1.5)
    ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
    plt.ylabel(ylabel)
    if sub==3 or sub==4:
        plt.xlabel('$\mu$ $(k_B T)$')
    return ax1

def complete_2d_plot_SBM(Y1,Y2,Y3,Y4,eta_min,eta_max,title):
    fig=plt.figure(figsize=(10,4))
    plt.suptitle(title)
    subplots_2D_graph_SBM(Y1,'S($S_0$)',1,eta_min,eta_max)
    subplots_2D_graph_SBM(Y2,'$\sigma(\sigma_0)$',2,eta_min,eta_max)
    subplots_2D_graph_SBM(Y3, '$\kappa_e(\kappa_0)$', 3,eta_min,eta_max)
    subplots_2D_graph_SBM(Y4, 'ZT(S,$\sigma$,$\kappa_e$)', 4,eta_min,eta_max)
    return fig


    
def plot_anim_3d(X,
                  Y,
                  Z,
                  xlabel,
                  ylabel,
                  zlabel,
                  title):

    """function to do plots that rotate in 3D

    Parameters
    ----------
    X : TYPE : numpy.ndarray
        DESCRIPTION. X data in the space (X,Y)
    Y : TYPE : numpy.ndarray
        DESCRIPTION. Y data in the space (X,Y)
    Z : TYPE : numpy.ndarray
        DESCRIPTION. Z data in function of the X,Y data 
    xlabel : TYPE : string
        DESCRIPTION: Label of the x axis 
    ylabel : TYPE : string 
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
    
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X,Y,Z,cmap=cm.nipy_spectral_r, rstride=2, cstride=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    plt.show()
    
    print("3D Plot done !")
    return fig

