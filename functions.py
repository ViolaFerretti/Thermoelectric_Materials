# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 11:14:14 2023

@author: viola
"""
# import necessary modules
import numpy as np
import mpmath
from scipy.integrate import quad

# useful elementary functions to recall later
plog = np.frompyfunc(mpmath.polylog, 2, 1)

def log1(x):
    
    """
    function to calculate the formula log(1 + exp(-x)),
    if x is an array

    Parameters
    ----------
    x : TYPE float
        DESCRIPTION variable that in later calculations will be given
        by the difference between the chemical potential and the energy gap

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the log(1 + exp(-x)) function

    """
    
    return np.log(1 + np.exp(-x))

def exp1(x):
    
    """
    function to calculate the formula [exp(x) + 1],
    if x is an array

    Parameters
    ----------
    x : TYPE float
        DESCRIPTION variable that in later calculations will be given
        by the difference between the chemical potential and the energy gap

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the [exp(x) + 1] function

    """
    
    return np.exp(x) + 1


# F functions for conduction band
def F0c(delta,
        eta):
    
    """
    function to calculate the F_0 function for the conduction band,
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
                          DESCRIPTION calculated value for the F_0 function for the conduction band 

    """
    
    return np.exp(eta - delta)/exp1(eta - delta)

def F1c(delta,
        eta):
    
    """
    function to calculate the F_1 function for the conduction band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the F_1 function for the conduction band  

    """
    
    exp = (eta - delta)/exp1(eta - delta) # 1st term (exponential dependency)
    log = log1(eta - delta) # 2nd term (logarithmic dependency)
    
    return exp + log

def F2c(delta,
        eta):
    
    """
    function to calculate the F_2 function for the conduction band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
          DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the F_2 function for the conduction band 

    """
    
    A = (np.pi**2)/3 # 1st term (constant)
    exp = -((eta - delta)**2)/exp1(eta - delta) # 2nd term (exponential dependency)
    log = -2*(eta - delta)*log1(eta - delta) # 3rd term (logarithmic dependency)
    polylog = 2*plog(2, -np.exp( -(eta - delta))) # 4th term (polylogarithmic)
    
    return A + exp + log + polylog

def F3c(delta,
        eta):
    
    """
    function to calculate theF_3 function for the conduction band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
            DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the F_3 function for the conduction band  

    """
    
    exp = ((eta - delta)**3)/exp1(eta - delta) # 1st term (exponential dependency)
    log = 3*((eta - delta)**2)*log1(eta - delta) # 2nd term (logarithmic dependency)
    polylog_1 = -6*(eta - delta)*plog(2, - np.exp( - (eta - delta))) # 3rd term (1st polylogarithmic term)
    polylog_2 = -6*plog(3, - np.exp( - (eta - delta))) # 4th term (2nd polylogarithmic term)
    
    return 2*(exp + log + polylog_1 + polylog_2)


# F functions for valence band
def F0v(delta,
        eta):
    
    """
    function to calculate the F_0 function for the valence band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
            DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the F_0 function for the valence band 

    """
    
    return 1/exp1(eta + delta)

def F1v(delta,
        eta):
    
    """
    function to calculate the F_1 function for the valence band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
            DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the F_1 function for the valence band  

    """
    
    exp = -(eta + delta)/exp1(eta + delta) # 1st term (exponential dependency)
    log = -log1(eta + delta) # 2nd term (logarithmic dependency)
    
    return exp + log

def F2v(delta,
        eta):
    
    """
    function to calculate the F_2 function for the valence band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
            DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the F_2 function for the valence band   

    """
    
    exp = ((eta + delta)**2)/exp1(eta + delta) # 1st term (exponential dependency)
    log = 2*(eta + delta)*log1(eta + delta) # 2nd term (logarithmic dependency)
    polylog = -2*plog(2, -np.exp(-(eta + delta))) # 3rd term (polylogarithmic term)
    
    return  exp + log + polylog

def F3v(delta,
        eta):
    
    """
    function to calculate the F_3 function for the valence band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
            DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the F_3 function for the valence band   

    """
    
    exp = ((eta + delta)**3)/exp1(eta + delta) # 1st term (exponential dependency)
    log = 3*((eta + delta)**2)*log1(eta + delta) # 2nd term (logarithmic dependency)
    polylog_1 = -6*(eta + delta)*plog(2, -np.exp( -(eta + delta))) # 3rd term (1st polylogarithmic term)
    polylog_2 = -6*plog(3, -np.exp(-(eta + delta))) # 4th term (2nd polylogarithmic term)
    
    return 2*(exp + log + polylog_1 + polylog_2)


# integrand to compute G functions 
def func_Gi(x,
            i,
            delta,
            eta):
    
    """
    function to calculate the G_i function integrand

    Parameters
    ----------
    x : TYPE nd.ndarray
        DESCRIPTION variable with respect to which the integration will be done,
        corresponding to the difference between the energy level and chemical potential
    i : TYPE int
        DESCRIPTION index parameter to be entered in the function,
        indicating the corresponding transport integral
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
            DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the G_i function integrand 

    """
    
    if x == -eta:
        f=ZeroDivisionError
    else:
        f = ((delta**2)/((x + eta)**2))*((x**i)*(np.exp(x))/(exp1(x)**2))
    
    return f    

# G function for conduction band
def Gic(func_Gi,
        i,
        delta,
        eta):
    
    """
    function to calculate the G_i function for the conduction band

    Parameters
    ----------
    func_Gi : TYPE function
              DESCRIPTION integrand function
    i : TYPE int
        DESCRIPTION index parameter to be entered in the function,
        indicating the corresponding transport integral
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
            DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the G_i function for the conduction band   

    """
    
    integral, error = quad(func_Gi, delta - eta, 300, (i, delta, eta), points=[-eta])
    
    return integral


# G function for valence band
def Giv(func_Gi,
        i,
        delta,
        eta):
    
    """
    function to calculate the G_i function for the valence band

    Parameters
    ----------
    func_Gi : TYPE function
              DESCRIPTION integrand function
    i : TYPE int
        DESCRIPTION index parameter to be entered in the function,
        indicating the corresponding transport integral
    delta : TYPE float
            DESCRIPTION energy gap value to be entered in the function
    eta : TYPE float
            DESCRIPTION chemical potential value to be entered in the function

    Returns
    -------
    calculated function : TYPE float
                          DESCRIPTION calculated value for the G_i function for the conduction band  

    """
    
    integral, error = quad(func_Gi, -300, -(delta + eta), (i, delta, eta), points=[-eta])
    
    return integral


