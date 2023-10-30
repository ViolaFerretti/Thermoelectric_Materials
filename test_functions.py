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
    function to test the log[1 + exp(-x)] calculation
    
    ----------
    Given an array of input values (which comprehends infinite, zero, positive and negative values),
    when the log1 function is applied, it gives an array containing the expected results
    - input = -inf -> expected output = -inf
    - input = float < 0 -> expected output > 0
    - input = 0 -> expected output = e
    - input > 0 -> the function tends asintotically to zero
    -------
   
    """
    
    value = np.asarray([-np.infty, -10, 0 ,10, np.infty]) # input x values
    expected_output = [np.infty, 1.00000454e+01, 6.93147181e-01, 4.53988992e-05, 0.00000000e+00] # expected results
    
    assert np.allclose(log1(value).astype(float), expected_output, atol=1e-10)
    

def test_exp1():
    
    """
    function to test the  [exp(x) + 1] calculation
    
    ----------
    Given an array of input values (which comprehends infinite, zero, positive and negative values),
    when the exp1 function is applied, it gives an array containing the expected results:
    - input = -inf -> expected output = 1
    - input = float -> expected output > 0
    - input = +inf -> expected output = inf
    -------
    
    """
    
    value = np.asarray([-np.infty, -10, 0 ,10, np.infty]) # input x values
    expected_output = [1.00000000e+00, 1.00004540e+00, 2.00000000e+00, 2.20274658e+04, np.infty] # expected results
    
    assert np.allclose(exp1(value).astype(float), expected_output, atol=1e-10)

# test of F functions of the conduction band
def test_F0c():
    
    """
    function to test the the function to calculate the F_0 function for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (which comprehends null and positive values in a realistic range),
    and an array of input values for the chemical potential (which comprehends null, positive and negative values in a realistic range)
    when the F0c function is applied, it gives an array containing the expected results:
    
    - if inputs such that (value2 - value1) < 0 (1st and 2nd elements of input arrays) -> F0c tends asintotically to 0
    - if inputs such that (value2 - value1) > 0 (3rd elements of input arrays) -> F0c tends asintotically to 1
    - if inputs such that (value2 - value1) = 0 (4th elements of input arrays) -> expected result = 0.5
    ----------

    """
    
    value1 = np.asarray([0, 1.5, 5, 20.5]) # input energy gap values 
    value2 = np.asarray([-20.5, 0 ,10, 20.5]) # input chemical potential values
    expected_output = [1.25015286e-09, 1.82425524e-01, 9.93307149e-01, 5.00000000e-01] # expected results
    
    assert np.allclose(F0c(value1, value2).astype(float), expected_output, atol=1e-10)

def test_F1c():
    
    """
    function to test the the function to calculate the F_1 function for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (which comprehends null and positive values in a realistic range),
    and an array of input values for the chemical potential (which comprehends null, positive and negative values in a realistic range)
    when the F1c function is applied, it gives an array containing the expected results:
    
    - if inputs such that (value2 - value1) < or > 0 (1st, 2nd and 3rd elements of input arrays) -> F1c is positive and tends asintotically to 0
    - if inputs such that (value2 - value1) = 0 (4th elements of input arrays) -> expected result = e
    ----------

    """
    
    value1 = np.asarray([0, 1.5, 5, 20.5]) # input energy gap values 
    value2 = np.asarray([-20.5, 0 ,10, 20.5]) # input chemical potential values
    expected_output = [2.68782863e-08, 4.75051564e-01, 4.01796031e-02, 6.93147181e-01] # expected results
    
    assert np.allclose(F1c(value1, value2).astype(float), expected_output, atol=1e-10)

def test_F2c():
    
    """
    function to test the the function to calculate the F_2 function for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (which comprehends null and positive values in a realistic range),
    and an array of input values for the chemical potential (which comprehends null, positive and negative values in a realistic range)
    when the F2c function is applied, it gives an array containing the expected results:
    
    - if inputs such that (value2 - value1) < 0 (1st and 2nd elements of input arrays) -> F2c is positive and tends asintotically to 0
    - if inputs such that (value2 - value1) = or > 0 (3rd and 4th elements of input arrays) -> F2c is positive 
    ----------

    """
    
    value1 = np.asarray([0, 1.5, 5, 20.5]) # input energy gap values 
    value2 = np.asarray([-20.5, 0 ,10, 20.5]) # input chemical potential values
    expected_output = [5.79133314e-07, 1.43826122e+00, 3.0419401139431073, 1.64493407e+00] # expected results
    
    assert np.allclose(F2c(value1, value2).astype(float), expected_output, atol=1e-10)

def test_F3c():
        
    """
    function to test the the function to calculate the F_3 function for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (which comprehends null and positive values in a realistic range),
    and an array of input values for the chemical potential (which comprehends null, positive and negative values in a realistic range)
    when the F3c function is applied, it gives an array containing the expected results:
        
    - if inputs such that (value2 - value1) < or > 0 (1st, 2nd and 3rd elements of input arrays) -> F3c is positive and tends asintotically to 0
    - if inputs such that (value2 - value1) = 0 (3rd and 4th elements of input arrays) -> F3c reaches the maximum value close to 10 

    ----------

    """
    
    value1 = np.asarray([0, 1.5, 5, 20.5]) # input energy gap values 
    value2 = np.asarray([-20.5, 0 ,10, 20.5]) # input chemical potential values
    expected_output = [2.50152443e-05, 1.03699281e+01, 3.1649002567560833, 1.08185121e+01] # expected results
    
    assert np.allclose(F3c(value1, value2).astype(float), expected_output, atol=1e-10)

# test of F functions of valence band

def test_F0v():
    
    """
    function to test the function to calculate the F_0 function for the valence band

    ----------    
    Given an array of input values for the energy gap (which comprehends null and positive values in a realistic range),
    and an array of input values for the chemical potential (which comprehends null, positive and negative values in a realistic range)
    when the F0v function is applied, it gives an array containing the expected results:
        
    - if inputs such that (value2 + value1) < 0 (1st elements of input arrays) -> F0v is positive and tends asintotically to 1
    - if inputs such that (value2 + value1) > 0 (2nd and 3rd elements of input arrays) -> F0v is positive and tends asintotically to 0
    - if inputs such that (value2 + value1) = 0 (4th elements of input arrays) -> F0v reaches the maximum value close to 10 

    ----------

    """
    
    value1 = np.asarray([0, 1.5, 15, 20.5]) # input energy gap values 
    value2 = np.asarray([-16.5, 0 ,10, -20.5]) # input chemical potential values
    expected_output = [9.99999999e-01, 1.82425524e-01, 1.38879439e-11, 5.00000000e-01] # expected results
    
    assert np.allclose(F0v(value1, value2).astype(float), expected_output, atol=1e-10)

def test_F1v():
    
    """
    function to test the function to calculate the F_1 function for the valence band

    ----------    
    Given an array of input values for the energy gap (which comprehends null and positive values in a realistic range),
    and an array of input values for the chemical potential (which comprehends null, positive and negative values in a realistic range)
    when the F1v function is applied, it gives an array containing the expected results:
        
    - if inputs such that (value2 + value1) < or > 0 (1st, 2nd and 3rd elements of input arrays) -> F1v is negative and tends asintotically to 1
    - if inputs such that (value2 + value1) = 0 (4th elements of input arrays) -> F1v reaches the minimum value close to -0.7

    ----------

    """
        
    value1 = np.asarray([0, 1.5, 15, 20.5]) # input energy gap values 
    value2 = np.asarray([-16.5, 0 ,10, -20.5]) # input chemical potential values
    expected_output = [-1.19448051e-06, -4.75051564e-01, -3.61086598e-10, -6.93147181e-01] # expected results
    
    assert np.allclose(F1v(value1, value2).astype(float), expected_output, atol=1e-10)

def test_F2v():
    
    """
    function to test the function to calculate the F_2 function for the valence band

    ----------    
    Given an array of input values for the energy gap (which comprehends null and positive values in a realistic range),
    and an array of input values for the chemical potential (which comprehends null, positive and negative values in a realistic range)
    when the F2v function is applied, it gives an array containing the expected results:
        
    - if inputs such that (value2 + value1) < 0 (1st elements of input arrays) -> F2v is positive and tends asintotically to 3.5
    - if inputs such that (value2 + value1) > 0 (2nd and 3rd elements of input arrays) -> F2v is positive and tends asintotically to 0 
    - if inputs such that (value2 + value1) = 0 (4th elements of input arrays) -> F2v reaches the minimum value close to 1.5

    ----------

    """
    
    value1 = np.asarray([0, 1.5, 15, 20.5]) # input energy gap values 
    value2 = np.asarray([-16.5, 0 ,10, -20.5]) # input chemical potential values
    expected_output = [3.289867554563159, 1.4382612217634507, 9.4021408961890241e-9, 1.6449340668482264] # expected results
    
    assert np.allclose(F2v(value1, value2).astype(float), expected_output, atol=1e-10)

def test_F3v():
        
    """
    function to test the function to calculate the F_3 function for the valence band

    ----------    
    Given an array of input values for the energy gap (which comprehends null and positive values in a realistic range),
    and an array of input values for the chemical potential (which comprehends null, positive and negative values in a realistic range)
    when the F3v function is applied, it gives an array containing the expected results:
        
    - if inputs such that (value2 + value1) < or < 0 (1st, 2nd and 3rd elements of input arrays) -> F3v is positive and tends asintotically to 0
    - if inputs such that (value2 + value1) = 0 (4th elements of input arrays) -> F3v reaches the minimum value close to 11

    ----------

    """
    
    value1 = np.asarray([0, 1.5, 15, 20.5]) # input energy gap values 
    value2 = np.asarray([-16.5, 0 ,10, -20.5]) # input chemical potential values
    expected_output = [0.00073905922545236535, 10.369928135499528, 4.9041129123324437e-7, 10.81851212843635] # expected results
    
    assert np.allclose(F3v(value1, value2).astype(float), expected_output, atol=1e-10)

# test of G functions

def test_func_Gi_0_pole():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 0 when poles are encountered

    ----------    
    Given input values such that the pole of the function is encountered,
    when the G_i function integrand is computed, it returns the ZeroDivisionError
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = 5 # input x value
    expected_output = ZeroDivisionError # expected result
    
    assert func_Gi(value3,0,value1,value2) == expected_output

def test_func_Gi_1_pole():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 1 when poles are encountered

    ----------    
    Given input values such that the pole of the function is encountered,
    when the G_i function integrand is computed, it returns the ZeroDivisionError
    ----------

    """
    value1 = 0 # input energy gap value
    value2 = -13.6 # input chemical potential value
    value3 = 13.6 # input x value
    expected_output = ZeroDivisionError # expected result
    
    assert func_Gi(value3,1,value1,value2) == expected_output
        
