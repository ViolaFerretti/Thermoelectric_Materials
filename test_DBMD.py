# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:05:57 2023

@author: viola
"""

# import necessary modules 
import functions
from functions import *
import numpy as np
from mpmath import *

from DBM_Dirac import *

# testing of specific functions of DBM_Dirac model

# sigma calculations 
def test_sigmac_DBMD_fixed_delta_1():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band
    when the energy gap is fixed and the chemical potential is negative
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a negative input value for the chemical potential (in a realistic range),
    when the sigmac function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta < 0 (= -5) -> sigmac positive and of the order of e-5
    ----------

    """
    
    
    value1 = 4 # input value for energy gap
    value2 = -5 # input value for chemical potential
    expected_output = 3.720897644224199e-05 # expected result
    
    assert np.isclose(sigmac_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_sigmac_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band
    when the energy gap is fixed and the chemical potential is null
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a null input value for the chemical potential,
    when the sigmac function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta = 0 -> sigmac positive and of the order of e-3
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = 0 # input value for chemical potential
    expected_output = 0.0054611779073790705 # expected result
    
    assert np.isclose(sigmac_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_sigmac_DBMD_fixed_delta_3():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band
    when the energy gap is fixed and the chemical potential is positive
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a positive input value for the chemical potential (in a realistic range),
    when the sigmac function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta > 0 (= 5) -> sigmac positive and of the order of e-1
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = 5 # input value for chemical potential
    expected_output = 0.335321634963535 # expected result
    
    assert np.isclose(sigmac_DBMD(value1, value2), expected_output, atol=1e-10)

def test_sigmac_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band
    when the chemical potential is fixed and the energy gap is small
    ----------    
    Given a small input value for the energy gap
    and a fixed input value for the chemical potential (in a realistic range),
    when the sigmac function is applied, it gives the expected results:
    
    - inputs: delta small (= 0.5), eta fixed (= 2) -> sigmac positive and of the order of e-1
    ----------

    """
    
    value1 = 0.5 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 0.7333560692852861 # expected result
    
    assert np.isclose(sigmac_DBMD(value1, value2), expected_output, atol=1e-10)

def test_sigmac_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band
    when the chemical potential is fixed and the energy gap is intermediate
    ----------    
    Given an intermediate input value for the energy gap
    and a fixed input value for the chemical potential (in a realistic range),
    when the sigmac function is applied, it gives the expected results:
    
    - inputs: delta intermediate (= 7), eta fixed (= 2) -> sigmac positive and of the order of e-3
    ----------

    """
    
    value1 = 7 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 0.0013786998480445215 # expected result
    assert np.isclose(sigmac_DBMD(value1, value2), expected_output, atol=1e-10)

def test_sigmac_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band
    when the chemical potential is fixed and the energy gap is high
    ----------    
    Given an high input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the sigmac function is applied, it gives the expected results:
    
    - inputs: delta high (= 18), eta fixed (= 2) -> sigmac positive and of the order of e-8
    ----------

    """
    
    value1 = 18 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 1.0785594038432437e-08 # expected result
    
    assert np.isclose(sigmac_DBMD(value1, value2), expected_output, atol=1e-10)

def test_sigmav_DBMD_fixed_delta_1():
     
    """
    function to test the calculation of the electrical conductivity sigma for the valence band
    when the energy gap is fixed and the chemical potential is negative
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a negative input value for the chemical potential (in a realistic range),
    when the sigmav function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta < 0 (= -5) -> sigmav positive and of the order of e-1
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = -5 # input value for chemical potential
    expected_output = 0.33532163496353523 # expected result
    assert np.isclose(sigmav_DBMD(value1, value2), expected_output, atol=1e-10)

def test_sigmav_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the electrical conductivity sigma for the valence band
    when the energy gap is fixed and the chemical potential is null
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a null input value for the chemical potential (in a realistic range),
    when the sigmav function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta = 0 -> sigmav positive and of the order of e-3
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = 0 # input value for chemical potential
    expected_output = 0.005461177907379074 # expected result
    
    assert np.isclose(sigmav_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_sigmav_DBMD_fixed_delta_3():
     
    """
    function to test the calculation of the electrical conductivity sigma for the valence band
    when the energy gap is fixed and the chemical potential is positive
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a positive input value for the chemical potential (in a realistic range),
    when the sigmav function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta > 0 (= 5) -> sigmav positive and of the order of e-5
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = 5 # input value for chemical potential
    expected_output = 3.720897644224199e-05 # expected result
    
    assert np.isclose(sigmav_DBMD(value1, value2), expected_output, atol=1e-10)

def test_sigmav_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the electrical conductivity sigma for the valence band
    when the chemical potential is fixed and the energy gap is small
    ----------    
    Given a small input value for the energy gap
    and a fixed input value for the chemical potential (in a realistic range),
    when the sigmav function is applied, it gives the expected results:
    
    - inputs: delta small (= 0.5), eta fixed (= 2) -> sigmav positive and of the order of e-2
    ----------

    """
    
    value1 = 0.5 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 0.05622606843544534 # expected result
    
    assert np.isclose(sigmav_DBMD(value1, value2), expected_output, atol=1e-10)

def test_sigmav_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the electrical conductivity sigma for the valence band
    when the chemical potential is fixed and the energy gap is intermediate
    ----------    
    Given an intermediate input value for the energy gap
    and a fixed input value for the chemical potential (in a realistic range),
    when the sigmav function is applied, it gives the expected results:
    
    - inputs: delta intermediate (= 7), eta fixed (= 2) -> sigmav positive and of the order of e-5
    ----------

    """
    
    value1 = 7 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 2.5348256669159954e-05 # expected result
    
    assert np.isclose(sigmav_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_sigmav_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the electrical conductivity sigma for the valence band
    when the chemical potential is fixed and the energy gap is high
    ----------    
    Given an high input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the sigmav function is applied, it gives the expected results:
    
    - inputs: delta high (= 18), eta fixed (= 2) -> sigmav positive and of the order of e-10
    ----------

    """
    
    value1 = 18 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 1.733740683713239e-10 # expected result
    
    assert np.isclose(sigmav_DBMD(value1, value2), expected_output, atol=1e-10)

def test_sigma_DBMD_fixed_delta_1():
      
    """
    function to test the calculation of the electrical conductivity sigma of the material
    when the energy gap is fixed and the chemical potential is negative
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a negative input value for the chemical potential (in a realistic range),
    when the sigma function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta < 0 (= -5) -> sigma positive and of the order of e-1 (symmetry with respect to y-axis)
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = -5 # input value for chemical potential
    expected_output = 0.33535884393997745 # expected result
    
    assert np.isclose(sigma_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_sigma_DBMD_fixed_delta_2():
     
    """
    function to test the calculation of the electrical conductivity sigma of the material
    when the energy gap is fixed and the chemical potential is null
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a null input value for the chemical potential (in a realistic range),
    when the sigma function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta = 0 -> sigma positive and of the order of e-2 (symmetry with respect to y-axis)
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = 0 # input value for chemical potential
    expected_output = 0.010922355814758145 # expected result
    
    assert np.isclose(sigma_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_sigma_DBMD_fixed_delta_3():
     
    """
    function to test the calculation of the electrical conductivity sigma of the material
    when the energy gap is fixed and the chemical potential is positive
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a positive input value for the chemical potential (in a realistic range),
    when the sigma function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta > 0 (= 5) -> sigma positive and of the order of e-1 (symmetry with respect to y-axis)
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = 5 # input value for chemical potential
    expected_output = 0.3353588439399772 # expected result
    
    assert np.isclose(sigma_DBMD(value1, value2), expected_output, atol=1e-10)

def test_sigma_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the electrical conductivity sigma of the material
    when the chemical potential is fixed and the energy gap is small
    ----------    
    Given a small input value for the energy gap
    and a fixed input value for the chemical potential (in a realistic range),
    when the sigma function is applied, it gives the expected results:
    
    - inputs: delta small (= 0.5), eta fixed (= 2) -> sigma positive and of the order of e-1
    ----------

    """
    
    value1 = 0.5 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 0.7895821377207314 # expected result
    
    assert np.isclose(sigma_DBMD(value1, value2), expected_output, atol=1e-10)

def test_sigma_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the electrical conductivity sigma of the material
    when the chemical potential is fixed and the energy gap is intermediate
    ----------    
    Given an intermediate input value for the energy gap
    and a fixed input value for the chemical potential (in a realistic range),
    when the sigma function is applied, it gives the expected results:
    
    - inputs: delta intermediate (= 7), eta fixed (= 2) -> sigma positive and of the order of e-3
    ----------

    """
    
    value1 = 7 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 0.0014040481047136815 # expected result
    
    assert np.isclose(sigma_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_sigma_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the electrical conductivity sigma of the material
    when the chemical potential is fixed and the energy gap is high
    ----------    
    Given an high input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the sigma function is applied, it gives the expected results:
    
    - inputs: delta high (= 18), eta fixed (= 2) -> sigma positive and of the order of e-8
    ----------

    """
    
    value1 = 18 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 1.0958968106803761e-08 # expected result
    
    assert np.isclose(sigma_DBMD(value1, value2), expected_output, atol=1e-10)

# S calculations 
def test_Sc_DBMD_fixed_delta_1():
      
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band
    when the energy gap is fixed and the chemical potential is negative
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a negative input value for the chemical potential (in a realistic range),
    when the Sc function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta < 0 (= -5) -> Sc negative and near -11
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = -5 # input value for chemical potential
    expected_output = -10.632887749436646 # expected result
    
    assert np.isclose(Sc_DBMD(value1, value2), expected_output, atol=1e-10)

def test_Sc_DBMD_fixed_delta_2():
      
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band
    when the energy gap is fixed and the chemical potential is null
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a null input value for the chemical potential (in a realistic range),
    when the Sc function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta = 0 -> Sc negative and near -6
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = 0 # input value for chemical potential
    expected_output = -5.6412813745790835 # expected result
    
    assert np.isclose(Sc_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_Sc_DBMD_fixed_delta_3():
       
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band
    when the energy gap is fixed and the chemical potential is positive
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a positive input value for the chemical potential (in a realistic range),
    when the Sc function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta > 0 (= 5) -> Sc negative and near -1
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = 5 # input value for chemical potential
    expected_output = -1.3454897739003142 # expected result
    
    assert np.isclose(Sc_DBMD(value1, value2), expected_output, atol=1e-10)

def test_Sc_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the Seebeck coefficient S for the valence band
    when the chemical potential is fixed and the energy gap is small
    ----------    
    Given a small input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the Sc function is applied, it gives the expected results:
    
    - inputs: delta small (= 0.5), eta fixed (= 2) -> Sc negative and near -1
    ----------

    """
    
    value1 = 0.5 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = -0.7280120112460412 # expected result
    
    assert np.isclose(Sc_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_Sc_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the Seebeck coefficient S for the valence band
    when the chemical potential is fixed and the energy gap is intermediate
    ----------    
    Given an intermediate input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the Sc function is applied, it gives the expected results:
    
    - inputs: delta intermediate (= 7), eta fixed (= 2) -> Sc negative and near -7
    ----------

    """
    
    value1 = 7 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = -6.739623761989619 # expected result
    
    assert np.isclose(Sc_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_Sc_DBMD_fixed_eta_3():
     
    """
    function to test the calculation of the Seebeck coefficient S for the valence band
    when the chemical potential is fixed and the energy gap is high
    ----------    
    Given an high input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the Sc function is applied, it gives the expected results:
    
    - inputs: delta high (= 18), eta fixed (= 2) -> Sc negative and near -18
    ----------

    """
    
    value1 = 18 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = -17.867681126718878 # expected result
    
    assert np.isclose(Sc_DBMD(value1, value2), expected_output, atol=1e-10)

def test_Sv_DBMD_fixed_delta_1():
         
    """
    function to test the calculation of the Seebeck coefficient S for the valence band
    when the energy gap is fixed and the chemical potential is negative
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a negative input value for the chemical potential (in a realistic range),
    when the Sv function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta < 0 (= -5) -> Sv positive and near 1
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = -5 # input value for chemical potential
    expected_output = 1.345489773900313 # expected result
    
    assert np.isclose(Sv_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_Sv_DBMD_fixed_delta_2():
        
    """
    function to test the calculation of the Seebeck coefficient S for the valence band
    when the energy gap is fixed and the chemical potential is null
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a null input value for the chemical potential (in a realistic range),
    when the Sv function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta = 0 -> Sv positive and near 6
    ----------

    """
    
    value1 = 4 # input value for energy gap
    value2 = 0 # input value for chemical potential
    expected_output = 5.64128137457915 # expected result
    
    assert np.isclose(Sv_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_Sv_DBMD_fixed_delta_3():
         
    """
    function to test the calculation of the Seebeck coefficient S for the valence band
    when the energy gap is fixed and the chemical potential is positive
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a positive input value for the chemical potential (in a realistic range),
    when the Sv function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta > 0 (= 5) -> Sv positive and near 10
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = 5 # input value for chemical potential
    expected_output = 10.632887749430298 # expected result
    
    assert np.isclose(Sv_DBMD(value1, value2), expected_output, atol=1e-10)

def test_Sv_DBMD_fixed_eta_1():
     
    """
    function to test the calculation of the Seebeck coefficient S for the valence band
    when the chemical potential is fixed and the energy gap is small
    ----------    
    Given a small input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the Sv function is applied, it gives the expected results:
    
    - inputs: delta small (= 0.5), eta fixed (= 2) -> Sv positive and near 4
    ----------

    """
    
    value1 = 0.5 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 3.7735151059871415 # expected result
    
    assert np.isclose(Sv_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_Sv_DBMD_fixed_eta_2():
     
    """
    function to test the calculation of the Seebeck coefficient S for the valence band
    when the chemical potential is fixed and the energy gap is intermediate
    ----------    
    Given an intermediate input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the Sv function is applied, it gives the expected results:
    
    - inputs: delta intermediate (= 7), eta fixed (= 2) -> Sv positive and near 11
    ----------

    """
    
    value1 = 7 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 10.736506865669007 # expected result
    
    assert np.isclose(Sv_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_Sv_DBMD_fixed_eta_3():
     
    """
    function to test the calculation of the Seebeck coefficient S for the valence band
    when the chemical potential is fixed and the energy gap is high
    ----------    
    Given a high input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the Sv function is applied, it gives the expected results:
    
    - inputs: delta high (= 18), eta fixed (= 2) -> Sv positive and near 24
    ----------

    """
    
    value1 = 18 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 24.91636960481909 # expected result
    
    assert np.isclose(Sv_DBMD(value1, value2), expected_output, atol=1e-10)

def test_S_DBMD_fixed_delta_1():
          
    """
    function to test the calculation of the Seebeck coefficient S of the material
    when the energy gap is fixed and the chemical potential is negative
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a negative input value for the chemical potential (in a realistic range),
    when the S function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta < 0 (= -5) -> S positive and near 1
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = -5 # input value for chemical potential
    expected_output = 1.3441607403139442 # expected result
    
    assert np.isclose(S_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_S_DBMD_fixed_delta_2():
         
    """
    function to test the calculation of the Seebeck coefficient S of the material
    when the energy gap is fixed and the chemical potential is null
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a null input value for the chemical potential (in a realistic range),
    when the S function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta = 0 -> S positive and of the order of e-14
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = 0 # input value for chemical potential
    expected_output = 3.525874987028874e-14 # expected result
    
    assert np.isclose(S_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_S_DBMD_fixed_delta_3():
         
    """
    function to test the calculation of the Seebeck coefficient S of the material
    when the energy gap is fixed and the chemical potential is positive
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a positive input value for the chemical potential (in a realistic range),
    when the S function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta > 0 (= 5) -> S neagtive and near -1
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = 5 # input value for chemical potential
    expected_output = -1.344160740313946 # expected result
    
    assert np.isclose(S_DBMD(value1, value2), expected_output, atol=1e-10)

def test_S_DBMD_fixed_eta_1():
     
    """
    function to test the calculation of the Seebeck coefficient S of the material
    when the chemical potential is fixed and the energy gap is small
    ----------    
    Given a small input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the S function is applied, it gives the expected results:
    
    - inputs: delta small (= 0.5), eta fixed (= 2) -> S negative and of the order of e-1
    ----------

    """
    
    value1 = 0.5 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = -0.40745869618727737 # expected result
    
    assert np.isclose(S_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_S_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the Seebeck coefficient S of the material
    when the chemical potential is fixed and the energy gap is intermediate
    ----------    
    Given an intermediate input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the S function is applied, it gives the expected results:
    
    - inputs: delta intermediate (= 7), eta fixed (= 2) -> S negative and near -6
    ----------

    """
    
    value1 = 7  # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = -6.424115024613419 # expected result
    
    
    assert np.isclose(S_DBMD(value1, value2), expected_output, atol=1e-10)
    
def test_S_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the Seebeck coefficient S of the material
    when the chemical potential is fixed and the energy gap is high
    ----------    
    Given a high input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the S function is applied, it gives the expected results:
    
    - inputs: delta high (= 18), eta fixed (= 2) -> S negative and near -17
    ----------

    """
    
    value1 = 18 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = -17.190824978909973 # expected result
    
    assert np.isclose(S_DBMD(value1, value2), expected_output, atol=1e-10)

# # ke calculations 
def test_kec_DBMD_fixed_delta_1():
         
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band
    when the energy gap is fixed and the chemical potential is negative
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a negative input value for the chemical potential (in a realistic range),
    when the kec function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta < 0 (= -5) -> kec positive and of the order of e-5
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = -5 # input value for chemical potential
    expected_output = 5.34101064720736e-5 # expected result
    
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output, atol=1e-10)
    
def test_kec_DBMD_fixed_delta_2():
          
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band
    when the energy gap is fixed and the chemical potential is null
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a null input value for the chemical potential (in a realistic range),
    when the kec function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta = 0 -> kec positive and of the order of e-3
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = 0 # input value for chemical potential
    expected_output = 0.00786749220501892 # expected result
    
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output, atol=1e-10)
    
def test_kec_DBMD_fixed_delta_3():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band
    when the energy gap is fixed and the chemical potential is positive
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a positive input value for the chemical potential (in a realistic range),
    when the kec function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta > 0 (= 5) -> kec positive and of the order of e-1
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = 5 # input value for chemical potential    
    expected_output = 0.616859374209206 # expected result
    
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output, atol=1e-10)

def test_kec_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band
    when the chemical potential is fixed and the energy gap is small
    ----------    
    Given a small input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the kec function is applied, it gives the expected results:
    
    - inputs: delta small (= 0.5), eta fixed (= 2) -> kec positive and near 1
    ----------

    """
    
    value1 = 0.5 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 1.3600452591123982 # expected result
    
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output, atol=1e-10)
 
def test_kec_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band
    when the chemical potential is fixed and the energy gap is intermediate
    ----------    
    Given an intermediate input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the kec function is applied, it gives the expected results:
    
    - inputs: delta intermediate (= 7), eta fixed (= 2) -> kec positive and of the order of e-3
    ----------

    """
    
    value1 = 7 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 0.00216163510819416 # expected result
    
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output, atol=1e-10)
    
def test_kec_DBMD_fixed_eta_3():
     
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band
    when the chemical potential is fixed and the energy gap is high
    ----------    
    Given a high input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the kec function is applied, it gives the expected results:
    
    - inputs: delta high (= 18), eta fixed (= 2) -> kec positive and of the order of e-8
    ----------

    """
    
    value1 = 18 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 1.89955154020879e-8 # expected result
    
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output, atol=1e-10)

def test_kev_DBMD_fixed_delta_1():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the valence band
    when the energy gap is fixed and the chemical potential is negative
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a negative input value for the chemical potential (in a realistic range),
    when the kev function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta < 0 (= -5) -> kev and of the order of e-1
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = -5 # input value for chemical potential
    expected_output = 0.616859374209206 # expected result
    
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output, atol=1e-10)
    
def test_kev_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the valence band
    when the energy gap is fixed and the chemical potential is null
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a null input value for the chemical potential (in a realistic range),
    when the kev function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta = 0 -> kev positive and of the order of e-3
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = 0 # input value for chemical potential
    expected_output = 0.00786749220501531 # expected result
    
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output, atol=1e-10)
    
def test_kev_DBMD_fixed_delta_3():
   
    """
    function to test the calculation of the thermal electronic conductivity ke for the valence band
    when the energy gap is fixed and the chemical potential is positive
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and a positive input value for the chemical potential (in a realistic range),
    when the kev function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta > 0 (= 5) -> kev positive and of the order of e-5
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = 5 # input value for chemical potential
    expected_output = 5.34101064486054e-5 # expected result
    
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output, atol=1e-10)

def test_kev_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the valence band
    when the chemical potential is fixed and the energy gap is small
    ----------    
    Given a small input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the kev function is applied, it gives the expected results:
    
    - inputs: delta small (= 0.5), eta fixed (= 2) -> kev positive and of the order of e-2
    ----------

    """
    
    value1 = 0.5 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 0.0629572805725923 # expected result
    
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output, atol=1e-10)
    
def test_kev_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the valence band
    when the chemical potential is fixed and the energy gap is intermediate
    ----------    
    Given an intermediate input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the kev function is applied, it gives the expected results:
    
    - inputs: delta intermediate (= 7), eta fixed (= 2) -> kev positive and of the order of e-5
    ----------

    """
    
    value1 = 7 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 3.96976135383729e-5 # expected result
    
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output, atol=1e-10)
    
def test_kev_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the valence band
    when the chemical potential is fixed and the energy gap is high
    ----------    
    Given a high input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the kev function is applied, it gives the expected results:
    
    - inputs: delta high (= 18), eta fixed (= 2) -> kev negative and of the order of e-8
    ----------

    """
    
    value1 = 18 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = -1.28219689007053e-8 # expected result
    
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output, atol=1e-10)

def test_ke_DBMD_fixed_delta_1():
   
    """
    function to test the calculation of the thermal electronic conductivity ke of the material
    when the energy gap is fixed and the chemical potential is negative
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and negative input value for the chemical potential (in a realistic range),
    when the ke function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta < 0 (= -5) -> ke positive and near 0.6 (symmetry with respect to y-axis)
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = -5 # input value for chemical potential
    expected_output = 0.622250992759856 # expected result
    
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output, atol=1e-10)
    
def test_ke_DBMD_fixed_delta_2():
   
    """
    function to test the calculation of the thermal electronic conductivity ke of the material
    when the energy gap is fixed and the chemical potential is null
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and null input value for the chemical potential (in a realistic range),
    when the ke function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta = 0 -> ke positive and near 0.4 (symmetry with respect to y-axis)
    ----------
    
    """
    value1 = 4 # input value for energy gap
    value2 = 0 # input value for chemical potential
    expected_output = 0.363328642564888 # expected result
    
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output, atol=1e-10)
    
def test_ke_DBMD_fixed_delta_3():
   
    """
    function to test the calculation of the thermal electronic conductivity ke of the material
    when the energy gap is fixed and the chemical potential is positive
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and positive input value for the chemical potential (in a realistic range),
    when the ke function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta > 0 (= 5) -> ke positive and near 0.6 (symmetry with respect to y-axis)
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = 5 # input value for chemical potential
    expected_output = 0.622250992759827 # expected result
    
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output, atol=1e-10)

def test_ke_DBMD_fixed_eta_1():
     
    """
    function to test the calculation of the thermal electronic conductivity ke of the material
    when the chemical potential is fixed and the energy gap is small
    ----------    
    Given a small input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the ke function is applied, it gives the expected results:
    
    - inputs: delta small (= 0.5), eta fixed (= 2) -> ke positive and near 2
    ----------

    """
    
    value1 = 0.5 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 2.48122027005063 # expected result
    
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output, atol=1e-10)
    
def test_ke_DBMD_fixed_eta_2():
      
    """
    function to test the calculation of the thermal electronic conductivity ke of the material
    when the chemical potential is fixed and the energy gap is intermediate
    ----------    
    Given an intermediate input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the ke function is applied, it gives the expected results:
    
    - inputs: delta intermediate (= 7), eta fixed (= 2) -> ke positive and of the order of e-3
    ----------

    """
    
    value1 = 7 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 0.009803307084193 # expected result
    
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output, atol=1e-10)
    
