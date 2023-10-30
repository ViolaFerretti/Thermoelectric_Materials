# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:24:35 2023

@author: viola
"""
# import necessary modules
from DBM_Parabolic import *
from SBM_Parabolic import *
from DBM_Dirac import *
from plots import create_matrix_DBM, create_matrix_SBM

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np


# testing of functions to create matrices of values to plot
# double band models
def test_create_matrix_DBM_sigma_DBMD():
    
    """
    function to test the creation of a matrix containing correct values of the
    electrical conductivity sigma computed in the double-Dirac-band model
    
    ----------    
    Given as inputs: the thermoelectric quantity sigma to calculate,
    a number indicating the subplot (1),
    an array of values for the energy gap (positive value in a realistic range)
    and an array of values for the chemical potential (negative, null and positive in a realistic range),
    and rk = 0,
    
    when the function is applied,
    
    it gives the expected results: a matrix of sigma values increasing along columns (fixed chemical potential, increasing energy gap)
    and initially decreasing (until 4th element) and then incresing along rows (fixed energy gap, increasing chemical potential)
    ----------

    """
    
    # input values
    Y = sigma_DBMD 
    sub = 1
    delta = np.arange(0, 4, 1)
    eta = np.arange(-3, 3, 1)
    rk = 0
    # expected output matrix of values
    expected_output = [[1., 1., 1., 1., 1., 1.],
                      [0.7534905, 0.59041838, 0.42060373, 0.34556551, 0.42060373, 0.59041838],
                      [0.46019411, 0.27986782, 0.15329349, 0.11051448, 0.15329349, 0.27986782],
                      [0.22557424, 0.10986525, 0.05122114, 0.03462449, 0.05122114, 0.10986525]]
    
    assert np.allclose(create_matrix_DBM(Y, sub, delta, eta, rk), expected_output, atol=1e-10)

def test_create_matrix_DBM_ke_DBMP():
    
    """
    function to test the creation of a matrix containing correct values of the
    thermal electronic conductivity ke computed in the double-Parabolic-band model
    ----------    
    Given as inputs: the thermoelectric quantity ke to calculate,
    a number indicating the subplot (3),
    an array of values for the energy gap (positive value in a realistic range)
    and an array of values for the chemical potential (negative, null and positive in a realistic range),
    and rk = 0,
    
    when the function is applied,
    
    it gives the expected results: a matrix of ke values decreasing along columns (fixed chemical potential, increasing energy gap)
    and decreasing, increasing towards local maximum, decreasing and increasing again along rows (fixed energy gap, increasing chemical potential) 
    ----------

    """
    
    # input values
    Y = ke_DBMP
    sub = 3
    delta = np.arange(0, 4, 1)
    eta = np.arange(-3, 3, 1)
    rk = 0
    # expected output matrix of values
    expected_output = [[19.96804623, 18.05317714, 19.60657931, 21.63702426, 19.60657931, 18.05317714],
                       [12.63071674, 10.59188483, 12.418841, 15.1329718, 12.418841, 10.59188483],
                       [7.14569757, 5.56937804, 7.1356376, 9.41843319, 7.1356376,  5.56937804],
                       [3.55211407, 2.68767867, 3.81121351, 5.29738007, 3.81121351, 2.68767867]]
    
    assert np.allclose(create_matrix_DBM(Y, sub, delta, eta, rk), expected_output, atol=1e-10)
 
def test_create_matrix_DBM_ZT_DBMD():
    
    """
    function to test the creation of a matrix containing correct values of the
    figure of merit ZT computed in the double-Dirac-band model
    
    ----------    
    Given as inputs: the thermoelectric quantity ZT to calculate,
    a number indicating the subplot (4),
    an array of values for the energy gap (positive value in a realistic range)
    and an array of values for the chemical potential (negative, null and positive in a realistic range),
    and rk positive in a realistic range,
    
    when the function is applied,
    
    it gives the expected results: a matrix of ZT values increasing along columns (fixed chemical potential, increasing energy gap)
    and decreasing (until 3rd-4th elements) and then increasing along rows (fixed energy gap, increasing chemical potential)
    ----------

    """
    
    # input values
    Y = ZT_DBMP
    sub = 4
    delta = np.arange(0, 3, 0.5)
    eta = np.arange(-2.5, 2.5, 1)
    rk = 2.5
    # expected output matrix of values
    expected_output = [[0.23614468, 0.16976463, 0.02741111, 0.02741111, 0.16976463],
                      [0.34341195, 0.26076388, 0.04247588, 0.04247588, 0.26076388],
                      [0.48581822, 0.37299289, 0.05903655, 0.05903655, 0.37299289],
                      [0.66578176, 0.49559258, 0.0744425, 0.0744425, 0.49559258],
                      [0.87507202, 0.60975508, 0.08635387, 0.08635387, 0.60975508],
                      [1.08781199, 0.69358919, 0.09333546, 0.09333546, 0.69358919]]
    
    assert np.allclose(create_matrix_DBM(Y, sub, delta, eta, rk), expected_output, atol=1e-10)


# single band models
def test_create_matrix_SBM_S():
    
    """
    function to test the creation of a matrix containing correct values of the
    Seebeck coefficient S computed in the single-parabolic-band model
    
    ----------    
    Given as inputs: the thermoelectric quantity S to calculate,
    a number indicating the subplot (2),
    and an array of values for the chemical potential (negative, null and positive in a realistic range),
    and rk = 0,
    
    when the function is applied,
    
    it gives the expected results: a matrix of S values decreasing along rows (with increasing chemical potential)
    ----------

    """
    
    # input values
    Y = S_SBMP
    sub = 2
    eta = np.arange(-6, 6, 0.5)
    rk = 0
    # expected output matrix of values
    expected_output = [8.00123818, 7.50204015, 7.00336018, 6.50553065, 6.00909327, 5.51492438,
                       5.02442482, 4.5397906,  4.0643589,  3.60295946, 3.16207733, 2.74949659,
                       2.37313822, 2.03925882, 1.75083951, 1.50709078, 1.30422239, 1.13681683,
                       0.99906753, 0.88555746, 0.79160897, 0.71335904, 0.64769772, 0.59215571]    
    
    assert np.allclose(create_matrix_SBM(Y, sub, eta, rk), expected_output, atol=1e-10)
  
    
def test_create_matrix_SBM_ZT():
    
    """
    function to test the creation of a matrix containing correct values of the
    figure of merit ZT computed in the single-parabolic-band model
    
    ----------    
    Given as inputs: the thermoelectric quantity ZT to calculate,
    a number indicating the subplot (4),
    and an array of values for the chemical potential (negative, null and positive in a realistic range),
    and rk = 4,
    
    when the function is applied,
    
    it gives the expected results: a matrix of ZT values increasing up to its maximum value, then decreasing along rows (with increasing chemical potential)
    ----------

    """
    
    # input values 
    Y = ZT_SBMP
    sub = 4
    eta = np.arange(-4.5, 5, 0.5)
    rk = 4
    # expected output matrix of values
    expected_output = [0.05828404, 0.08155155, 0.112267,   0.15147145, 0.19926791, 0.25390594,
                       0.31078345, 0.36206354, 0.39802635, 0.41066906, 0.39782816, 0.36440503,
                       0.31943175, 0.27168627, 0.22707774, 0.18840296, 0.15629091, 0.13023928,
                       0.10932144]
    
    assert np.allclose(create_matrix_SBM(Y, sub, eta, rk), expected_output, atol=1e-10)


