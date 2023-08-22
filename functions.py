# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 11:14:14 2023

@author: viola
"""

import numpy as np
import pandas as pd
import mpmath
from scipy.integrate import quad

# polylogarithmic functions
plog = np.frompyfunc(mpmath.polylog, 2, 1)

# useful elementary functions to recall later
def log1(x):
    return np.log(1+np.exp(-x))
def exp1(x):
    return np.exp(x)+1


# F functions for conduction band
def F0c(delta, eta):
    return np.exp(eta-delta)/exp1(eta-delta)

def F1c(delta,eta):
    return (eta-delta)/exp1(eta-delta)+log1(eta-delta)

def F2c(delta,eta):
    return (np.pi**2)/3-((eta-delta)**2)/exp1(eta-delta)-2*(eta-delta)*log1(eta-delta)+2*plog(2,-np.exp(-(eta-delta)))

def F3c(delta,eta):
    return 2*( ((eta-delta)**3)/exp1(eta-delta) + 3*((eta-delta)**2)*log1(eta-delta) - 6*(eta-delta)*plog(2,-np.exp(-(eta-delta))) - 6*plog(3,-np.exp(-(eta-delta))) )


# F functions for valence band
def F0v(delta,eta):
    return 1/exp1(eta+delta)

def F1v(delta,eta):
    return -(eta+delta)/exp1(eta+delta)-log1(eta+delta)

def F2v(delta,eta):
    return ((eta+delta)**2)/exp1(eta+delta)+2*(eta+delta)*log1(eta+delta)-2*plog(2,-np.exp(-(eta+delta)))

def F3v(delta,eta):
    return 2*( ((eta+delta)**3)/exp1(eta+delta)+ 3*((eta+delta)**2)*log1(eta+delta) - 6*(eta+delta)*plog(2,-np.exp(-(eta+delta))) - 6*plog(3,-np.exp(-(eta+delta))) )


# integrand to compute G functions 
def func_Gi(x,i,delta,eta): #delta, eta
    #x=np.longlong(x)
    if x==-eta:
        f=ZeroDivisionError
    else:
        f=((delta**2)/((x+eta)**2))*((x**i)*(np.exp(x))/(exp1(x)**2))
    #return np.nanmin(f)
    return f    

# G function for conduction band
def Gic(i,delta,eta):
    #poles=np.where(pd.isnull(func_Gi))
    #print(poles)
    #func_Gi=np.nanmin(func_Gi)
    integral, error=quad(func_Gi, delta-eta,300, (i,delta,eta),points=[-eta])#,poles)#, np.where(x+eta==0))
    #print(error)
    return integral


# G function for valence band
def Giv(i,delta,eta):
    integral, error = quad(func_Gi, -300, -delta-eta, (i,delta,eta),points=[-eta])
    return integral


