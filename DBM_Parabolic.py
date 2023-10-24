# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:20:02 2023

@author: viola
"""

# 2D DOUBLE-PARABOLIC-BAND MATERIALS #

# import necessary functions 
from functions import F0c, F1c, F2c, F3c, F0v, F1v, F2v, F3v

# TE QUANTITIES - CONDUCTION BAND 

def sigmac_DBMP(delta,
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
    
    return 2*F1c(delta, eta) + (eta - delta)*2*F0c(delta, eta)

def Sc_DBMP(delta,
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
    
    return - (2*F2c(delta ,eta) + (eta - delta)*2*F1c(delta, eta))/(2*F1c(delta, eta) + (eta - delta)*2*F0c(delta, eta))#+small)

def kec_DBMP(delta,
             eta):
    
    """
    function to calculate the thermal electronic conductivity k_e for the conduction band,
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
    
    return (F3c(delta, eta) + (eta - delta)*2*F2c(delta, eta)) - ((2*F2c(delta, eta) + (eta - delta)*2*F1c(delta, eta))**2/(2*F1c(delta, eta) + (eta - delta)*2*F0c(delta, eta)))#+small) )

# TE QUANTITIES - VALENCE BAND 

def sigmav_DBMP(delta,
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
    
    return - 2*F1v(delta, eta) + (eta + delta)*(- 2)*F0v(delta, eta)

def Sv_DBMP(delta,
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
    
    return - (- 2*F2v(delta, eta) + (eta + delta)*(- 2)*F1v(delta, eta))/(- 2*F1v(delta, eta) + (eta + delta)*(- 2)*F0v(delta, eta))#+small)

def kev_DBMP(delta,
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
    
    return (F3v(delta, eta) + (eta + delta)*(- 2)*F2v(delta, eta)) - ((- 2*F2v(delta, eta) + (eta + delta)*(- 2)*F1v(delta, eta))**2/(- 2*F1v(delta, eta) + (eta + delta)*(- 2)*F0v(delta, eta)))#+small) )

# TE QUANTITIES OF THE MATERIAL

def sigma_DBMP(delta,
               eta):
    
    """
    function to calculate the electrical conductivity sigma for the material,
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
    
    return sigmac_DBMP(delta, eta) + sigmav_DBMP(delta, eta)

def S_DBMP(delta,
           eta):
    
    """
    function to calculate the Seebeck coefficient S for the material,
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
    
    return (sigmac_DBMP(delta, eta)*Sc_DBMP(delta, eta) + sigmav_DBMP(delta, eta)*Sv_DBMP(delta, eta))/(sigmac_DBMP(delta, eta) + sigmav_DBMP(delta, eta))

def ke_DBMP(delta,
            eta):
    
    """
    function to calculate the thermal electronic conductivity k_e for the material,
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
    
    return ((sigmac_DBMP(delta, eta)*sigmav_DBMP(delta, eta))/(sigmac_DBMP(delta, eta) + sigmav_DBMP(delta, eta)))*(Sc_DBMP(delta, eta) - Sv_DBMP(delta, eta))**2 + kec_DBMP(delta, eta) + kev_DBMP(delta, eta)

def ZT_DBMP(delta,
            eta,
            rk):
    
    """
    function to calculate the figure of merit ZT for the material,
    if inputs are arrays

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
    
    return ((S_DBMP(delta, eta)**2)*sigma_DBMP(delta, eta))/(ke_DBMP(delta, eta) + rk)#+kp(x))

