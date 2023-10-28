# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:18:13 2023

@author: viola
"""

# import necessary modules 
import functions
from functions import *
import numpy as np
from mpmath import *

from SBM_Parabolic import *

# test of F integrand
def test_func_Fi_0_largex_pos():
            
    """
    function to test the function to calculate the F_i function integrand
    when i = 0 when x is large and positive

    ----------    
    DOC
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = 200 # input x value
    expected_output = 9.324621449370603e-90 # expected result
    
    assert func_Fi(value2, 0, value1) == expected_output

def test_func_Fi_1_largex_pos():
            
    """
    function to test the function to calculate the F_i function integrand
    when i = 1 when x is large and positive

    ----------    
    DOC
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = 200 # input x value
    expected_output = 1.8649242898741204e-87 # expected result
    
    assert func_Fi(value2, 1, value1) == expected_output

def test_func_Fi_2_largex_pos():
            
    """
    function to test the function to calculate the F_i function integrand
    when i = 2 when x is large and positive

    ----------    
    DOC
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = 200 # input x value
    expected_output = 3.729848579748241e-85 # expected result
    
    assert func_Fi(value2, 2, value1) == expected_output

def test_func_Fi_0_largex_neg():
            
    """
    function to test the function to calculate the F_i function integrand
    when i = 0 when x is large and negative

    ----------    
    DOC
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = -200 # input x value
    expected_output = 1.0 # expected result
    
    assert func_Fi(value2, 0, value1) == expected_output

def test_func_Fi_1_largex_neg():
            
    """
    function to test the function to calculate the F_i function integrand
    when i = 1 when x is large and negative

    ----------    
    DOC
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = -200 # input x value
    expected_output = -200.0 # expected result
    
    assert func_Fi(value2, 1, value1) == expected_output

def test_func_Fi_2_largex_neg():
            
    """
    function to test the function to calculate the F_i function integrand
    when i = 2 when x is large and negative

    ----------    
    DOC
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = -200 # input x value
    expected_output = 40000.0 # expected result
    
    assert func_Fi(value2, 2, value1) == expected_output

def test_func_Fi_0_smallx_pos():
            
    """
    function to test the function to calculate the F_i function integrand
    when i = 0 when x is small and positive

    ----------    
    DOC
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = 0.003 # input x value
    expected_output = 0.006672936241374847 # expected result
    
    assert func_Fi(value2, 0, value1) == expected_output

def test_func_Fi_1_smallx_pos():
            
    """
    function to test the function to calculate the F_i function integrand
    when i = 1 when x is small and positive

    ----------    
    DOC
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = 0.003 # input x value
    expected_output = 2.001880872412454e-05 # expected result
    
    assert func_Fi(value2, 1, value1) == expected_output

def test_func_Fi_2_smallx_pos():
            
    """
    function to test the function to calculate the F_i function integrand
    when i = 2 when x is small and positive

    ----------    
    DOC
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = 0.003 # input x value
    expected_output = 6.005642617237363e-08 # expected result
    
    assert func_Fi(value2, 2, value1) == expected_output

def test_func_Fi_0_smallx_neg():
            
    """
    function to test the function to calculate the F_i function integrand
    when i = 0 when x is small and negative

    ----------    
    DOC
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = -0.003 # input x value
    expected_output = 0.006712824638845502 # expected result
    
    assert func_Fi(value2, 0, value1) == expected_output

def test_func_Fi_1_smallx_neg():
            
    """
    function to test the function to calculate the F_i function integrand
    when i = 1 when x is small and negative

    ----------    
    DOC
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = -0.003 # input x value
    expected_output = -2.0138473916536507e-05 # expected result
    
    assert func_Fi(value2, 1, value1) == expected_output

