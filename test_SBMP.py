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
    function to test the calculation of the F_i function integrand
    when i = 0 when x is large and positive

    ----------    
    Given a fixed input value of chemical potential and a large and positive input value for x, 
    when the function is applied, it gives the expected result:
    
    - x large and positive -> the function is positive and tends asintotically to 0
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = 200 # input x value
    expected_output = 9.324621449370603e-90 # expected result
    
    assert np.isclose(func_Fi(value2, 0, value1), expected_output, atol=1e-10)

def test_func_Fi_1_largex_pos():
            
    """
    function to test the calculation of the F_i function integrand
    when i = 1 when x is large and positive

    ----------    
    Given a fixed input value of chemical potential and a large and positive input value for x, 
    when the function is applied, it gives the expected result:
    
    - x large and positive -> the function is positive and tends asintotically to 0
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = 200 # input x value
    expected_output = 1.8649242898741204e-87 # expected result
    
    assert np.isclose(func_Fi(value2, 1, value1), expected_output, atol=1e-10)

def test_func_Fi_2_largex_pos():
            
    """
    function to test the calculation of the F_i function integrand
    when i = 2 when x is large and positive

    ----------    
    Given a fixed input value of chemical potential and a large and positive input value for x, 
    when the function is applied, it gives the expected result:
    
    - x large and positive -> the function is positive and tends asintotically to 0
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = 200 # input x value
    expected_output = 3.729848579748241e-85 # expected result
    
    assert np.isclose(func_Fi(value2, 2, value1), expected_output, atol=1e-10)

def test_func_Fi_0_largex_neg():
            
    """
    function to test the calculation of the F_i function integrand
    when i = 0 when x is large and negative

    ----------    
    Given a fixed input value of chemical potential and a large and negative input value for x, 
    when the function is applied, it gives the expected result:
    
    - x large and negative -> the function is positive and tends to 1
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = -200 # input x value
    expected_output = 1.0 # expected result
    
    assert np.isclose(func_Fi(value2, 0, value1), expected_output, atol=1e-10)

def test_func_Fi_1_largex_neg():
            
    """
    function to test the calculation of the F_i function integrand
    when i = 1 when x is large and negative

    ----------    
    Given a fixed input value of chemical potential and a large and negative input value for x, 
    when the function is applied, it gives the expected result:
    
    - x large and negative -> the function is negative and tends to -x
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = -200 # input x value
    expected_output = -200.0 # expected result
    
    assert np.isclose(func_Fi(value2, 1, value1), expected_output, atol=1e-10)

def test_func_Fi_2_largex_neg():
            
    """
    function to test the calculation of the F_i function integrand
    when i = 2 when x is large and negative

    ----------    
    Given a fixed input value of chemical potential and a large and negative input value for x, 
    when the function is applied, it gives the expected result:
    
    - x large and negative -> the function is positive and tends to (-x)^2 
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = -200 # input x value
    expected_output = 40000.0 # expected result
    
    assert np.isclose(func_Fi(value2, 2, value1), expected_output, atol=1e-10)

def test_func_Fi_0_smallx_pos():
            
    """
    function to test the calculation of the F_i function integrand
    when i = 0 when x is small and positive

    ----------    
    Given a fixed input value of chemical potential and a small and positive input value for x, 
    when the function is applied, it gives the expected result:
    
    - x small and positive -> the function is positive and tends to 0
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = 0.003 # input x value
    expected_output = 0.006672936241374847 # expected result
    
    assert np.isclose(func_Fi(value2, 0, value1), expected_output, atol=1e-10)

