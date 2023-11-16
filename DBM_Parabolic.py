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
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated values for sigma of the conduction band 

    """
    
    F_1 = 2*F1c(delta, eta) # 1st term (F1 contribution)
    F_0 = (eta - delta)*2*F0c(delta, eta) # 2nd term (F0 contribution)
    
    return F_1 + F_0

def Sc_DBMP(delta,
            eta):
    
    """
    function to calculate the Seebeck coefficient S for the conduction band,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated values for S of the conduction band

    """
    
    F_1_2 = (2*F2c(delta ,eta) + (eta - delta)*2*F1c(delta, eta)) # numerator (F2 and F1 contribution)
    F_1_0 = (2*F1c(delta, eta) + (eta - delta)*2*F0c(delta, eta)) # denominator (F1 and F0 contribution)
    
    return - F_1_2/F_1_0

def kec_DBMP(delta,
             eta):
    
    """
    function to calculate the thermal electronic conductivity k_e for the conduction band,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated values for k_e of the conduction band  

    """
    
    F_3_2 = (F3c(delta, eta) + (eta - delta)*2*F2c(delta, eta)) # 1st term (F3 and F2 contribution)
    F_2_1 = (2*F2c(delta, eta) + (eta - delta)*2*F1c(delta, eta))**2 # numerator of 2nd term (F2 and F1 contribution)
    F_1_0 = (2*F1c(delta, eta) + (eta - delta)*2*F0c(delta, eta)) #denominator of 2nd term (F1 and F2 contribution)
    return F_3_2 - F_2_1/F_1_0

# TE QUANTITIES - VALENCE BAND 

def sigmav_DBMP(delta,
                eta):
    
    """
    function to calculate the electrical conductivity sigma for the valence band,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated values for sigma of the valence band  

    """
    
    F_1 = 2*F1v(delta, eta) # 1st term (F1 contribution)
    F_2 = (eta + delta)*(-2)*F0v(delta, eta) # 2nd term (F0 contribution)
    
    return - F_1 + F_2

def Sv_DBMP(delta,
            eta):
    
    """
    function to calculate the Seebeck coefficient S for the valence band,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated values for S of the valence band  

    """
    
    F_2_1 = -2*F2v(delta, eta) + (eta + delta)*(-2)*F1v(delta, eta) # numerator (F2 and F1 contribution)
    F_1_0 = -2*F1v(delta, eta) + (eta + delta)*(-2)*F0v(delta, eta) # denominator (F1 and F0 contribution)
    
    return - F_2_1/F_1_0

def kev_DBMP(delta,
             eta):
    
    """
    function to calculate the thermal electronic conductivity k_e for the valence band,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated values for k_e of the valence band   

    """
    
    F_3_2 = F3v(delta, eta) + (eta + delta)*(- 2)*F2v(delta, eta) # 1st term (F3 and F2 contribution)
    F_2_1 = (-2*F2v(delta, eta) + (eta + delta)*(-2)*F1v(delta, eta))**2 # numerator of 2nd term (F2 and F1 contribution)
    F_1_0 = -2*F1v(delta, eta) + (eta + delta)*(-2)*F0v(delta, eta) # denominator of 3rd term (F1 and F0 contribution)
    
    return F_3_2 - F_2_1/F_1_0

# TE QUANTITIES OF THE MATERIAL

def sigma_DBMP(delta,
               eta):
    
    """
    function to calculate the electrical conductivity sigma for the material,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated values for sigma of the material   

    """
    
    return sigmac_DBMP(delta, eta) + sigmav_DBMP(delta, eta)

def S_DBMP(delta,
           eta):
    
    """
    function to calculate the Seebeck coefficient S for the material,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated values for S of the material  

    """
    
    sigma_S_c = sigmac_DBMP(delta, eta)*Sc_DBMP(delta, eta) # 1st term of numerator (conduction band sigma and S contribution)
    sigma_S_v = sigmav_DBMP(delta, eta)*Sv_DBMP(delta, eta) # 2nd term of numerator (valence band sigma and S contribution)
        
    return (sigma_S_c + sigma_S_v)/sigma_DBMP(delta, eta)

def ke_DBMP(delta,
            eta):
    
    """
    function to calculate the thermal electronic conductivity k_e for the material,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated values for k_e of the material  

    """
    
    sigma_cv = sigmac_DBMP(delta, eta)*sigmav_DBMP(delta, eta) # 1st factor of 1st term numerator (sigma contribution)
    S_c_v = Sc_DBMP(delta, eta) - Sv_DBMP(delta, eta) # 2nd factor of 1st term numerator (S contribution)
    ke_c_v = kec_DBMP(delta, eta) + kev_DBMP(delta, eta) # k_e contribution
    
    return (sigma_cv/sigma_DBMP(delta, eta))*(S_c_v)**2 + ke_c_v

def ZT_DBMP(delta,
            eta,
            rk):
    
    """
    function to calculate the figure of merit ZT for the material,
    if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function
    rk : TYPE float
         DESCRIPTION thermal lattice conductivity value to be entered in the function
    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated values for ZT of the material  

    """
    
    return ((S_DBMP(delta, eta)**2)*sigma_DBMP(delta, eta))/(ke_DBMP(delta, eta) + rk)

