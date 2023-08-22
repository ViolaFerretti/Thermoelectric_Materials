# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:11:30 2023

@author: viola
"""
###########################################
           #2D DIRAC MATERIALS#
###########################################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('QtAgg')

###########################################

from functions import F0c,F1c,F2c,F0v,F1v,F2v,Gic,Giv
from plots import subplots_2D_graph,plot_anim_3d

############## CONDUCTION BAND ##############

#units of sigma0, S0, k0 

def sigmac(delta,eta):
    return F0c(delta,eta)-Gic(0,delta,eta)

def Sc(delta,eta):
    return -(F1c(delta,eta)-Gic(1,delta,eta))/(F0c(delta,eta)-Gic(0,delta,eta))

def kec(delta,eta):
    return (F2c(delta,eta)-Gic(2,delta,eta))-((F1c(delta,eta)-Gic(1,delta,eta))**2)/(F0c(delta,eta)-Gic(0,delta,eta))

############## VALENCE BAND ##############

#TE quantities 
def sigmav(delta,eta):
    return F0v(delta,eta)-Giv(0,delta,eta)

def Sv(delta, eta):
    return -(F1v(delta,eta)-Giv(1,delta,eta))/(F0v(delta,eta)-Giv(0,delta,eta))

def kev(delta, eta):
    return (F2v(delta,eta)-Giv(2,delta,eta))-((F1v(delta,eta)-Giv(1,delta,eta))**2)/(F0v(delta,eta)-Giv(0,delta,eta))

############## TE QUANTITIES OF THE MATERIAL ##############
def sigma(delta,eta):
    return sigmac(delta,eta)+sigmav(delta,eta)

def S(delta,eta):
    return (sigmac(delta,eta)*Sc(delta,eta)+sigmav(delta,eta)*Sv(delta,eta))/(sigmac(delta,eta)+sigmav(delta,eta))

def ke(delta,eta):
    return ((sigmac(delta,eta)*sigmav(delta,eta))/(sigmac(delta,eta)+sigmav(delta,eta)))*(Sc(delta,eta)-Sv(delta,eta))**2+kec(delta,eta)+kev(delta,eta)
#def kp(x):
#    return x*k0

def ZT(delta,eta,rk):
    return ((S(delta,eta)**2)*sigma(delta,eta))/(ke(delta,eta)+rk)#+kp(x))


############## PLOTS ##############

a=0

# 2D PLOTS

if a==0:
    plt.figure(figsize=(10,4))
    plt.suptitle('TE quantities of 2D Dirac double-band material')
    subplots_2D_graph(S,'S($S_0$)',1,1)
    subplots_2D_graph(sigma,'$\sigma(\sigma_0)$',2,0)
    subplots_2D_graph(ke, '$\kappa_e(\kappa_0)$', 3,0)
    subplots_2D_graph(ZT, 'ZT(S,$\sigma$,$\kappa_e$)', 4,0)


# 3D PLOTS 

if a==1:
    npoint=51
    delta, eta = np.meshgrid(np.linspace(0,10,npoint), np.linspace(-10,10,npoint))
    
    vectorized_function = np.vectorize(sigma)
    output = vectorized_function(delta,eta)
    sigma1=output.astype(float)
    plot_anim_3d(eta, delta, sigma1, '$\eta$', '$\Delta$', '$\sigma$($\eta$,$\Delta$)', '3D plot: 2D double-band Dirac material')
    
    vectorized_function = np.vectorize(S)
    output = vectorized_function(delta,eta)
    S1=output.astype(float)
    plot_anim_3d(eta, delta, S1, '$\eta$', '$\Delta$', 'S($\eta$,$\Delta$)', '3D plot: 2D double-band Dirac material')
    
    vectorized_function = np.vectorize(ke)
    output = vectorized_function(delta,eta)
    ke1=output.astype(float)
    plot_anim_3d(eta, delta, ke1, '$\eta$', '$\Delta$', '$\kappa_{e}$($\eta$,$\Delta$)', '3D plot: 2D double-band Dirac material')
        
    vectorized_function = np.vectorize(ZT)
    output = vectorized_function(delta,eta,1)
    ZT1=output.astype(float)
    plot_anim_3d(eta, delta, ZT1, '$\eta$', '$\Delta$', 'ZT($\eta$,$\Delta$)', '3D plot: 2D double-band Dirac material')


if a==2:
    npoint=21
    delta, eta, rk=np.meshgrid(np.linspace(0.002,15,npoint),np.linspace(0.002,15,npoint),np.linspace(1,5,npoint))   
    ZT_vectorized_function = np.vectorize(ZT)
    ZT_output = ZT_vectorized_function(delta,eta,rk)
    ZT1=ZT_output.astype(float) #3d matrix
    ZTmax=np.amax(ZT1,axis=1) #2d matrix delta,rk 10x10
    
    
    rk1,delta1=np.meshgrid(np.linspace(1,5,npoint),np.linspace(0.002,15,npoint))
    
    plot_anim_3d(2*delta1, rk1, ZTmax, '$E_{g}$','$\kappa_{L}$', '$ZT_{max}$($\Delta$,$\kappa_{L}$)', '3D plot: 2D double-band Dirac material')