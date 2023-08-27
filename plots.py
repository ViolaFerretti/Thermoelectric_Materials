# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:34:11 2023

@author: viola
"""

from matplotlib import cm
from matplotlib.figure import Figure
from matplotlib.ticker import AutoMinorLocator
import numpy as np



# plots for double band models
def subplots_2D_graph(fig,Y,ylabel,sub,delta,eta,rk): #eta, Y
    # delta=np.arange(delta_min, delta_max, delta_st)
    # eta=np.arange(eta_min,eta_max,eta_st)
    ax1=fig.add_subplot(2,2,sub)
    ax1.grid()
    y=[]
    for i in range(delta.size):
        y.append(np.zeros(eta.size,float)) #i=delta,j=eta
    y=np.asarray(y)

    if sub==4:
        for i in range(eta.size):
            for j in range(delta.size):
                y[j][i]=Y(delta[j],eta[i],rk)
        for j in range(delta.size) :   
            ax1.plot(eta,y[j][:])
             
    else:
        for i in range(eta.size):
            for j in range(delta.size):
                y[j][i]=Y(delta[j],eta[i])
        for j in range(delta.size) :   
            ax1.plot(eta,y[j][:], label="\u0394=%f" % delta[j])
    
    if sub==1:
        ax1.legend(fontsize="6", loc="upper right")
    ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax1.set_ylabel(ylabel)
    
    if sub==3 or sub==4:
        ax1.set_xlabel('$\mu$ $(k_B T)$')
    return ax1

def complete_2d_plot(Y1,Y2,Y3,Y4,delta,eta,rk,title):
    fig=Figure(figsize=(10,4))
    fig.suptitle(title)
    subplots_2D_graph(fig,Y1,'S($S_0$)',1,delta,eta,0)
    subplots_2D_graph(fig,Y2,'$\sigma(\sigma_0)$',2,delta,eta,0)
    subplots_2D_graph(fig,Y3, '$\kappa_e(\kappa_0)$', 3,delta,eta,0)
    subplots_2D_graph(fig,Y4, 'ZT(S,$\sigma$,$\kappa_e$)', 4,delta,eta,rk)
    return fig

# plots for single band model
def subplots_2D_graph_SBM(fig,Y,ylabel,sub,eta,rk): #eta, Y
    ax1=fig.add_subplot(2,2,sub)
    ax1.grid()
    y0 = np.zeros(eta.size,float)
    if sub==4:
        for i in range(eta.size):
             y0[i] = Y(eta[i],rk)
    else:
        for i in range(eta.size):
             y0[i] = Y(eta[i])

    l1, =ax1.plot(eta, y0, color='orange', linestyle='-',linewidth=1.5)
    ax1.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax1.set_ylabel(ylabel)
    if sub==3 or sub==4:
        ax1.set_xlabel('$\mu$ $(k_B T)$')
    return ax1

def complete_2d_plot_SBM(Y1,Y2,Y3,Y4,eta,rk,title):
    fig=Figure(figsize=(10,4))
    fig.suptitle(title)
    subplots_2D_graph_SBM(fig,Y1,'S($S_0$)',1,eta,0)
    subplots_2D_graph_SBM(fig,Y2,'$\sigma(\sigma_0)$',2,eta,0)
    subplots_2D_graph_SBM(fig,Y3, '$\kappa_e(\kappa_0)$', 3,eta,0)
    subplots_2D_graph_SBM(fig,Y4, 'ZT(S,$\sigma$,$\kappa_e$)', 4,eta,rk)
    return fig


    
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
    if ind==0:
        fig=Figure(figsize=(5,2.7))
    if ind==1:
        fig=Figure(figsize=(6,5))
    ax = fig.add_subplot(projection='3d') 
    ax.plot_surface(X,Y,Z,cmap=cm.nipy_spectral_r, rstride=2, cstride=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    
    
    print("3D Plot done !")
    return fig