def test_func_Fi_1_smallx_pos():
            
    """
    function to test the calculation of the F_i function integrand
    when i = 1 when x is small and positive

    ----------    
    Given a fixed input value of chemical potential and a small and positive input value for x, 
    when the function is applied, it gives the expected result:
    
    - x small and positive -> the function is positive and tends to 0
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = 0.003 # input x value
    expected_output = 2.001880872412454e-05 # expected result
    
    assert np.isclose(func_Fi(value2, 1, value1), expected_output, atol=1e-10)

def test_func_Fi_2_smallx_pos():
            
    """
    function to test the calculation of the F_i function integrand
    when i = 2 when x is small and positive

    ----------    
    Given a fixed input value of chemical potential and a small and positive input value for x, 
    when the function is applied, it gives the expected result:
    
    - x small and positive -> the function is positive and tends to 0
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = 0.003 # input x value
    expected_output = 6.005642617237363e-08 # expected result
    
    assert np.isclose(func_Fi(value2, 2, value1), expected_output, atol=1e-10)

def test_func_Fi_0_smallx_neg():
            
    """
    function to test the calculation of the F_i function integrand
    when i = 0 when x is small and negative

    ----------    
    Given a fixed input value of chemical potential and a small and negative input value for x, 
    when the function is applied, it gives the expected result:
    
    - x small and negative -> the function is positive and tends to 0
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = -0.003 # input x value
    expected_output = 0.006712824638845502 # expected result
    
    assert np.isclose(func_Fi(value2, 0, value1), expected_output, atol=1e-10)

def test_func_Fi_1_smallx_neg():
            
    """
    function to test the calculation of the F_i function integrand
    when i = 1 when x is small and negative

    ----------    
    Given a fixed input value of chemical potential and a small and negative input value for x, 
    when the function is applied, it gives the expected result:
    
    - x small and negative -> the function is negative and tends to 0
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = -0.003 # input x value
    expected_output = -2.0138473916536507e-05 # expected result
    
    assert np.isclose(func_Fi(value2, 1, value1), expected_output, atol=1e-10)

def test_func_Fi_2_smallx_neg():
            
    """
    function to test the calculation of the F_i function integrand
    when i = 2 when x is small and negative

    ----------    
    Given a fixed input value of chemical potential and a small and negative input value for x, 
    when the function is applied, it gives the expected result:
    
    - x small and negative -> the function is positive and tends to 0
    ----------

    """
    value1 = -5 # input chemical potential value
    value2 = -0.003 # input x value
    expected_output = 6.041542174960951e-08 # expected result
    
    assert np.isclose(func_Fi(value2, 2, value1), expected_output, atol=1e-10)

# test of Fi function for conduction band
def test_Fic_0_neg():
    
    """
    function to test the calculation of the F_i function
    when i = 0 when the chemical potential is negative

    ----------    
    Given a negative input value of chemical potential,
    when the function is applied, it gives the expected result:
    
    - eta < 0 -> the function is positive and near to 0
    ----------

    """
    
    value1 = -5 # input chemical potential value
    expected_output = 0.003357674244559035 # expected result
    
    assert np.isclose(float(Fic(func_Fi, 0, value1)), expected_output, atol=1e-10)

def test_Fic_1_neg():
    
    """
    function to test the calculation of the F_i function
    when i = 1 when the chemical potential is negative

    ----------    
    Given a negative input value of chemical potential,
    when the function is applied, it gives the expected result:
    
    - eta < 0 -> the function is positive and near to 0
    ----------

    """
    
    value1 = -5 # input chemical potential value
    expected_output = 0.0033633154387611988 # expected result
    
    assert np.isclose(float(Fic(func_Fi, 1, value1)), expected_output, atol=1e-10)

def test_Fic_2_neg():
    
    """
    function to test the calculation of the F_i function
    when i = 2 when the chemical potential is negative

    ----------    
    Given a negative input value of chemical potential,
    when the function is applied, it gives the expected result:
    
    - eta < 0 -> the function is positive and near to 0
    ----------

    """
    
    value1 = -5 # input chemical potential value
    expected_output = 0.006732283305485879 # expected result
    
    assert np.isclose(float(Fic(func_Fi, 2, value1)), expected_output, atol=1e-10)

