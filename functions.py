# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 11:14:14 2023

@author: viola
"""

import numpy as np
import mpmath
from scipy.integrate import quad

#polylogarithmic functions
plog = np.frompyfunc(mpmath.polylog, 2, 1)

#useful elementary functions to recall later
def log1(x):
    return np.log(1+np.exp(-x))
def exp1(x):
    return np.exp(x)+1

##############CONDUCTION BAND##############

#F functions
def F0c(delta, eta):
    return np.exp(eta-delta)/exp1(eta-delta)

def F1c(delta,eta):
    return (eta-delta)/exp1(eta-delta)+log1(eta-delta)

def F2c(delta,eta):
    return (np.pi**2)/3-((eta-delta)**2)/exp1(eta-delta)-2*(eta-delta)*log1(eta-delta)+2*plog(2,-np.exp(-(eta-delta)))

def F3c(delta,eta):
    return 2*( ((eta-delta)**3)/exp1(eta-delta) + 3*((eta-delta)**2)*log1(eta-delta) - 6*(eta-delta)*plog(2,-np.exp(-(eta-delta))) - 6*plog(3,-np.exp(-(eta-delta))) )

#G functions 
def func_Gi(x,i,delta,eta): #delta, eta
    #x=np.longlong(x)
    return ((delta**2)/((x+eta)**2))*((x**i)*(np.exp(x))/(exp1(x)**2))

def Gic(i,delta,eta):
    integral, error=quad(func_Gi, delta-eta,100, (i,delta,eta))
    return integral

##############VALENCE BAND##############

#F functions
def F0v(delta,eta):
    return 1/exp1(eta+delta)

def F1v(delta,eta):
    return -(eta+delta)/exp1(eta+delta)-log1(eta+delta)

def F2v(delta,eta):
    return ((eta+delta)**2)/exp1(eta+delta)+2*(eta+delta)*log1(eta+delta)-2*plog(2,-np.exp(-(eta+delta)))

def F3v(delta,eta):
    return 2*( ((eta+delta)**3)/exp1(eta+delta)+ 3*((eta+delta)**2)*log1(eta+delta) - 6*(eta+delta)*plog(2,-np.exp(-(eta+delta))) - 6*plog(3,-np.exp(-(eta+delta))) )

#G functions
def Giv(i,delta,eta):
    return quad(func_Gi, -100, -delta-eta, (i,delta,eta))[0]



