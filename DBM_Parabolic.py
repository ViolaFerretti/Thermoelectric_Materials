# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:20:02 2023

@author: viola
"""

import numpy as np
import matplotlib.pyplot as plt

from functions import F0c,F1c,F2c,F3c,F0v,F1v,F2v,F3v
from plots import subplots_2D_graph,plot_anim_3d

###########################################
       #2D PARABOLIC BAND MATERIALS#
###########################################

##############CONDUCTION BAND##############

#TE quantities
#units of sigma0, S0, k0 (find way to calculate C!!!) sigma0and k0 different wrt Dirac

def sigmac(delta,eta):
    return 2*F1c(delta,eta)+(eta-delta)*2*F0c(delta,eta)

def Sc(delta,eta):
    return -(2*F2c(delta,eta)+(eta-delta)*2*F1c(delta,eta)) / (2*F1c(delta,eta)+(eta-delta)*2*F0c(delta,eta))#+small)

def kec(delta,eta):
    return (F3c(delta,eta)+(eta-delta)*2*F2c(delta,eta)) - ((2*F2c(delta,eta)+(eta-delta)*2*F1c(delta,eta))**2/(2*F1c(delta,eta)+(eta-delta)*2*F0c(delta,eta)))#+small) )

##############VALENCE BAND##############

#TE quantities 
def sigmav(delta,eta):
    return -2*F1v(delta,eta)+(eta+delta)*(-2)*F0v(delta,eta)

def Sv(delta, eta):
    return -(-2*F2v(delta,eta)+(eta+delta)*(-2)*F1v(delta,eta)) / (-2*F1v(delta,eta)+(eta+delta)*(-2)*F0v(delta,eta))#+small)

def kev(delta, eta):
    return (F3v(delta,eta)+(eta+delta)*(-2)*F2v(delta,eta)) - ((-2*F2v(delta,eta)+(eta+delta)*(-2)*F1v(delta,eta))**2/(-2*F1v(delta,eta)+(eta+delta)*(-2)*F0v(delta,eta)))#+small) )

##############TE QUANTITIES OF THE MATERIAL##############
def sigma(delta,eta):
     return sigmac(delta,eta)+sigmav(delta,eta)

def S(delta,eta):
    return (sigmac(delta,eta)*Sc(delta,eta)+sigmav(delta,eta)*Sv(delta,eta))/(sigmac(delta,eta)+sigmav(delta,eta))

def ke(delta,eta):
    return ((sigmac(delta,eta)*sigmav(delta,eta))/(sigmac(delta,eta)+sigmav(delta,eta)))*(Sc(delta,eta)-Sv(delta,eta))**2+kec(delta,eta)+kev(delta,eta)

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
    print(type(subplots_2D_graph(S,'S($S_0$)',1,1)))

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
    
    plot_anim_3d(2*delta1, rk1, ZTmax, '$E_{g}$','$\kappa_{L}$', '$ZT_{max}$($\Delta$,$\kappa_{L}$)', '3D plot: 2D double--parabolic-band material')