def test_func_Fi_2_smallx_neg():
            
    """
    function to test the function to calculate the F_i function integrand
    when i = 2 when x is small and negative

    ----------    
    DOC
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = -0.003 # input x value
    expected_output = 6.041542174960951e-08 # expected result
    
    assert func_Fi(value2, 2, value1) == expected_output

# test of Fi function for conduction band
def test_Fic_0_neg():
    
    """
    DOC

    """
    
    value1 = -5 # input chemical potential value
    expected_output = 0.003357674244559035 # expected result
    
    assert float(Fic(0, value1)) == expected_output

def test_Fic_1_neg():
    
    """
    DOC

    """
    
    value1 = -5 # input chemical potential value
    expected_output = 0.0033633154387611988 # expected result
    
    assert float(Fic(1, value1)) == expected_output

def test_Fic_2_neg():
    
    """
    DOC
    ----------

    """
    
    value1 = -5 # input chemical potential value
    expected_output = 0.006732283305485879 # expected result
    
    assert float(Fic(2, value1)) == expected_output

def test_Fic_0_pos():
    
    """
    DOC
   

    """
    
    value1 = 19 # input chemical potential value
    expected_output = 9.500000002801396 # expected result
    
    assert float(Fic(0, value1)) == expected_output

def test_Fic_1_pos():
    
    """
    DOC
    

    """
    
    value1 = 19 # input chemical potential value
    expected_output = 91.07246703062272 # expected result
    
    assert float(Fic(1, value1)) == expected_output

def test_Fic_2_pos():
    
    """
    DOC
    
    """
    
    value1 = 19 # input chemical potential value
    expected_output = 1174.4204139423857 # expected result
    
    assert float(Fic(2, value1)) == expected_output

# test of thermoelectric quantities calculation

def test_sigma_neg():
            
    """
    DOC

    """
    
    value1 = -15 # input chemical potential value
    expected_output = 1.5295113685686032e-07 # expected result
    
    assert float(sigma_SBMP(value1)) == expected_output

def test_sigma_0():
            
    """
    DOC

    """
    
    value1 = 0 # input chemical potential value
    expected_output = 0.34657359027997264 # expected result
    
    assert float(sigma_SBMP(value1)) == expected_output

def test_sigma_pos():
        
    """
    DOC

    """
    
    value1 = 15 # input chemical potential value
    expected_output = 7.500000152951139 # expected result
    
    assert float(sigma_SBMP(value1)) == expected_output

def test_S_neg():
            
    """
    DOC

    """
    
    value1 = -15 # input chemical potential value
    expected_output = 17.000000152951127 # expected result
    
    assert float(S_SBMP(value1)) == expected_output

def test_S_0():
            
    """
    DOC
    
    """
    
    value1 = 0 # input chemical potential value
    expected_output = 2.3731382208312506 # expected result
    
    assert float(S_SBMP(value1)) == expected_output
    
def test_S_pos():
            
    """
    DOC

    """
    
    value1 = 15 # input chemical potential value
    expected_output = 0.21932419108440931 # expected result
    
    assert float(S_SBMP(value1)) == expected_output

def test_ke_neg():
            
    """
    DOC

    """
    
    value1 = -15 # input chemical potential value
    expected_output = 3.059022854108267e-07 # expected result
    
    assert float(ke_SBMP(value1)) == expected_output

def test_ke_0():
            
    """
    DOC

    """
    
    value1 = 0 # input chemical potential value
    expected_output = 0.752800079716631 # expected result
    
    assert float(ke_SBMP(value1)) == expected_output
    
def test_ke_pos():
            
    """
    DOC

    """
    
    value1 = 15 # input chemical potential value
    expected_output = 24.313282248185896 # expected result
    
    assert float(ke_SBMP(value1)) == expected_output

def test_ZT_neg():
            
    """
    DOC

    """
    
    value1 = -15 # input chemical potential value
    expected_output = 4.420286582527262e-05 # expected result
    
    assert float(ZT_SBMP(value1,1)) == expected_output

def test_ZT_0():
            
    """
    DOC

    """
    
    value1 = 0 # input chemical potential value
    expected_output = 1.1135485301369918 # expected result
    
    assert float(ZT_SBMP(value1,1)) == expected_output
    
def test_ZT_pos():
            
    """
    DOC

    """
    
    value1 = 15 # input chemical potential value
    expected_output = 0.014252330447763563 # expected result
    
    assert float(ZT_SBMP(value1,1)) == expected_output
