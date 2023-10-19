# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:11:30 2023

@author: viola
"""
###########################################
           #2D DIRAC MATERIALS#
###########################################


import matplotlib
matplotlib.use('TkAgg')


###########################################

from functions import F0c, F1c, F2c, F0v, F1v, F2v, Gic, Giv

############## CONDUCTION BAND ##############

#units of sigma0, S0, k0 

def sigmac_DBMD(delta,
                eta):
    return F0c(delta, eta) - Gic(0, delta, eta)

def Sc_DBMD(delta,
            eta):
    return - (F1c(delta, eta) - Gic(1, delta, eta))/(F0c(delta, eta) - Gic(0, delta, eta))

def kec_DBMD(delta,
             eta):
    return (F2c(delta, eta) - Gic(2, delta, eta)) - ((F1c(delta, eta) - Gic(1, delta, eta))**2)/(F0c(delta, eta) - Gic(0, delta, eta))

############## VALENCE BAND ##############

#TE quantities 
def sigmav_DBMD(delta,
                eta):
    return F0v(delta, eta) - Giv(0, delta, eta)

def Sv_DBMD(delta,
            eta):
    return - (F1v(delta, eta) - Giv(1, delta, eta))/(F0v(delta, eta) - Giv(0, delta, eta))

def kev_DBMD(delta,
             eta):
    return (F2v(delta, eta) - Giv(2, delta, eta)) - ((F1v(delta, eta) - Giv(1, delta, eta))**2)/(F0v(delta, eta) - Giv(0, delta, eta))

############## TE QUANTITIES OF THE MATERIAL ##############
def sigma_DBMD(delta,
               eta):
    return sigmac_DBMD(delta, eta) + sigmav_DBMD(delta, eta)

def S_DBMD(delta,
           eta):
    return (sigmac_DBMD(delta, eta)*Sc_DBMD(delta, eta) + sigmav_DBMD(delta, eta)*Sv_DBMD(delta, eta))/(sigmac_DBMD(delta, eta) + sigmav_DBMD(delta, eta))

def ke_DBMD(delta,
            eta):
    return ((sigmac_DBMD(delta, eta)*sigmav_DBMD(delta, eta))/(sigmac_DBMD(delta, eta) + sigmav_DBMD(delta, eta)))*(Sc_DBMD(delta, eta) - Sv_DBMD(delta, eta))**2 + kec_DBMD(delta, eta) + kev_DBMD(delta, eta)

def ZT_DBMD(delta,
            eta,
            rk):
    return ((S_DBMD(delta, eta)**2)*sigma_DBMD(delta, eta))/(ke_DBMD(delta,eta) + rk)