def test_func_Gi_2_pole():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 2 when poles are encountered

    ----------    
    Given input values such that the pole of the function is encountered,
    when the G_i function integrand is computed, it returns the ZeroDivisionError
    ----------

    """
    value1 = 0.001 # input energy gap value
    value2 = 0.2 # input chemical potential value
    value3 = -0.2 # input x value
    expected_output = ZeroDivisionError # expected result
    
    assert func_Gi(value3,2,value1,value2) == expected_output
        
def test_func_Gi_3_pole():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 3 when poles are encountered

    ----------    
    Given input values such that the pole of the function is encountered,
    when the G_i function integrand is computed, it returns the ZeroDivisionError
    ----------

    """
    value1 = 2.4 # input energy gap value
    value2 = 19 # input chemical potential value
    value3 = -19 # input x value
    expected_output = ZeroDivisionError # expected result
    
    assert func_Gi(value3,3,value1,value2) == expected_output
        
def test_func_Gi_0_largex_pos():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 0 when x is large and positive

    ----------    
    Given input values with x large and positive,
    when the G_i function integrand is computed, it returns the expected output:
    
    - input: value3 = large and positive -> output: positive and and closer to zero as i decreases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = 200 # input x value
    expected_output = 5.240791580541492e-90 # expected result
    
    assert np.isclose(func_Gi(value3,0,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_1_largex_pos():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 1 when x is large and positive

    ----------    
    Given input values with x large and positive,
    when the G_i function integrand is computed, it returns the expected output:
    
    - input: value3 = large and positive -> output: positive and and closer to zero as i decreases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = 200 # input x value
    expected_output = 1.0481583161082983e-87 # expected result
    
    assert np.isclose(func_Gi(value3,1,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_2_largex_pos():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 2 when x is large and positive

    ----------    
    Given input values with x large and positive,
    when the G_i function integrand is computed, it returns the expected output:
    
    - input: value3 = large and positive -> output: positive and and closer to zero as i decreases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = 200 # input x value
    expected_output = 2.0963166322165967e-85 # expected result
    
    assert np.isclose(func_Gi(value3,2,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_3_largex_pos():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 3 when x is large and positive

    ----------    
    Given input values with x large and positive,
    when the G_i function integrand is computed, it returns the expected output:
        
    - input: value3 = large and positive -> output: positive and and closer to zero as i decreases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = 200 # input x value
    expected_output = 4.192633264433194e-83 # expected result
    
    assert np.isclose(func_Gi(value3,3,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_0_largex_neg():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 0 when x is large and negative

    ----------    
    Given input values with x large and negative,
    when the G_i function integrand is computed, it returns the expected output:
        
    - input: value3 = large and negative -> output: positive and closer to zero as i decreases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = -200 # input x value
    expected_output = 4.741965493160981e-90 # expected result
    
    assert np.isclose(func_Gi(value3,0,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_1_largex_neg():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 1 when x is large and negative

    ----------    
    Given input values with x large and negative,
    when the G_i function integrand is computed, it returns the expected output.
    
    - input: value3 = large and negative -> output: negative and closer to zero as i decreases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = -200 # input x value
    expected_output = -9.48393098632196e-88 # expected result
    
    assert np.isclose(func_Gi(value3,1,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_2_largex_neg():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 2 when x is large and negative

    ----------    
    Given input values with x large and negative,
    when the G_i function integrand is computed, it returns the expected output:
        
    - input: value3 = large and negative -> output: positive and closer to zero as i decreases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = -200 # input x value
    expected_output = 1.8967861972643923e-85 # expected result
    
    assert np.isclose(func_Gi(value3,2,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_3_largex_neg():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 3 when x is large and negative

    ----------    
    Given input values with x large and negative,
    when the G_i function integrand is computed, it returns the expected output:
        
    - input: value3 = large and negative -> output: negative and closer to zero as i decreases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = -200 # input x value
    expected_output = -3.793572394528785e-83 # expected result
    
    assert np.isclose(func_Gi(value3,3,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_0_smallx_pos():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 0 when x is small and positive

    ----------    
    Given input values with x small and positive,
    when the G_i function integrand is computed, it returns the expected output:
        
    - input: value3 = small and positive -> output: positive and closer to zero as i increases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = 0.003 # input x value
    expected_output = 1.441726312558458 # expected result
    
    assert np.isclose(func_Gi(value3,0,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_1_smallx_pos():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 1 when x is small and positive

    ----------    
    Given input values with x small and positive,
    when the G_i function integrand is computed, it returns the expected output.
    
    - input: value3 = small and positive -> output: negative and closer to zero as i increases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = 0.003 # input x value
    expected_output = 0.004325178937675374 # expected result
    
    assert np.isclose(func_Gi(value3,1,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_2_smallx_pos():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 2 when x is small and positive

    ----------    
    Given input values with x small and positive,
    when the G_i function integrand is computed, it returns the expected output:
        
    - input: value3 = small and positive -> output: positive and closer to zero as i increases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = 0.003 # input x value
    expected_output = 1.2975536813026123e-05 # expected result
    
    assert np.isclose(func_Gi(value3,2,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_3_smallx_pos():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 3 when x is small and positive

    ----------    
    Given input values with x small and positive,
    when the G_i function integrand is computed, it returns the expected output:
        
    - input: value3 = small and positive -> output: negative and closer to zero as i increases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = 0.003 # input x value
    expected_output = 3.8926610439078365e-08 # expected result
    
    assert np.isclose(func_Gi(value3,3,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_0_smallx_neg():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 0 when x is small and negative

    ----------    
    Given input values with x small and negative,
    when the G_i function integrand is computed, it returns the expected output:
        
    - input: value3 = small and negative -> output: positive and closer to zero as i increases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = -0.003 # input x value
    expected_output = 1.43827031784613 # expected result
    
    assert np.isclose(func_Gi(value3,0,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_1_smallx_neg():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 1 when x is small and negative

    ----------    
    Given input values with x small and negative,
    when the G_i function integrand is computed, it returns the expected output.
    
    - input: value3 = small and negative -> output: negative and closer to zero as i increases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = -0.003 # input x value
    expected_output = -0.00431481095353839 # expected result
    
    assert np.isclose(func_Gi(value3,1,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_2_smallx_neg():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 2 when x is small and negative

    ----------    
    Given input values with x small and positive,
    when the G_i function integrand is computed, it returns the expected output:
        
    - input: value3 = small and negative -> output: positive and closer to zero as i increases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = -0.003 # input x value
    expected_output = 1.2944432860615173e-05 # expected result
    
    assert np.isclose(func_Gi(value3,2,value1,value2), expected_output, atol=1e-10)
    
def test_func_Gi_3_smallx_neg():
            
    """
    function to test the function to calculate the G_i function integrand
    when i = 3 when x is small and negative

    ----------    
    Given input values with x small and negative,
    when the G_i function integrand is computed, it returns the expected output
        
    - input: value3 = small and negative -> output: positive and closer to zero as i increases
    ----------

    """
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    value3 = -0.003 # input x value
    expected_output = -3.883329858184551e-08 # expected result
    
    assert np.isclose(func_Gi(value3,3,value1,value2), expected_output, atol=1e-10)
    
def test_Gic_0_neg():
    
    """
    function to test the function to calculate the G_i function for the conduction band
    when i = 0 and (value2 - value1) < 0

    ----------    
    Given input values such that i = 0 and (value2 - value1) < 0
    when the G_ic function is applied, it returns the expected output:
        
    - inputs: i = 0, (value2 - value1) < 0 -> output: positive 
    ----------

    """
    
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    expected_output = 3.581198434041771e-08 # expected result
    
    assert np.isclose(float(Gic(func_Gi, 0, value1, value2)), expected_output, atol=1e-10)

def test_Gic_1_neg():
    
    """
    function to test the function to calculate the G_i function for the conduction band
    when i = 1 and (value2 - value1) < 0

    ----------    
    Given input values such that i = 1 and (value2 - value1) < 0
    when the G_ic function is applied, it returns the expected output:
        
    - inputs: i = 1, (value2 - value1) < 0 -> output: positive 
    ----------

    """
    
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    expected_output = 6.400404422663984e-07 # expected result
    
    assert np.isclose(float(Gic(func_Gi, 1, value1, value2)), expected_output, atol=1e-10)

def test_Gic_2_neg():
    
    """
    function to test the function to calculate the G_i function for the conduction band
    when i = 2 and (value2 - value1) < 0

    ----------    
    Given input values such that i = 2 and (value2 - value1) < 0
    when the G_ic function is applied, it returns the expected output:
        
    - inputs: i = 2, (value2 - value1) < 0 -> output: positive 
    ----------

    """
    
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    expected_output = 1.1466614882245465e-05 # expected result
    
    assert np.isclose(float(Gic(func_Gi, 2, value1, value2)), expected_output, atol=1e-10)

def test_Gic_3_neg():
    
    """
    function to test the function to calculate the G_i function for the conduction band
    when i = 3 and (value2 - value1) < 0

    ----------    
    Given input values such that i = 3 and (value2 - value1) < 0
    when the G_ic function is applied, it returns the expected output:
        
    - inputs: i = 3, (value2 - value1) < 0 -> output: positive 
    ----------

    """
    
    value1 = 12 # input energy gap value
    value2 = -5 # input chemical potential value
    expected_output = 0.0002059723191182534 # expected result
    
    assert np.isclose(float(Gic(func_Gi, 3, value1, value2)), expected_output, atol=1e-10)

def test_Gic_0_pos():
    
    """
    function to test the function to calculate the G_i function for the conduction band
    when i = 0 and (value2 - value1) > 0

    ----------    
    Given input values such that i = 0 and (value2 - value1) > 0
    when the G_ic function is applied, it returns the expected output:
        
    - inputs: i = 0, (value2 - value1) > 0 -> output: positive 
    ----------

    """
    
    value1 = 4.5 # input energy gap value
    value2 = 19 # input chemical potential value
    expected_output = 0.05774031961490533 # expected result
    
    assert np.isclose(float(Gic(func_Gi, 0, value1, value2)), expected_output, atol=1e-10)

def test_Gic_1_pos():
    
    """
    function to test the function to calculate the G_i function for the conduction band
    when i = 1 and (value2 - value1) > 0

    ----------    
    Given input values such that i = 1 and (value2 - value1) > 0
    when the G_ic function is applied, it returns the expected output:
        
    - inputs: i = 1, (value2 - value1) > 0 -> output: negative 
    ----------

    """
    
    value1 = 4.5 # input energy gap value
    value2 = 19 # input chemical potential value
    expected_output = -0.021155868450199625 # expected result
    
    assert np.isclose(float(Gic(func_Gi, 1, value1, value2)), expected_output, atol=1e-10)

def test_Gic_2_pos():
    
    """
    function to test the function to calculate the G_i function for the conduction band
    when i = 2 and (value2 - value1) > 0

    ----------    
    Given input values such that i = 2 and (value2 - value1) > 0
    when the G_ic function is applied, it returns the expected output:
        
    - inputs: i = 2, (value2 - value1) > 0 -> output: positive
    ----------

    """
    
    value1 = 4.5 # input energy gap value
    value2 = 19 # input chemical potential value
    expected_output = 0.2096574070917556 # expected result
    
    assert np.isclose(float(Gic(func_Gi, 2, value1, value2)), expected_output, atol=1e-10)

def test_Gic_3_pos():
    
    """
    function to test the function to calculate the G_i function for the conduction band
    when i = 3 and (value2 - value1) > 0

    ----------    
    Given input values such that i = 3 and (value2 - value1) > 0
    when the G_ic function is applied, it returns the expected output:
        
    - inputs: i = 0, (value2 - value1) > 0 -> output: negative
    ----------

    """
    
    value1 = 4.5 # input energy gap value
    value2 = 19 # input chemical potential value
    expected_output = -0.32955465691931424 # expected result
    
    assert np.isclose(float(Gic(func_Gi, 3, value1, value2)), expected_output, atol=1e-10)

def test_Giv_0_pos(): 

    """
    function to test the function to calculate the G_i function for the valence band
    when i = 0 and (value2 + value1) > 0

    ----------    
    Given input values such that i = 0 and (value2 + value1) > 0
    when the G_iv function is applied, it returns the expected output:
        
    - inputs: i = 0, (value2 + value1) > 0 -> output: positive
    ----------

    """
    value1 = 17 # input energy gap value
    value2 = -9 # input chemical potential value
    expected_output = 0.0003015760070507426 # expected result
    
    assert np.isclose(float(Giv(func_Gi, 0, value1, value2)), expected_output, atol=1e-10)

def test_Giv_1_pos(): 

    """
    function to test the function to calculate the G_i function for the valence band
    when i = 1 and (value2 + value1) > 0

    ----------    
    Given input values such that i = 1 and (value2 + value1) > 0
    when the G_iv function is applied, it returns the expected output:
        
    - inputs: i = 1, (value2 + value1) > 0 -> output: negative
    ----------

    """
    value1 = 17 # input energy gap value
    value2 = -9 # input chemical potential value
    expected_output = -0.002685138951920471 # expected result
    
    assert np.isclose(float(Giv(func_Gi, 1, value1, value2)), expected_output, atol=1e-10)

def test_Giv_2_pos(): 

    """
    function to test the function to calculate the G_i function for the valence band
    when i = 2 and (value2 + value1) > 0

    ----------    
    Given input values such that i = 2 and (value2 + value1) > 0 
    when the G_iv function is applied, it returns the expected output:
        
    - inputs: i = 2, (value2 + value1) > 0 -> output: positive
    ----------

    """
    value1 = 17 # input energy gap value
    value2 = -9 # input chemical potential value
    expected_output = 0.02415602999913352 # expected result
    
    assert np.isclose(float(Giv(func_Gi, 2, value1, value2)), expected_output, atol=1e-10)

def test_Giv_3_pos(): 

    """
    function to test the function to calculate the G_i function for the valence band
    when i = 3 and (value2 + value1) > 0

    ----------    
    Given input values such that i = 3 and (value2 + value1) > 0 
    when the G_iv function is applied, it returns the expected output:
        
    - inputs: i = 3, (value2 + value1) > 0 -> output: negative
    ----------

    """
    value1 = 17 # input energy gap value
    value2 = -9 # input chemical potential value
    expected_output = -0.21995714831541316 # expected result
    
    assert np.isclose(float(Giv(func_Gi, 3, value1, value2)), expected_output, atol=1e-10)

def test_Giv_0_neg(): 

    """
    function to test the function to calculate the G_i function for the valence band
    when i = 0 and (value2 + value1) < 0

    ----------    
    Given input values such that i = 0 and (value2 + value1) < 0
    when the G_iv function is applied, it returns the expected output:
        
    - inputs: i = 0, (value2 + value1) < 0 -> output: positive
    ----------

    """
    value1 = 6 # input energy gap value
    value2 = -13.5 # input chemical potential value
    expected_output = 0.20920887511574163 # expected result
    
    assert np.isclose(float(Giv(func_Gi, 0, value1, value2)), expected_output, atol=1e-10)

def test_Giv_1_neg(): 

    """
    function to test the function to calculate the G_i function for the valence band
    when i = 1 and (value2 + value1) < 0

    ----------    
    Given input values such that i = 1 and (value2 + value1) < 0
    when the G_iv function is applied, it returns the expected output:
        
    - inputs: i = 1, (value2 + value1) < 0 -> output: positive
    ----------

    """
    value1 = 6 # input energy gap value
    value2 = -13.5 # input chemical potential value
    expected_output = 0.1091344724450294 # expected result
    
    assert np.isclose(float(Giv(func_Gi, 1, value1, value2)), expected_output, atol=1e-10)

def test_Giv_2_neg(): 

    """
    function to test the function to calculate the G_i function for the valence band
    when i = 2 and (value2 + value1) < 0

    ----------    
    Given input values such that i = 2 and (value2 + value1) < 0
    when the G_iv function is applied, it returns the expected output:
    
    - inputs: i = 2, (value2 + value1) < 0 -> output: positive
    ----------

    """
    value1 = 6 # input energy gap value
    value2 = -13.5 # input chemical potential value
    expected_output = 0.7984132352426201 # expected result
    
    assert np.isclose(float(Giv(func_Gi, 2, value1, value2)), expected_output, atol=1e-10)

def test_Giv_3_neg(): 

    """
    function to test the function to calculate the G_i function for the valence band
    when i = 3 and (value2 + value1) < 0

    ----------    
    Given input values such that i = 3 and (value2 + value1) < 0
    when the G_iv function is applied, it returns the expected output:
        
    - inputs: i = 3, (value2 + value1) < 0 -> output: positive
    ----------

    """
    value1 = 6 # input energy gap value
    value2 = -13.5 # input chemical potential value
    expected_output = 1.498243983361794 # expected result
    
    assert np.isclose(float(Giv(func_Gi, 3, value1, value2)), expected_output, atol=1e-10)
