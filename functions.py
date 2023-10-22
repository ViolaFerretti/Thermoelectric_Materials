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
    function to calculate the formula log(x + exp(-x)), if x is an array

    Parameters
    ----------
    x : TYPE nd.ndarray
        DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    return np.log(1 + np.exp(-x))

def exp1(x):
    
    """
    function to calculate the formula [exp(x) + 1], if x is an array

    Parameters
    ----------
    x : TYPE nd.ndarray
        DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    return np.exp(x) + 1


# F functions for conduction band
def F0c(delta,
        eta):
    
    """
    function to calculate the F_0 function for the conduction band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function
    eta : TYPE nd.ndarray
          DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    return np.exp(eta - delta)/exp1(eta - delta)

def F1c(delta,
        eta):
    
    """
    function to calculate the F_1 function for the conduction band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function
    eta : TYPE nd.ndarray
          DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    return (eta - delta)/exp1(eta - delta) + log1(eta - delta)

def F2c(delta,
        eta):
    
    """
    function to calculate the F_2 function for the conduction band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function
    eta : TYPE nd.ndarray
          DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    return (np.pi**2)/3 - ((eta - delta)**2)/exp1(eta - delta) - 2*(eta - delta)*log1(eta - delta) + 2*plog(2, - np.exp( - (eta - delta)))

def F3c(delta,
        eta):
    
    """
    function to calculate theF_3 function for the conduction band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function
    eta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    return 2*(((eta - delta)**3)/exp1(eta - delta) + 3*((eta - delta)**2)*log1(eta - delta) - 6*(eta - delta)*plog(2, - np.exp( - (eta - delta))) - 6*plog(3, - np.exp( - (eta - delta))))


# F functions for valence band
def F0v(delta,
        eta):
    
    """
    function to calculate the F_0 function for the valence band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function
    eta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    return 1/exp1(eta + delta)

def F1v(delta,
        eta):
    
    """
    function to calculate the F_1 function for the valence band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function
    eta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    return - (eta + delta)/exp1(eta + delta) - log1(eta + delta)

def F2v(delta,
        eta):
    
    """
    function to calculate the F_2 function for the valence band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function
    eta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    return ((eta + delta)**2)/exp1(eta + delta) + 2*(eta + delta)*log1(eta + delta) - 2*plog(2, - np.exp( - (eta + delta)))

def F3v(delta,
        eta):
    
    """
    function to calculate the F_3 function for the valence band, if inputs are arrays

    Parameters
    ----------
    delta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function
    eta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    return 2*(((eta + delta)**3)/exp1(eta + delta) + 3*((eta + delta)**2)*log1(eta + delta) - 6*(eta + delta)*plog(2, - np.exp( - (eta + delta))) - 6*plog(3, - np.exp( - (eta + delta))))


# integrand to compute G functions 
def func_Gi(x,
            i,
            delta,
            eta):
    
    """
    function to calculate the G_i function

    Parameters
    ----------
    x : TYPE nd.ndarray
        DESCRIPTION. parameter to be entered in the calculation function
    i : TYPE int
        DESCRIPTION. index parameter to be entered in the calculation function
    delta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function
    eta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    if x == -eta:
        f=ZeroDivisionError
    else:
        f = ((delta**2)/((x + eta)**2))*((x**i)*(np.exp(x))/(exp1(x)**2))
    return f    

# G function for conduction band
def Gic(i,
        delta,
        eta):
    
    """
    function to calculate the G_i function integral for the conduction band

    Parameters
    ----------
    i : TYPE int
        DESCRIPTION. index parameter to be entered in the calculation function
    delta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function
    eta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    integral, error = quad(func_Gi, delta - eta, 300, (i, delta, eta), points=[-eta])
    return integral


# G function for valence band
def Giv(i,
        delta,
        eta):
    
    """
    function to calculate the G_i function integral for the valence band

    Parameters
    ----------
    i : TYPE int
        DESCRIPTION. index parameter to be entered in the calculation function
    delta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function
    eta : TYPE nd.ndarray
            DESCRIPTION. parameter to be entered in the calculation function

    Returns
    -------
    calculated function : TYPE nd.ndarray
                          DESCRIPTION. calculated array  

    """
    
    integral, error = quad(func_Gi, -300, -delta - eta, (i, delta, eta), points=[-eta])
    return integral


