# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:13:54 2023

@author: viola
"""

# import
import functions
from functions import *
import numpy as np


# test of elementary functions
def test_log1():
    
    """
    function to test the log(x + exp(-x)) calculation

    Returns
    -------
    None.

    """
    
    # test 1
    value = 9 # example value for x
    
    expected_output = 0.00012340218972333965 # expected result
    assert log1(value) == expected_output    
    
    # test 2
    value = 2.5 # example value for x
    
    expected_output = 0.07888973429254956 # expected result
    assert log1(value) == expected_output   

def test_exp1():
    
    """
    function to test the [exp(x) + 1] calculation

    Returns
    -------
    None.

    """
    
    # test 1
    value = 5 # example value for x
    
    expected_output = 149.4131591025766 # expected result
    assert exp1(value) == expected_output
    
    # test 2
    value = 7.6 # example value for x
    
    expected_output = 1999.1958951041172 # expected result
    assert exp1(value) == expected_output

# test of F functions of the conduction band

def test_F0c():

    """
    function to test the function to calculate the F_0 function for the conduction band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 3  # example value for energy gap
    value2 = 13 # example value for chemical potential
    
    expected_output = 0.9999546021312976 # expected result
    assert F0c(value1, value2) == expected_output
    
    # test 2
    value1 = 9 # example value for energy gap
    value2 = -2 # example value for chemical potential
    
    expected_output = 1.670142184809518e-05 # expected result
    assert F0c(value1, value2) == expected_output

def test_F1c():

    """
    function to test the function to calculate the F_1 function for the conduction band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 3 # example value for energy gap
    value2 = 13 # example value for chemical potential
    
    expected_output = 0.0004993775862412144 # expected result
    assert F1c(value1, value2) == expected_output
    
    # test 2
    value1 = 9 # example value for energy gap
    value2 = -2 # example value for chemical potential
    
    expected_output = 0.00020041720164520882 # expected result
    assert F1c(value1, value2) == expected_output

def test_F2c():
    
    """
    function to test the function to calculate the F_2 function for the conduction band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 18 # example value for energy gap
    value2 = 4 # example value for chemical potential
    
    expected_output = 0.000187925344988571 # expected result
    assert np.isclose(float(F2c(value1, value2)), expected_output)
    
    # test 2
    value1 = 3 # example value for energy gap
    value2 = 9.3 # example value for chemical potential
    
    expected_output = 3.19033163968246 # expected result
    assert np.isclose(float(F2c(value1, value2)), expected_output)

def test_F3c():
    
    """
    function to test the function to calculate the F_3 function for the conduction band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 5 # example value for energy gap
    value2 = 17 # example value for chemical potential
    
    expected_output = 0.0275013463014754 # expected result
    assert np.isclose(float(F3c(value1, value2)), expected_output)
    
    # test 2
    value1 = 1.2 # example value for energy gap
    value2 = -2 # example value for chemical potential
    
    expected_output = 7.05778150624795 # expected result
    assert np.isclose(float(F3c(value1, value2)), expected_output)


# test of F functions of valence band

def test_F0v():
    
    """
    function to test the function to calculate the F_0 function for the valence band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 6
    value2 = -15
    
    expected_output = 0.9998766054240137
    assert F0v(value1, value2) == expected_output
    
    # test 2
    value1 = 9
    value2 = -1
    
    expected_output = 0.0003353501304664781
    assert F0v(value1, value2) == expected_output

def test_F1v():
    
    """
    function to test the function to calculate the F_1 function for the valence band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 6
    value2 = -15
    
    expected_output = -0.001233953373599661
    assert F1v(value1, value2) == expected_output
    
    # test 2
    value1 = 3.3
    value2 = 14
    
    expected_output = -5.612502402258072e-07
    assert F1v(value1, value2) == expected_output

def test_F2v():
    
    """
    function to test the function to calculate the F_2 function for the valence band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 6
    value2 = -15
    
    expected_output = 3.27740512163292
    assert np.isclose(float(F2v(value1, value2)), expected_output)
    
    # test 2
    value1 = 9.7
    value2 = -4
    
    expected_output = 0.153114564841314
    assert np.isclose(float(F2v(value1, value2)), expected_output)

def test_F3v():
    
    """
    function to test the function to calculate the F_3 function for the valence band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 6
    value2 = -15
    
    expected_output = 0.254691498452758
    assert np.isclose(float(F3v(value1, value2)), expected_output)
    
    # test 2
    value1 = 19
    value2 = 5
    
    expected_output = 1.18554329424333e-6
    assert np.isclose(float(F3v(value1, value2)), expected_output)

# test of G functions

def test_func_Gi(): 
    
    """
    function to test the function to calculate the G_i function 

    Returns
    -------
    None.

    """
    
    value1 = 12 # example value for energy gap
    value2 = -5 # example value for chemical potential
    value3 = 52 # example value for x

    # test 1: i = 0
    i = 0
    
    expected_output = 1.701585269498187e-24
    assert np.isclose(float(func_Gi(value3, i, value1, value2)), expected_output)
    
    # test 2: i = 1
    i = 1
    
    expected_output = 8.848243401390573e-23
    assert np.isclose(float(func_Gi(value3, i, value1, value2)), expected_output)
    
    # test 3: i = 2
    i = 2
    
    expected_output = 4.601086568723097e-21
    assert np.isclose(float(func_Gi(value3, i, value1, value2)), expected_output)
    
    # test 4: i = 3
    i = 3
    
    expected_output = 2.392565015736011e-19
    assert np.isclose(float(func_Gi(value3, i, value1, value2)), expected_output)


def test_Gic():
    
    """
    function to test the function to calculate the G_i integral for the conduction band

    Returns
    -------
    None.

    """
    
    value1 = 12 # example value for energy gap
    value2 = -5 # example value for chemical potential
    
    # test 1: i = 0
    i = 0
    
    expected_output = 3.581198434041771e-08
    assert np.isclose(float(Gic(i, value1, value2)), expected_output)
    
    # test 2: i = 1
    i = 1
    
    expected_output = 6.400404422663984e-07
    assert np.isclose(float(Gic(i, value1, value2)), expected_output)
    
    # test 3: i = 2
    i = 2
    
    expected_output = 1.1466614882245465e-05
    assert np.isclose(float(Gic(i, value1, value2)), expected_output)
    
    # test 4: i = 3
    i = 3
    
    expected_output = 0.0002059723191182534
    assert np.isclose(float(Gic(i, value1, value2)), expected_output)
  
def test_Giv(): 
    
    """
    function to test the function to calculate the G_i integral for the valence band

    Returns
    -------
    None.

    """
    
    value1 = 17 # example value for energy gap
    value2 = -9 # example value for chemical potential

    # test 1: i = 0
    i = 0
    
    expected_output = 0.0003015760070507426
    assert np.isclose(float(Giv(i, value1, value2)), expected_output)
    
    # test 2: i = 1
    i = 1
    
    expected_output = -0.002685138951920471
    assert np.isclose(float(Giv(i, value1, value2)), expected_output)
    
    # test 3: i = 2
    i = 2
    
    expected_output = 0.02415602999913352
    assert np.isclose(float(Giv(i, value1, value2)), expected_output)
    
    # test 4: i = 3
    i = 3
    
    expected_output = -0.21995714831541316
    assert np.isclose(float(Giv(i, value1, value2)), expected_output)


