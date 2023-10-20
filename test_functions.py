# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:13:54 2023

@author: viola
"""

import functions
from functions import *
import numpy as np
#from hypothesis import given
#import hypothesis.strategies as st

# test of elementary functions

def test_log1():
    value=9
    print(log1(value))
    expected_output = 0.00012340218972333965
    assert log1(value) == expected_output    


def test_exp1():
    value=5
    print(exp1(value))
    expected_output = 149.4131591025766
    assert exp1(value) == expected_output

# test of F functions of the conduction band


def test_F0c():
    value1=3
    value2=13
    print(F0c(value1, value2))
    expected_output = 0.9999546021312976
    assert F0c(value1, value2) == expected_output

def test_F1c():
    value1=3
    value2=13
    print(F1c(value1, value2))
    expected_output = 0.0004993775862412144
    assert F1c(value1, value2) == expected_output

def test_F2c():
    value1=18
    value2=4
    print(F2c(value1, value2))
    expected_output = 0.000187925344988571
    assert np.isclose(float(F2c(value1, value2)), expected_output)

def test_F3c():
    value1=5
    value2=17
    print(F3c(value1, value2))
    expected_output = 0.0275013463014754
    assert np.isclose(float(F3c(value1, value2)), expected_output)

# test of F functions of valence band

def test_F0v():
    value1=6
    value2=-15
    print(F0v(value1, value2))
    expected_output = 0.9998766054240137
    assert F0v(value1, value2) == expected_output

def test_F1v():
    value1=6
    value2=-15
    print(F1v(value1, value2))
    expected_output = -0.001233953373599661
    assert F1v(value1, value2) == expected_output

def test_F2v():
    value1=6
    value2=-15
    print(F2v(value1, value2))
    expected_output = 3.27740512163292
    assert np.isclose(float(F2v(value1, value2)), expected_output)

def test_F3v():
    value1=6
    value2=-15
    print(F3v(value1, value2))
    expected_output = 0.254691498452758
    assert np.isclose(float(F3v(value1, value2)), expected_output)

# test of G functions

def test_func_Gi(): 
    
    value1=12
    value2=-5
    value3=52

    # test 1: i = 0
    i = 0
    print(func_Gi(value1,value2,value3,i))
    expected_output = 4.6365916132406466e-10
    assert np.isclose(float(func_Gi(value3, i, value1, value2)), expected_output)
    
    # test 2: i = 1
    i = 1
    print(func_Gi(value1,value2,value3,i))
    expected_output = 3.950705279921024e-10
    assert np.isclose(float(func_Gi(value3, i, value1, value2)), expected_output)
    
    # test 3: i = 2
    i = 2
    print(func_Gi(value1,value2,value3,i))
    expected_output = 3.4064754709523115e-10
    assert np.isclose(float(func_Gi(value3, i, value1, value2)), expected_output)
    
    # test 4: i = 3
    i = 3
    print(func_Gi(value1,value2,value3,i))
    expected_output = 2.9674186324740134e-10
    assert np.isclose(float(func_Gi(value3, i, value1, value2)), expected_output)


def test_Gic():
    
    value1=12
    value2=-5
    value3=52
    
    # test 1: i = 0
    i = 0
    print(Gic(i, value1, value2))
    expected_output = 3.581198434041771e-08
    assert np.isclose(float(Gic(i, value1, value2)), expected_output)
    
    # test 2: i = 1
    i = 1
    print(Gic(i, value1, value2))
    expected_output = 6.400404422663984e-07
    assert np.isclose(float(Gic(i, value1, value2)), expected_output)
    
    # test 3: i = 2
    i = 2
    print(Gic(i, value1, value2))
    expected_output = 1.1466614882245465e-05
    assert np.isclose(float(Gic(i, value1, value2)), expected_output)
    
    # test 4: i = 3
    i = 3
    print(Gic(i, value1, value2))
    expected_output = 0.0002059723191182534
    assert np.isclose(float(Gic(i, value1, value2)), expected_output)
  
def test_Giv(): 
    
    value1=17
    value2=-9

    # test 1: i = 0
    i = 0
    print(Giv(i, value1, value2))
    expected_output = 0.0003015760070507426
    assert np.isclose(float(Giv(i, value1, value2)), expected_output)
    
    # test 2: i = 1
    i = 1
    print(Giv(i, value1, value2))
    expected_output = -0.002685138951920471
    assert np.isclose(float(Giv(i, value1, value2)), expected_output)
    
    # test 3: i = 2
    i = 2
    print(Giv(i, value1, value2))
    expected_output = 0.02415602999913352
    assert np.isclose(float(Giv(i, value1, value2)), expected_output)
    
    # test 4: i = 3
    i = 3
    print(Giv(i, value1, value2))
    expected_output = -0.21995714831541316
    assert np.isclose(float(Giv(i, value1, value2)), expected_output)


