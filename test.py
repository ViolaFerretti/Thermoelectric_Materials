# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:13:54 2023

@author: viola
"""

import functions
from functions import *
import numpy as np
from hypothesis import given
import hypothesis.strategies as st

# test of elementary functions

@given(value = st.floats(min_value=-30, max_value=30))
def test_log1(value):
    print(value)
    expected_output = np.log(1 + np.exp(- value))
    assert log1(value) == expected_output    

@given(value = st.floats(min_value=-30, max_value=30))
def test_exp1(value):
    print(value)
    expected_output = np.exp(value) + 1
    assert exp1(value) == expected_output

# test of F functions of the conduction band

@given(value1 = st.floats(min_value=0, max_value=20), value2 = st.floats(min_value=-20, max_value=20))
def test_F0c(value1, value2):
    print(value1, value2)
    expected_output = np.exp(value2 - value1)/exp1(value2 - value1)
    assert F0c(value1, value2) == expected_output

@given(value1 = st.floats(min_value=0, max_value=20), value2 = st.floats(min_value=-20, max_value=20))
def test_F1c(value1, value2):
    print(value1, value2)
    expected_output = (value2 - value1)/exp1(value2 - value1) + log1(value2 - value1)
    assert F1c(value1, value2) == expected_output

@given(value1 = st.floats(min_value=0, max_value=20), value2 = st.floats(min_value=-20, max_value=20))
def test_F2c(value1, value2):
    print(value1, value2)
    expected_output = (np.pi**2)/3 - ((value2 - value1)**2)/exp1(value2 - value1) - 2*(value2 - value1)*log1(value2 - value1) + 2*plog(2, - np.exp(- (value2 - value1)))
    assert F2c(value1, value2) == expected_output

@given(value1 = st.floats(min_value=0, max_value=20), value2 = st.floats(min_value=-20, max_value=20))
def test_F3c(value1, value2):
    print(value1, value2)
    expected_output = 2*(((value2 - value1)**3)/exp1(value2 - value1) + 3*((value2 - value1)**2)*log1(value2 - value1) - 6*(value2 - value1)*plog(2, - np.exp(- (value2 - value1))) - 6*plog(3, - np.exp(- (value2 - value1))))
    assert F3c(value1, value2) == expected_output

# test of F functions of valence band

@given(value1 = st.floats(min_value=0, max_value=20), value2 = st.floats(min_value=-20, max_value=20))
def test_F0v(value1, value2):
    print(value1, value2)
    expected_output = 1/exp1(value1 + value2)
    assert F0v(value1, value2) == expected_output

@given(value1 = st.floats(min_value=0, max_value=20), value2 = st.floats(min_value=-20, max_value=20))
def test_F1v(value1, value2):
    print(value1, value2)
    expected_output = - (value1 + value2)/exp1(value1 + value2) - log1(value1 + value2)
    assert F1v(value1, value2) == expected_output

@given(value1 = st.floats(min_value=0, max_value=20), value2 = st.floats(min_value=-20, max_value=20))
def test_F2v(value1, value2):
    print(value1, value2)
    expected_output = ((value1 + value2)**2)/exp1(value1 + value2) + 2*(value1 + value2)*log1(value1 + value2) - 2*plog(2, - np.exp(- (value1 + value2)))
    assert F2v(value1, value2) == expected_output

@given(value1 = st.floats(min_value=0, max_value=20), value2 = st.floats(min_value=-20, max_value=20))
def test_F3v(value1, value2):
    print(value1, value2)
    expected_output = 2*(((value1 + value2)**3)/exp1(value1 + value2) + 3*((value1 + value2)**2)*log1(value1 + value2) - 6*(value1 + value2)*plog(2, - np.exp(- (value1 + value2))) - 6*plog(3, - np.exp(- (value1 + value2))))
    assert F3v(value1, value2) == expected_output

# test of G functions

@given(value1 = st.floats(min_value=0, max_value=20), value2 = st.floats(min_value=-20, max_value=20), value3=st.floats(1, 100))
def test_func_Gi(value1, value2, value3): #FAILED test.py::test_func_Gi - ZeroDivisionError: float division by zero
    
    # test 1: i = 0
    i = 0
    #print(value1,value2,value3,i)
    if value3 + value2 == 0:
        expected_output = ZeroDivisionError
    else:
        expected_output = ((value1**2)/((value3 + value2)**2))*((value3**i)*(np.exp(value3))/(exp1(value3)**2))
    assert ((func_Gi(value3, i, value1, value2) == expected_output) or (func_Gi(value3,i,value1,value2) == ZeroDivisionError and expected_output == ZeroDivisionError))# (np.isnan(func_Gi(value3,i,value1,value2)) and np.isnan(expected_output)))

    # test 2: i = 1
    i = 1
    if value3 + value2 == 0:
        expected_output = ZeroDivisionError
    else:
        expected_output = ((value1**2)/((value3 + value2)**2))*((value3**i)*(np.exp(value3))/(exp1(value3)**2))
    assert ((func_Gi(value3, i, value1, value2) == expected_output) or (func_Gi(value3, i, value1, value2) == ZeroDivisionError and expected_output == ZeroDivisionError))# (np.isnan(func_Gi(value3,i,value1,value2)) and np.isnan(expected_output)))
    
    # test 3: i = 2
    i = 2
    if value3 + value2 == 0:
        expected_output = ZeroDivisionError
    else:
        expected_output = ((value1**2)/((value3+value2)**2))*((value3**i)*(np.exp(value3))/(exp1(value3)**2))
    assert ((func_Gi(value3,i,value1,value2) == expected_output) or (func_Gi(value3, i, value1, value2) == ZeroDivisionError and expected_output == ZeroDivisionError))# (np.isnan(func_Gi(value3,i,value1,value2)) and np.isnan(expected_output)))
    
    # test 4: i = 3
    i = 3
    if value3 + value2 == 0:
        expected_output = ZeroDivisionError
    else:
        expected_output = ((value1**2)/((value3 + value2)**2))*((value3**i)*(np.exp(value3))/(exp1(value3)**2))
    assert ((func_Gi(value3, i, value1, value2) == expected_output) or (func_Gi(value3, i, value1, value2) == ZeroDivisionError and expected_output == ZeroDivisionError))# (np.isnan(func_Gi(value3,i,value1,value2)) and np.isnan(expected_output)))

@given(value1 = st.floats(min_value=0, max_value=20), value2 = st.floats(min_value=-20, max_value=20))#,value3=st.floats(1,100))
def test_Gic(value1,value2): #FAILED test.py::test_func_Gi - ZeroDivisionError: float division by zero
    
    # test 1: i = 0
    i = 0
    print(value1, value2, i)
    integral, error = quad(func_Gi, value1 - value2, 300, (i, value1, value2), points=[- value2])
    expected_output = integral
    assert Gic(i, value1, value2) == expected_output
    
    # test 2: i = 1
    i = 1
    print(value1, value2, i)
    integral, error = quad(func_Gi, value1 - value2, 300, (i, value1, value2), points=[- value2])
    expected_output = integral
    assert Gic(i, value1, value2) == expected_output
    
    # test 3: i = 2
    i = 2
    print(value1, value2, i)
    integral, error = quad(func_Gi, value - value2, 300, (i, value1, value2), points=[- value2])
    expected_output = integral
    assert Gic(i, value1, value2) == expected_output
    
    # test 4: i = 3
    i = 3
    print(value1, value2, i)
    integral, error = quad(func_Gi, value1 - value2, 300, (i, value1, value2), points=[- value2])
    expected_output = integral
    assert Gic(i, value1, value2 )== expected_output
    
@given(value1 = st.floats(min_value=0, max_value=20), value2 = st.floats(min_value=-20, max_value=20))#,value3=st.floats(1,100))
def test_Giv(value1, value2): #FAILED test.py::test_func_Gi - ZeroDivisionError: float division by zero
    
    # test 1: i = 0
    i = 0
    print(value1, value2, i)
    integral, error = quad(func_Gi, - 300, - value1 - value2, (i, value1, value2), points=[- value2])
    expected_output = integral
    assert Giv(i, value1, value2) == expected_output
    
    # test 2: i = 1
    i = 1
    print(value1, value2, i)
    integral, error = quad(func_Gi, - 300, - value1 - value2, (i, value1, value2), points=[- value2])
    expected_output = integral
    assert Giv(i, value1, value2) == expected_output
    
    # test 3: i = 2
    i = 2
    print(value1, value2, i)
    integral, error = quad(func_Gi, - 300, - value1 - value2, (i, value1, value2), points=[- value2])
    expected_output = integral
    assert Giv(i, value1, value2) == expected_output
    
    # test 4: i = 3
    i = 3
    print(value1, value2, i)
    integral, error = quad(func_Gi, - 300, - value1 - value2, (i, value1, value2), points=[- value2])
    expected_output = integral
    assert Giv(i, value1, value2) == expected_output


