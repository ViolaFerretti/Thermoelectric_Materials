# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 12:21:32 2023

@author: viola
"""

# 2D SINGLE-PARABOLIC-BAND MATERIALS #

# import necessary modules 
import numpy as np
import mpmath
from scipy.integrate import quad
from functions import exp1

# useful functions
plog = np.frompyfunc(mpmath.polylog, 2, 1)

def func_Fi(x,
            i,
            eta):
    """
    function to calculate the F_i function

    Parameters
    ----------
    x : TYPE nd.ndarray
        DESCRIPTION variable with respect to which the integration will be done,
        corresponding to the difference between the energy level and chemical potential
    i : TYPE int
        DESCRIPTION index parameter to be entered in the function,
        indicating the corresponding transport integral
    eta : TYPE nd.ndarray
            DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    return (x)**i/(exp1(x - eta))
    
def Fic(i,
        eta):
    """
    function to calculate the F_i integral for the conduction band

    Parameters
    ----------
    i : TYPE int
        DESCRIPTION index parameter to be entered in the function,
        indicating the corresponding transport integral
    eta : TYPE nd.ndarray
            DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    return 0.5*quad(func_Fi, 0, 100, (i, eta))[0]

############## TE QUANTITIES OF THE MATERIAL ##############

def sigma_SBMP(eta):
    
    """
    function to calculate the electrical conductivity sigma of the material, if the input is an array

    Parameters
    ----------
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    
    return Fic(0, eta)

def S_SBMP(eta):
    
    """
    function to calculate the Seebeck coefficient of the material, if the input is an array

    Parameters
    ----------
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    
    return (2*Fic(1, eta) - eta*Fic(0, eta))/Fic(0, eta)

def ke_SBMP(eta):
    
    """
    function to calculate the thermal electronic conductivity k_e of the material, if the input is an array

    Parameters
    ----------
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    
    return 3*Fic(2, eta) - 4*eta*Fic(1, eta)+(eta**2)*Fic(0, eta) - ((2*Fic(1, eta) - eta*Fic(0, eta))**2)/Fic(0, eta)

def ZT_SBMP(eta,
            rk):
    
    """
    function to calculate the figure of merit ZT of the material

    Parameters
    ----------
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function
    rk : TYPE float
         DESCRIPTION thermal lattice conductivity value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    
    return ((S_SBMP(eta)**2)*sigma_SBMP(eta))/(ke_SBMP(eta) + rk)
    