def test_Fic_0_pos():
    
    """
    function to test the calculation of the F_i function
    when i = 0 when the chemical potential is positive

    ----------    
    Given a positive input value of chemical potential,
    when the function is applied, it gives the expected result:
    
    - eta > 0 -> the function is positive and of the order of (eta)^1
    ----------

    """
    
    value1 = 19 # input chemical potential value
    expected_output = 9.500000002801396 # expected result
    
    assert np.isclose(float(Fic(func_Fi, 0, value1)), expected_output, atol=1e-10)

def test_Fic_1_pos():
    
    """
    function to test the calculation of the F_i function
    when i = 1 when the chemical potential is positive

    ----------    
    Given a positive input value of chemical potential,
    when the function is applied, it gives the expected result:
    
    - eta > 0 -> the function is positive and of the order of (eta)^2
    ----------

    """
    
    value1 = 19 # input chemical potential value
    expected_output = 91.07246703062272 # expected result
    
    assert np.isclose(float(Fic(func_Fi, 1, value1)), expected_output, atol=1e-10)

def test_Fic_2_pos():
    
    """
    function to test the calculation of the F_i function
    when i = 0 when the chemical potential is positive

    ----------    
    Given a positive input value of chemical potential,
    when the function is applied, it gives the expected result:
    
    - eta > 0 -> the function is positive and of the order of (eta)^3
    ----------

    """
    
    value1 = 19 # input chemical potential value
    expected_output = 1174.4204139423857 # expected result
    
    assert np.isclose(float(Fic(func_Fi, 2, value1)), expected_output, atol=1e-10)

# test of thermoelectric quantities calculation

def test_sigma_neg():
    
    """
    function to test the calculation the electrical conductivity sigma
    when the chemical potential is negative

    ----------    
    Given a negative input value of chemical potential (in a realistic range),
    when the function is applied, it gives the expected result:
    
    - eta < 0 -> sigma is positive and near to zero
    ----------

    """
    
    value1 = -15 # input chemical potential value
    expected_output = 1.5295113685686032e-07 # expected result
    
    assert np.isclose(float(sigma_SBMP(value1)), expected_output, atol=1e-10)

def test_sigma_0():
      
    """
    function to test the calculation the electrical conductivity sigma
    when the chemical potential is null

    ----------    
    Given a null input value of chemical potential,
    when the function is applied, it gives the expected result:
    
    - eta = 0 -> sigma is positive and of the order of e-1
    ----------

    """
    
    value1 = 0 # input chemical potential value
    expected_output = 0.34657359027997264 # expected result
    
    assert np.isclose(float(sigma_SBMP(value1)), expected_output, atol=1e-10)

def test_sigma_pos():
    
    """
    function to test the calculation the electrical conductivity sigma
    when the chemical potential is positive

    ----------    
    Given a positive input value of chemical potential (in a realistic range),
    when the function is applied, it gives the expected result:
    
    - eta > 0 -> sigma is positive and of the order of e+1
    ----------

    """
    
    value1 = 15 # input chemical potential value
    expected_output = 7.500000152951139 # expected result
    
    assert np.isclose(float(sigma_SBMP(value1)), expected_output, atol=1e-10)

def test_S_neg():
       
    """
    function to test the calculation the Seebeck coefficient S
    when the chemical potential is negative

    ----------    
    Given a negative input value of chemical potential (in a realistic range),
    when the function is applied, it gives the expected result:
    
    - eta < 0 -> S is positive and of the order of e+1
    ----------

    """
    
    value1 = -15 # input chemical potential value
    expected_output = 17.000000152951127 # expected result
    
    assert np.isclose(float(S_SBMP(value1)), expected_output, atol=1e-10)

