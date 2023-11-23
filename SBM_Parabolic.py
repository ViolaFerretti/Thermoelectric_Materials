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
    function to calculate the F_i function integrand

    Parameters
    ----------
    x : TYPE nd.ndarray
        DESCRIPTION variable with respect to which the integration will be done,
        corresponding to the difference between the energy level and chemical potential
    i : TYPE int
        DESCRIPTION index parameter to be entered in the function,
        indicating the corresponding transport integral
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the F_i function integrand  

    """
    
    return (x)**i/(exp1(x - eta))
    
def Fic(func_Fi,
        i,
        eta):
    """
    function to calculate the F_i function for the conduction band

    Parameters
    ----------
    func_Fi : TYPE function
              DESCRIPTION integrand function
    i : TYPE int
        DESCRIPTION index parameter to be entered in the function,
        indicating the corresponding transport integral
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the F_i function 

    """
    
    return 0.5*quad(func_Fi, 0, 100, (i, eta))[0]

############## TE QUANTITIES OF THE MATERIAL ##############

def sigma_SBMP(eta):
    
    """
    function to calculate the electrical conductivity sigma of the material

    Parameters
    ----------
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for sigma  

    """
    
    return Fic(func_Fi, 0, eta)

def S_SBMP(eta):
    
    """
    function to calculate the Seebeck coefficient of the material

    Parameters
    ----------
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for S  

    """
    
    return (2*Fic(func_Fi, 1, eta) - eta*Fic(func_Fi, 0, eta))/Fic(func_Fi, 0, eta) 

def ke_SBMP(eta):
    
    """
    function to calculate the thermal electronic conductivity k_e of the material

    Parameters
    ----------
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for k_e  

    """
    
    F_2 = 3*Fic(func_Fi, 2, eta) # 1st term (F2 contribution)
    F_1 = 4*eta*Fic(func_Fi, 1, eta) # 2nd term (F1 contribution)
    F_0 = (eta**2)*Fic(func_Fi, 0, eta) # 3rd term (F0 contribution)
    F_1_0 = ((2*Fic(func_Fi, 1, eta) - eta*Fic(func_Fi, 0, eta))**2)/Fic(func_Fi, 0, eta) # 4th term (F1 and F0 contribution)
    
    return F_2 - F_1 + F_0 - F_1_0

def ZT_SBMP(eta,
            rk):
    
    """
    function to calculate the figure of merit ZT of the material

    Parameters
    ----------
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function
    rk : TYPE float
         DESCRIPTION thermal lattice conductivity value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for ZT  

    """
    
    return ((S_SBMP(eta)**2)*sigma_SBMP(eta))/(ke_SBMP(eta) + rk)
    