def test_ke_DBMD_fixed_eta_3():
      
    """
    function to test the calculation of the thermal electronic conductivity ke of the material
    when the chemical potential is fixed and the energy gap is high
    ----------    
    Given a high input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the ke function is applied, it gives the expected results:
    
    - inputs: delta high (= 18), eta fixed (= 2) -> ke positive and of the order of e-7
    ----------

    """
    
    value1 = 18 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 3.18509765205363e-7 # expected result
    
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output, atol=1e-10)

# ZT calculation
def test_ZT_DBMD_fixed_delta_1():
   
    """
    function to test the calculation of the figure of merit ZT of the material
    when the energy gap is fixed and the chemical potential is negative
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and negative input value for the chemical potential (in a realistic range),
    when the ZT function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta < 0 (= -5) -> ZT positive and near 0.4 (symmetry with respect to y-axis)
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = -5 # input value for chemical potential
    expected_output = 0.373503029173528 # expected result
    
    assert np.isclose(float(ZT_DBMD(value1, value2, 1)), expected_output, atol=1e-10)
    
def test_ZT_DBMD_fixed_delta_2():
   
    """
    function to test the calculation of the figure of merit ZT of the material
    when the energy gap is fixed and the chemical potential is null
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and null input value for the chemical potential (in a realistic range),
    when the ZT function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta = 0 -> ZT positive and of the order of e-30 (symmetry with respect to y-axis)
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = 0 # input value for chemical potential
    expected_output = 9.95977623275776e-30 # expected result
    
    assert np.isclose(float(ZT_DBMD(value1, value2, 1)), expected_output, atol=1e-10)
    
