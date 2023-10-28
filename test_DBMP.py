# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:22:02 2023

@author: viola
"""

# import necessary modules 
import functions
from functions import *
import numpy as np
from mpmath import *

from DBM_Parabolic import *

# testing of specific functions of DBM_Parabolic model

# sigma calculation
def test_sigmac_DBMP_fixed_delta(): 
    
    """
    function to test the the function to calculate sigma for the conduction band
    
    ----------    
    Given an array of fixed input values for the energy gap (positive values in a realistic range),
    and an array of increasing input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - sigmac positive and increases for increasing chemical potential
    ----------

    """
    
    value1 = np.asarray([1, 1, 1])
    value2 = np.asarray([-13, -2, 7])
    expected_output = np.asarray([1.66305675e-06, 9.71747031e-02, 1.20049514e+01]) # expected results
    
    assert np.allclose(sigmac_DBMP(value1, value2), expected_output)

def test_sigmac_DBMP_fixed_eta(): 
    
    """
    function to test the the function to calculate sigma for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (positive values in a realistic range),
    and an array of input values for the chemical potential (positive and negative values in a realistic range)
    when the F0c function is applied, it gives an array containing the expected results:
    
    - sigmac positive and decreases for increasing values of energy gap
    ----------

    """
    
    value1 = np.asarray([2, 7.6, 19])
    value2 = np.asarray([3, 3, 3])
    expected_output = np.asarray([2.62652338e+00, 2.00033041e-02, 2.25070338e-07]) # expected results
    
    assert np.allclose(sigmac_DBMP(value1, value2), expected_output)

def test_sigmav_DBMP_fixed_delta(): 
    
    """
    function to test the the function to calculate sigma for the valence band
    
    ----------    
    Given an array of fixed input values for the energy gap (positive values in a realistic range),
    and an array of increasing input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - sigmav positive and decreases for increasing chemical potential
    ----------

    """
    
    value1 = np.asarray([1, 1, 1])
    value2 = np.asarray([-13, -2, 7])
    expected_output = np.asarray([2.40000123e+01, 2.62652338e+00, 6.70812746e-04]) # expected results
    
    assert np.allclose(sigmav_DBMP(value1, value2), expected_output)

def test_sigmav_DBMP_fixed_eta(): 
    
    """
    function to test the the function to calculate sigma for the valence band
    
    ----------    
    Given an array of input values for the energy gap (positive values in a realistic range),
    and an array of input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - sigmav positive and decreases for increasing values of energy gap
    ----------

    """
    
    value1 = np.asarray([2, 7.6, 19])
    value2 = np.asarray([3, 3, 3])
    expected_output = np.asarray([1.34306970e-02, 4.98313987e-05, 5.57893731e-10]) # expected results
    
    assert np.allclose(sigmav_DBMP(value1, value2), expected_output)

def test_sigma_DBMP_fixed_delta(): 
    
    """
    function to test the the function to calculate sigma for the conduction band
    
    ----------    
    Given an array of fixed input values for the energy gap (positive values in a realistic range),
    and an array of increasing input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - sigma has a quasi-parabolic behavior: decreases for increasing chemical potential when it is negative,
    then increases for increasing chemical potential when it is positive
    ----------

    """
    
    value1 = np.asarray([1, 1, 1])
    value2 = np.asarray([-13, -2, 7])
    expected_output = np.asarray([24.00001395, 2.72369808, 12.00562218]) # expected results
    
    assert np.allclose(sigma_DBMP(value1, value2), expected_output)

def test_sigma_DBMP_fixed_eta(): 
    
    """
    function to test the the function to calculate sigma for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (positive values in a realistic range),
    and an array of input values for the chemical potential (positive and negative values in a realistic range)
    when the F0c function is applied, it gives an array containing the expected results:
    
    - sigma positive and decreases for increasing values of energy gap
    ----------

    """
    
    value1 = np.asarray([2, 7.6, 19])
    value2 = np.asarray([3, 3, 3])
    #print(sigma_DBMP(value1, value2))
    expected_output = np.asarray([2.63995407e+00, 2.00531355e-02, 2.25628232e-07]) # expected results
    
    assert np.allclose(sigma_DBMP(value1, value2), expected_output)

# S calculation
def test_Sc_DBMP_fixed_delta(): 
    
    """
    function to test the the function to calculate S for the conduction band
    
    ----------    
    Given an array of fixed input values for the energy gap (positive values in a realistic range),
    and an array of increasing input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - Sc negative and increases for increasing values of chemical potential
    ----------

    """
    
    value1 = np.asarray([1, 1, 1])
    value2 = np.asarray([-13, -2, 7])
    expected_output = np.asarray([-16.000000390970271, -5.0244248243982694, -0.5447851451260235]) # expected results
    
    assert np.allclose(Sc_DBMP(value1, value2).astype(float), expected_output)

def test_Sc_DBMP_fixed_eta(): 
    
    """
    function to test the the function to calculate S for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (positive values in a realistic range),
    and an array of input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - Sc negative and decreases for increasing values of energy gap
    ----------

    """
    
    value1 = np.asarray([2, 7.6, 19])
    value2 = np.asarray([3, 3, 3])
    expected_output = np.asarray([-1.7508395129660097, -6.6050063834138895, -18.000000320536959]) # expected results
    
    assert np.allclose(Sc_DBMP(value1, value2).astype(float), expected_output)

def test_Sv_DBMP_fixed_delta(): 
    
    """
    function to test the the function to calculate S for the conduction band
    
    ----------    
    Given an array of fixed input values for the energy gap (positive values in a realistic range),
    and an array of increasing input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - Sv positive and increases for increasing values of chemical potential
    ----------

    """
    
    value1 = np.asarray([1, 1, 1])
    value2 = np.asarray([-13, -2, 7])
    expected_output = np.asarray([0.27414836921235658, 1.7508395129660099, 10.000167709436949]) # expected results
    
    assert np.allclose(Sv_DBMP(value1, value2).astype(float), expected_output)

def test_Sv_DBMP_fixed_eta(): 
    
    """
    function to test the the function to calculate S for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (positive values in a realistic range),
    and an array of input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - Sv positive and increases for increasing values of energy gap
    ----------

    """
    
    value1 = np.asarray([2, 7.6, 19])
    value2 = np.asarray([3, 3, 3])
    expected_output = np.asarray([7.003360179571537, 12.600012457890539, 23.999999596340341]) # expected results
    
    assert np.allclose(Sv_DBMP(value1, value2).astype(float), expected_output)

def test_S_DBMP_fixed_delta(): 
    
    """
    function to test the the function to calculate S for the conduction band
    
    ----------    
    Given an array of fixed input values for the energy gap (positive values in a realistic range),
    and an array of increasing input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - S positive and increases for increasing chemical potential when it is negative,
    decreases for increasing values in a narrow range near to zero becoming negative for positive chemical potential values,
    then increases again for positive values
    ----------

    """
    
    value1 = np.asarray([1, 1, 1, 1])
    value2 = np.asarray([-13, -2, 0.2, 7])
    expected_output = np.asarray([0.27414724151163972, 1.5091151067248834, -0.36665404456475648, -0.54419594710939645]) # expected results
    
    assert np.allclose(S_DBMP(value1, value2).astype(float), expected_output)

def test_S_DBMP_fixed_eta(): 
    
    """
    function to test the the function to calculate S for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (positive values in a realistic range),
    and an array of input values for the chemical potential (positive and negative values in a realistic range)
    when the F0c function is applied, it gives an array containing the expected results:
    
    - S negative and decreases for increasing values of energy gap
    ----------

    """
    
    value1 = np.asarray([2, 7.6, 19])
    value2 = np.asarray([3, 3, 3])
    expected_output = np.asarray([-1.7063027520413352, -6.5572825274719584, -17.896150122093459]) # expected results
    
    assert np.allclose(S_DBMP(value1, value2).astype(float), expected_output)
test_S_DBMP_fixed_delta()
test_S_DBMP_fixed_eta()

# ke calculation
def test_kec_DBMP_fixed_delta(): 
    
    """
    function to test the the function to calculate S for the conduction band
    
    ----------    
    Given an array of fixed input values for the energy gap (positive values in a realistic range),
    and an array of increasing input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - kec positive and increases for increasing values of chemical potential
    ----------

    """
    
    value1 = np.asarray([1, 1, 1])
    value2 = np.asarray([-13, -2, 7])
    expected_output = np.asarray([3.3261141529321715e-6, 0.19552973291472187, 36.242349432268476]) # expected results
    
    assert np.allclose(kec_DBMP(value1, value2).astype(float), expected_output)


def test_kec_DBMP_fixed_eta(): 
    
    """
    function to test the the function to calculate S for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (positive values in a realistic range),
    and an array of input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - kec positive and decreases for increasing values of energy gap
    ----------

    """
    
    value1 = np.asarray([2, 7.6, 19])
    value2 = np.asarray([3, 3, 3])
    expected_output = np.asarray([6.0947749765540493, 0.040056624675003705, 4.501399163888022e-7]) # expected results
    
    assert np.allclose(kec_DBMP(value1, value2).astype(float), expected_output)

def test_kev_DBMP_fixed_delta(): 
    
    """
    function to test the the function to calculate S for the conduction band
    
    ----------    
    Given an array of fixed input values for the energy gap (positive values in a realistic range),
    and an array of increasing input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - kev positive and decreases for increasing values of chemical potential
    ----------

    """
    
    value1 = np.asarray([1, 1, 1])
    value2 = np.asarray([-13, -2, 7])
    expected_output = np.asarray([77.15549150664225, 6.0947749765540475, 0.0013416817402995967]) # expected results
    
    assert np.allclose(kev_DBMP(value1, value2).astype(float), expected_output)

def test_kev_DBMP_fixed_eta(): 
    
    """
    function to test the the function to calculate S for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (which comprehends null and positive values in a realistic range),
    and an array of input values for the chemical potential (which comprehends null, positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - kev positive and decreases for increasing values of energy gap
    ----------

    """
    
    value1 = np.asarray([2, 7.6, 19])
    value2 = np.asarray([3, 3, 3])
    expected_output = np.asarray([0.02688394189501131, 9.9663107726927908e-5, 1.1157876875834053e-9]) # expected results
    
    assert np.allclose(kev_DBMP(value1, value2).astype(float), expected_output)

def test_ke_DBMP_fixed_delta(): 
    
    """
    function to test the the function to calculate ke of the material
    
    ----------    
    Given an array of fixed input values for the energy gap (positive values in a realistic range),
    and an array of increasing input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - ke is always positive and it decreases for increasing chemical potential when it is negative,
    reaches a local maximum in a narrow range near zero,
    then increases for positive values
    ----------

    """
    
    value1 = np.asarray([1, 1, 1, 1, 1, 1, 1])
    value2 = np.asarray([-13, -2, -0.2, 0, 0.2, 5, 17])
    expected_output = np.asarray([77.155935289843256, 10.591884828306991, 14.978132624202384, 15.132971795675514, 14.978132624202384, 23.059044241733691, 103.92296378132363]) # expected results
    
    assert np.allclose(ke_DBMP(value1, value2).astype(float), expected_output)

def test_ke_DBMP_fixed_eta(): 
    
    """
    function to test the the function to calculate S for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (positive values in a realistic range),
    and an array of input values for the chemical potential (positive and negative values in a realistic range)
    when the F0c function is applied, it gives an array containing the expected results:
    
    - S positive and decreases for increasing values of energy gap
    ----------

    """
    
    value1 = np.asarray([2, 7.6, 19])
    value2 = np.asarray([3, 3, 3])
    expected_output = np.asarray([7.1456975668755973, 0.058490067175707171, 1.4329468721701097e-6]) # expected results
    
    assert np.allclose(ke_DBMP(value1, value2).astype(float), expected_output)

# ZT calculation
def test_ZT_DBMP_fixed_delta(): 
    
    """
    function to test the the function to calculate ZT of the material
    
    ----------    
    Given an array of fixed input values for the energy gap (positive values in a realistic range),
    and an array of increasing input values for the chemical potential (positive and negative values in a realistic range)
    when the function is applied, it gives an array containing the expected results:
    
    - ZT is always positive and, for increasing values of the chemical potential:
    it is near to zero and increases until it reaches a local maximum,
    then decreases until eta = 0 where ZT is zero,
    then increases again until another local maximum,
    then decreases again towards zero
    ----------

    """
    
    value1 = np.asarray([1, 1, 1, 1, 1, 1, 1])
    value2 = np.asarray([-13, -2, -0.2, 0, 0.2, 5, 17])
    expected_output = np.asarray([0.023079016104636245, 0.53511809880070416, 0.010675016667360518, 2.195034301991368e-32, 0.010675016667360518, 0.20658824275862803, 0.01289424227108558]) # expected results
    
    assert np.allclose(ZT_DBMP(value1, value2, 1).astype(float), expected_output)

def test_ZT_DBMP_fixed_eta(): 
    
    """
    function to test the the function to calculate S for the conduction band
    
    ----------    
    Given an array of input values for the energy gap (positive values in a realistic range),
    and an array of input values for the chemical potential (positive and negative values in a realistic range)
    when the F0c function is applied, it gives an array containing the expected results:
    
    - S positive and decreases for increasing values of energy gap
    ----------

    """
    
    value1 = np.asarray([2, 7.6, 19])
    value2 = np.asarray([3, 3, 3])
    expected_output = np.asarray([0.94358335728462628, 0.81459791438907991, 7.2262344238493525e-5]) # expected results
    
    assert np.allclose(ZT_DBMP(value1, value2, 1).astype(float), expected_output)
    

