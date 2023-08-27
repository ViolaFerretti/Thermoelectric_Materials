# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 12:21:32 2023

@author: viola
"""

import numpy as np
import mpmath
from scipy.integrate import quad
#import matplotlib.pyplot as plt
#from matplotlib.ticker import AutoMinorLocator
from functions import exp1

plog = np.frompyfunc(mpmath.polylog, 2, 1)

def func_Fi(x,i,eta): #delta, eta
    #x=np.longlong(x)
    return (x)**i/(exp1(x-eta))
    
def Fic(i,eta):
    return 0.5*quad(func_Fi, 0,100, (i,eta))[0]
    #if p-doped    
    #return quad(func_Fi, -100, 0, (i,eta))[0]
    #return -0.5*plog(i+1,-np.exp(eta))

def sigma_SBMP(eta):
    return Fic(0,eta)

def S_SBMP(eta):
    return (2*Fic(1,eta)-eta*Fic(0,eta))/Fic(0,eta)

def ke_SBMP(eta):
    return 3*Fic(2,eta)-4*eta*Fic(1,eta)+(eta**2)*Fic(0,eta)-((2*Fic(1,eta)-eta*Fic(0,eta))**2)/Fic(0,eta)

def ZT_SBMP(eta,rk):
    return ((S_SBMP(eta)**2)*sigma_SBMP(eta))/(ke_SBMP(eta)+rk)#+kp(x))
    #return (((2*Fic(1,eta)-eta*Fic(0,eta))**2)/(Fic(0,eta)*(3*Fic(2,eta)-4*eta*Fic(1,eta)+(eta**2)*Fic(0,eta))-(2*Fic(1,eta)-eta*Fic(0,eta))**2))*1/(1/ke(eta)+1)
##############PLOTS##############
# Text sizes
# plt.rc('font', size=12)        # controls default text sizes
# plt.rc('legend', fontsize=12)  # legend fontsize
# plt.rc('xtick', labelsize=10)  # fontsize of the x tick labels
# plt.rc('ytick', labelsize=10)  # fontsize of the y tick labels
# plt.rc('axes', labelsize=12)   # fontsize of the x and y labels

# Create sample points within [-10,10]:
# npoint=101
# eta=np.linspace(-10, 10, npoint)

# # Define the size of the entire plot
# plt.figure(figsize=(10,4))
# plt.suptitle('TE quantities of 2D single-parabolic-band material')

# # Subplot (a): Seebeck's coefficient
# ax1=plt.subplot(2,2,1)
# S0 = np.zeros(npoint,float)
# for i in range(eta.size):
#      S0[i] = S_SBMP(eta[i])
# plt.plot(eta, S0, color='red', linestyle='-',linewidth=1.5)
# plt.ylabel('$S$ $(S_0)$')

# # Subplot (b): Electrical conductivity
# ax2 = plt.subplot(2,2,2)
# sig0 = np.zeros(npoint,float)
# for i in range(eta.size):
#      sig0[i] = sigma_SBMP(eta[i])
# plt.plot(eta, sig0, color='red', linestyle='-',linewidth=1.5)
# plt.ylabel('$\sigma$ $(\sigma_0)$')

# # Subplot (c): Thermal conductivity (electron part)
# ax3 = plt.subplot(2,2,3)
# kappae0 = np.zeros(npoint,float)
# for i in range(eta.size):
#     kappae0[i] = ke_SBMP(eta[i])
# plt.plot(eta, kappae0, color='red', linestyle='-',linewidth=1.5)
# plt.xlabel('$\mu$ $(k_B T)$')
# plt.ylabel('$\kappa_e$ $(\kappa_0)$')

# # Subplot (d): KT
# ax4 = plt.subplot(2,2,4)
# ZT0 = np.zeros(npoint,float)
# for i in range(eta.size):
#     ZT0[i] = ZT_SBMP(eta[i],1)   
# plt.plot(eta, ZT0, color='red', linestyle='-',linewidth=1.5)
# plt.xlabel('$\mu$ $(k_B T)$')
# plt.ylabel('$ZT$')

# from plots import plot_anim_3d
# npoint=51
# eta,rk = np.meshgrid(np.linspace(-10,10,npoint), np.linspace(1,5,npoint))
# vectorized_function = np.vectorize(ZT_SBMP)
# output = vectorized_function(eta,rk)
# ZT1=output.astype(float)
# plot_anim_3d(eta, rk, ZT1, '$\eta$', '$\kappa_L$', 'ZT($\eta$,$\kappa_l$)', '3D plot: 2D single-parabolic-band material')