def test_ZT_DBMD_fixed_delta_3():
   
    """
    function to test the calculation of the figure of merit ZT of the material
    when the energy gap is fixed and the chemical potential is positive
    
    ----------    
    Given a fixed input value for the energy gap (positive value in a realistic range)
    and positive input value for the chemical potential (in a realistic range),
    when the ZT function is applied, it gives the expected results:
    
    - inputs: delta fixed (= 4), eta > 0 (= 5) -> ZT positive and near 0.4 (symmetry with respect to y-axis)
    ----------
    
    """
    
    value1 = 4 # input value for energy gap
    value2 = 5 # input value for chemical potential
    expected_output = 0.373503029173535 # expected result
    
    assert np.isclose(float(ZT_DBMD(value1, value2, 1)), expected_output, atol=1e-10)

def test_ZT_DBMD_fixed_eta_1():
     
    """
    function to test the calculation of the figure of merit ZT of the material
    when the chemical potential is fixed and the energy gap is small
    ----------    
    Given a small input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the ZT function is applied, it gives the expected results:
    
    - inputs: delta small (= 0.5), eta fixed (= 2) -> ZT positive and of the order of e-2
    ----------

    """
    
    value1 = 0.5 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 0.0376558966803113 # expected result
    
    assert np.isclose(float(ZT_DBMD(value1, value2, 1)), expected_output, atol=1e-10)
    