def test_S_0():
      
    """
    function to test the calculation the Seebeck coefficient S
    when the chemical potential is null

    ----------    
    Given a null input value of chemical potential,
    when the function is applied, it gives the expected result:
    
    - eta = 0 -> S is positive and of the order of e+0
    ----------

    """
    
    value1 = 0 # input chemical potential value
    expected_output = 2.3731382208312506 # expected result
    
    assert np.isclose(float(S_SBMP(value1)), expected_output, atol=1e-10)
    
def test_S_pos():
     
    """
    function to test the calculation the Seebeck coefficient S
    when the chemical potential is positive

    ----------    
    Given a positive input value of chemical potential (in a realistic range),
    when the function is applied, it gives the expected result:
    
    - eta > 0 -> S is positive and of the order of e-1
    ----------

    """
    
    value1 = 15 # input chemical potential value
    expected_output = 0.21932419108440931 # expected result
    
    assert np.isclose(float(S_SBMP(value1)), expected_output, atol=1e-10)

def test_ke_neg():
      
    """
    function to test the calculation the thermal electronic conductivity ke
    when the chemical potential is negative

    ----------    
    Given a negative input value of chemical potential (in a realistic range),
    when the function is applied, it gives the expected result:
    
    - eta < 0 -> ke is positive and near to zero
    ----------

    """
    
    value1 = -15 # input chemical potential value
    expected_output = 3.059022854108267e-07 # expected result
    
    assert np.isclose(float(ke_SBMP(value1)), expected_output, atol=1e-10)

def test_ke_0():
       
    """
    function to test the calculation the thermal electronic conductivity ke
    when the chemical potential is null

    ----------    
    Given a null input value of chemical potential,
    when the function is applied, it gives the expected result:
    
    - eta = 0 -> ke is positive and near to 1
    ----------

    """
    
    value1 = 0 # input chemical potential value
    expected_output = 0.752800079716631 # expected result
    
    assert np.isclose(float(ke_SBMP(value1)), expected_output, atol=1e-10)
    
def test_ke_pos():
      
    """
    function to test the calculation the thermal electronic conductivity ke
    when the chemical potential is positive

    ----------    
    Given a positive input value of chemical potential (in a realistic range),
    when the function is applied, it gives the expected result:
    
    - eta > 0 -> ke is positive and of the order of e+1
    ----------

    """
    
    value1 = 15 # input chemical potential value
    expected_output = 24.313282248185896 # expected result
    
    assert np.isclose(float(ke_SBMP(value1)), expected_output, atol=1e-10)

def test_ZT_neg():
     
    """
    function to test the calculation the figure of merit ZT
    when the chemical potential is negative

    ----------    
    Given a negative input value of chemical potential (in a realistic range),
    when the function is applied, it gives the expected result:
    
    - eta < 0 -> ZT is positive and near to zero
    ----------

    """
    value1 = -15 # input chemical potential value
    expected_output = 4.420286582527262e-05 # expected result
    
    assert np.isclose(float(ZT_SBMP(value1, 1)), expected_output, atol=1e-10)

def test_ZT_0():
        
    """
    function to test the calculation the figure of merit ZT
    when the chemical potential is null

    ----------    
    Given a null input value of chemical potential,
    when the function is applied, it gives the expected result:
    
    - eta = 0 -> ZT is positive and of the order of e+0
    ----------

    """
    
    value1 = 0 # input chemical potential value
    expected_output = 1.1135485301369918 # expected result
    
    assert np.isclose(float(ZT_SBMP(value1, 1)), expected_output, atol=1e-10)
    
def test_ZT_pos():
       
    """
    function to test the calculation the figure of merit ZT
    when the chemical potential is positive

    ----------    
    Given a positive input value of chemical potential (in a realistic range),
    when the function is applied, it gives the expected result:
    
    - eta > 0 -> ZT is positive and approaching zero
    ----------

    """
    
    value1 = 15 # input chemical potential value
    expected_output = 0.014252330447763563 # expected result
    
    assert np.isclose(float(ZT_SBMP(value1, 1)), expected_output, atol=1e-10)
