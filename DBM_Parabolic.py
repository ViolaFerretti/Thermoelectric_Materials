# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:20:02 2023

@author: viola
"""

#import numpy as np
#import matplotlib.pyplot as plt

from functions import F0c, F1c, F2c, F3c, F0v, F1v, F2v, F3v
#from plots import subplots_2D_graph,plot_anim_3d

###########################################
       #2D PARABOLIC BAND MATERIALS#
###########################################

##############CONDUCTION BAND##############

#TE quantities
#units of sigma0, S0, k0 (find way to calculate C!!!) sigma0and k0 different wrt Dirac

def sigmac_DBMP(delta,
                eta):
    return 2*F1c(delta, eta) + (eta - delta)*2*F0c(delta, eta)

def Sc_DBMP(delta,
            eta):
    return - (2*F2c(delta ,eta) + (eta - delta)*2*F1c(delta, eta))/(2*F1c(delta, eta) + (eta - delta)*2*F0c(delta, eta))#+small)

def kec_DBMP(delta,
             eta):
    return (F3c(delta, eta) + (eta - delta)*2*F2c(delta, eta)) - ((2*F2c(delta, eta) + (eta - delta)*2*F1c(delta, eta))**2/(2*F1c(delta, eta) + (eta - delta)*2*F0c(delta, eta)))#+small) )

##############VALENCE BAND##############

#TE quantities 
def sigmav_DBMP(delta,
                eta):
    return - 2*F1v(delta, eta) + (eta + delta)*(- 2)*F0v(delta, eta)

def Sv_DBMP(delta,
            eta):
    return - (- 2*F2v(delta, eta) + (eta + delta)*(- 2)*F1v(delta, eta))/(- 2*F1v(delta, eta) + (eta + delta)*(- 2)*F0v(delta, eta))#+small)

def kev_DBMP(delta,
             eta):
    return (F3v(delta, eta) + (eta + delta)*(- 2)*F2v(delta, eta)) - ((- 2*F2v(delta, eta) + (eta + delta)*(- 2)*F1v(delta, eta))**2/(- 2*F1v(delta, eta) + (eta + delta)*(- 2)*F0v(delta, eta)))#+small) )

##############TE QUANTITIES OF THE MATERIAL##############
def sigma_DBMP(delta,
               eta):
     return sigmac_DBMP(delta, eta) + sigmav_DBMP(delta, eta)

def S_DBMP(delta,
           eta):
    return (sigmac_DBMP(delta, eta)*Sc_DBMP(delta, eta) + sigmav_DBMP(delta, eta)*Sv_DBMP(delta, eta))/(sigmac_DBMP(delta, eta) + sigmav_DBMP(delta, eta))

def ke_DBMP(delta,
            eta):
    return ((sigmac_DBMP(delta, eta)*sigmav_DBMP(delta, eta))/(sigmac_DBMP(delta, eta) + sigmav_DBMP(delta, eta)))*(Sc_DBMP(delta, eta) - Sv_DBMP(delta, eta))**2 + kec_DBMP(delta, eta) + kev_DBMP(delta, eta)

def ZT_DBMP(delta,
            eta,
            rk):
    return ((S_DBMP(delta, eta)**2)*sigma_DBMP(delta, eta))/(ke_DBMP(delta, eta) + rk)#+kp(x))