def test_ZT_DBMD_fixed_eta_2():
      
    """
    function to test the calculation of the figure of merit ZT of the material
    when the chemical potential is fixed and the energy gap is intermediate
    ----------    
    Given an intermediate input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the ZT function is applied, it gives the expected results:
    
    - inputs: delta intermediate (= 7), eta fixed (= 2) -> ZT positive and of the order of e-2
    ----------

    """
    
    value1 = 7 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 0.057381489289831 # expected result
    
    assert np.isclose(float(ZT_DBMD(value1, value2, 1)), expected_output, atol=1e-10)
    
def test_ZT_DBMD_fixed_eta_3():
       
    """
    function to test the calculation of the figure of merit ZT of the material
    when the chemical potential is fixed and the energy gap is high
    ----------    
    Given an high input value for the energy gap (in a realistic range)
    and a fixed input value for the chemical potential (in a realistic range),
    when the ZT function is applied, it gives the expected results:
    
    - inputs: delta high (= 18), eta fixed (= 2) -> ZT positive and of the order of e-6
    ----------

    """
    
    value1 = 18 # input value for energy gap
    value2 = 2 # input value for chemical potential
    expected_output = 3.23864213825014e-6 # expected result
    
    assert np.isclose(float(ZT_DBMD(value1, value2, 1)), expected_output, atol=1e-10)
