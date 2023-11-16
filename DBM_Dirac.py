# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:11:30 2023

@author: viola
"""

# 2D DOUBLE-DIRAC-BAND MATERIALS #

# import necessary functions
from functions import F0c, F1c, F2c, F0v, F1v, F2v, Gic, Giv, func_Gi

# TE QUANTITIES - CONDUCTION BAND 

def sigmac_DBMD(delta,
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
    
    return F0c(delta, eta) - Gic(func_Gi, 0, delta, eta)

def Sc_DBMD(delta,
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
    
    F_G_0 = F0c(delta, eta) - Gic(func_Gi, 0, delta, eta) # numerator (F0, G0 contribution)
    F_G_1 = F1c(delta, eta) - Gic(func_Gi, 1, delta, eta) # denominator (F1, G1 contribution)
    
    return -F_G_1/F_G_0

def kec_DBMD(delta,
             eta):
    
    """
    function to calculate the thermal electronic conductivity k_e sigma for the conduction band,
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
    
    F_G_2 = F2c(delta, eta) - Gic(func_Gi, 2, delta, eta) # 1st term (F2, G2 contribution)
    F_G_1 = (F1c(delta, eta) - Gic(func_Gi, 1, delta, eta))**2 # 2nd term numerator (F1, G1 contribution)
    F_G_0 = F0c(delta, eta) - Gic(func_Gi, 0, delta, eta) # 2nd term denominator (F0, G0 contribution)
    
    return F_G_2 - F_G_1/F_G_0

# TE QUANTITIES - VALENCE BAND 

def sigmav_DBMD(delta,
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
    
    return F0v(delta, eta) - Giv(func_Gi, 0, delta, eta)

def Sv_DBMD(delta,
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
    
    F_G_1 = F1v(delta, eta) - Giv(func_Gi, 1, delta, eta) # numerator (F1, G1 contribution)
    F_G_0 = F0v(delta, eta) - Giv(func_Gi, 0, delta, eta) # denominator (F0, G0 contribution)
    
    return - F_G_1/F_G_0

def kev_DBMD(delta,
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
    
    F_G_2 = F2v(delta, eta) - Giv(func_Gi, 2, delta, eta) # 1st term (F2, G2 contribution)
    F_G_1 = (F1v(delta, eta) - Giv(func_Gi, 1, delta, eta))**2 # 2nd term numerator (F1, G1 contribution)
    F_G_0 = F0v(delta, eta) - Giv(func_Gi, 0, delta, eta) # 2nd term denominator (F0, G0 contribution)
    
    return F_G_2 - F_G_1/F_G_0

# TE QUANTITIES OF THE MATERIAL 

def sigma_DBMD(delta,
               eta):
    
    """
    function to calculate the electrical conductivity sigma of the material,
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
    
    return sigmac_DBMD(delta, eta) + sigmav_DBMD(delta, eta)

def S_DBMD(delta,
           eta):
    
    """
    function to calculate the Sebeck coefficient S of the material,
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
    
    sigma_S_c = sigmac_DBMD(delta, eta)*Sc_DBMD(delta, eta) # 1st term of numerator (conduction band sigma and S contribution)
    sigma_S_v = sigmav_DBMD(delta, eta)*Sv_DBMD(delta, eta) # 2nd term of numerator (valence band sigma and S contribution)
    
    return (sigma_S_v + sigma_S_c)/sigma_DBMD(delta, eta)

def ke_DBMD(delta,
            eta):
    
    """
    function to calculate the themal electronic conductivity k_e of the material,
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
    
    sigma_cv = sigmac_DBMD(delta, eta)*sigmav_DBMD(delta, eta) # 1st factor of 1st term numerator (sigma contribution)
    S_c_v = Sc_DBMD(delta, eta) - Sv_DBMD(delta, eta) # 2nd factor of 1st term numerator (S contribution)
    ke_c_v = kec_DBMD(delta, eta) + kev_DBMD(delta, eta) # 2nd term (k_e contribution)
    
    return (sigma_cv/sigma_DBMD(delta, eta))*(S_c_v)**2 + ke_c_v

def ZT_DBMD(delta,
            eta,
            rk):
    
    """
    function to calculate the figure of merit ZT of the material

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
    
    return ((S_DBMD(delta, eta)**2)*sigma_DBMD(delta, eta))/(ke_DBMD(delta,eta) + rk)

