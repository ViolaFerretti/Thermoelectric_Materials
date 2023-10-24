# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:11:30 2023

@author: viola
"""

# 2D DOUBLE-DIRAC-BAND MATERIALS #

# import necessary functions
from functions import F0c, F1c, F2c, F0v, F1v, F2v, Gic, Giv

# TE QUANTITIES - CONDUCTION BAND 

def sigmac_DBMD(delta,
                eta):
    
    """
    function to calculate the electrical conductivity sigma for the conduction band,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """ 
    
    return F0c(delta, eta) - Gic(0, delta, eta)

def Sc_DBMD(delta,
            eta):
    
    """
    function to calculate the Seebeck coefficient S for the conduction band,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    
    return - (F1c(delta, eta) - Gic(1, delta, eta))/(F0c(delta, eta) - Gic(0, delta, eta))

def kec_DBMD(delta,
             eta):
    
    """
    function to calculate the thermal electronic conductivity k_e sigma for the conduction band,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """ 
    
    return (F2c(delta, eta) - Gic(2, delta, eta)) - ((F1c(delta, eta) - Gic(1, delta, eta))**2)/(F0c(delta, eta) - Gic(0, delta, eta))

# TE QUANTITIES - VALENCE BAND 

def sigmav_DBMD(delta,
                eta):
    
    """
    function to calculate the electrical conductivity sigma for the valence band,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    
    return F0v(delta, eta) - Giv(0, delta, eta)

def Sv_DBMD(delta,
            eta):
    
    """
    function to calculate the Seebeck coefficient S for the valence band,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    
    return - (F1v(delta, eta) - Giv(1, delta, eta))/(F0v(delta, eta) - Giv(0, delta, eta))

def kev_DBMD(delta,
             eta):
    
    """
    function to calculate the thermal electronic conductivity k_e for the valence band,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    
    return (F2v(delta, eta) - Giv(2, delta, eta)) - ((F1v(delta, eta) - Giv(1, delta, eta))**2)/(F0v(delta, eta) - Giv(0, delta, eta))

# TE QUANTITIES OF THE MATERIAL 

def sigma_DBMD(delta,
               eta):
    
    """
    function to calculate the electrical conductivity sigma of the material,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    
    return sigmac_DBMD(delta, eta) + sigmav_DBMD(delta, eta)

def S_DBMD(delta,
           eta):
    
    """
    function to calculate the Sebeck coefficient S of the material,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    
    return (sigmac_DBMD(delta, eta)*Sc_DBMD(delta, eta) + sigmav_DBMD(delta, eta)*Sv_DBMD(delta, eta))/(sigmac_DBMD(delta, eta) + sigmav_DBMD(delta, eta))

def ke_DBMD(delta,
            eta):
    
    """
    function to calculate the themal electronic conductivity k_e of the material,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    
    return ((sigmac_DBMD(delta, eta)*sigmav_DBMD(delta, eta))/(sigmac_DBMD(delta, eta) + sigmav_DBMD(delta, eta)))*(Sc_DBMD(delta, eta) - Sv_DBMD(delta, eta))**2 + kec_DBMD(delta, eta) + kev_DBMD(delta, eta)

def ZT_DBMD(delta,
            eta,
            rk):
    
    """
    function to calculate the figure of merit ZT of the material

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE nd.ndarray
          DESCRIPTION chemical potential value to be entered in the function
    rk : TYPE float
         DESCRIPTION thermal lattice conductivity value to be entered in the function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION calculated array  

    """
    
    return ((S_DBMD(delta, eta)**2)*sigma_DBMD(delta, eta))/(ke_DBMD(delta,eta) + rk)

