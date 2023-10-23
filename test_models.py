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
from DBM_Dirac import *
from SBM_Parabolic import *

# testing of specific functions of DBM_Parabolic model
def test_sigmac_DBMP(): 
    
    """
    function to test the function to calculate the electrical conductivity sigma for the conduction band

    Returns
    -------
    None.

    """
    
    value1 = np.asarray([2, 3, 4, 9]) # example values for energy gap
    value2 = np.asarray([7, 2, 6, 8]) # example values for chemical potential
    
    expected_output = np.asarray([10.0134307, 0.62652338, 4.25385602, 0.62652338]) # expected results
    assert np.allclose(sigmac_DBMP(value1, value2), expected_output)

def test_sigmav_DBMP():
    
    """
    function to test the function to calculate the electrical conductivity sigma for the valence band

    Returns
    -------
    None.

    """
    
    value1 = np.asarray([2, 3, 4, 9]) # example values for energy gap
    value2 = np.asarray([7, 2, 6, 8]) # example values for chemical potential
    
    expected_output = np.asarray([2.46804379e-04, 1.34306970e-02, 9.07977984e-05, 8.27987528e-08]) # expected results
    assert np.allclose(sigmav_DBMP(value1, value2), expected_output)

def test_sigma_DBMP():
    
    """
    function to test the function to calculate the electrical conductivity sigma of the material

    Returns
    -------
    None.

    """
    
    value1 = np.asarray([2, 5, 0.5, 9]) # example values for energy gap
    value2 = np.asarray([7, 8, 6, 2]) # example values for chemical potential
    
    expected_output = np.asarray([1.00136775e+01, 6.09717922e+00, 1.10111615e+01, 1.85633603e-03]) # expected results
    assert np.allclose(sigma_DBMP(value1, value2), expected_output)

def test_Sc_DBMP():
    
    """
    function to test the function to calculate the Seebeck coefficient S for the conduction band

    Returns
    -------
    None.

    """
    
    value1 = np.asarray([2, 5, 0.5, 9]) # example values for energy gap
    value2 = np.asarray([7, 8, 6, 2]) # example values for chemical potential
   
    expected_output = np.asarray([-0.64769772271443649, -0.99906753097473289, -0.5921557118310008, -9.0004557793968374]) # expected results
    assert np.allclose(Sc_DBMP(value1, value2).astype(float), expected_output)

def test_Sv_DBMP():
    
    """
    function to test the function to calculate the Seebeck coefficient S for the valence band

    Returns
    -------
    None.

    """
    
    value1 = np.asarray([2, 5, 0.5, 9]) # example values for energy gap
    value2 = np.asarray([7, 8, 6, 2]) # example values for chemical potential
    
    expected_output = np.asarray([11.000061701939575, 15.000001130166538, 8.5007512804651828, 13.000008350806922]) # expected results
    assert np.allclose(Sv_DBMP(value1, value2).astype(float), expected_output)

def test_S_DBMP():
    
    """
    function to test the function to calculate the Seebeck coefficient S of the material

    Returns
    -------
    None.

    """
    
    value1 = np.asarray([2, 5, 0.5, 9]) # example values for energy gap
    value2 = np.asarray([7, 8, 6, 2]) # example values for chemical potential
    
    expected_output = np.asarray([-0.64741064356330968, -0.99905566872723073, -0.58967452643603291, -8.6045769140110089]) # expected results
    assert np.allclose(S_DBMP(value1, value2).astype(float), expected_output)

def test_kec_DBMP():
    
    """
    function to test the function to calculate the thermal electronic conductivity k_e for the conduction band

    Returns
    -------
    None.

    """
    
    value1 = np.asarray([2, 5, 0.5, 9]) # example values for energy gap
    value2 = np.asarray([7, 8, 6, 2]) # example values for chemical potential
    
    expected_output = np.asarray([29.383543652975188, 16.302089684568426, 32.803953624335598, 0.0036462812001165634]) # expected results
    assert np.allclose(kec_DBMP(value1, value2).astype(float), expected_output)

def test_kev_DBMP():
    
    """
    function to test the function to calculate the thermal electronic conductivity k_e for the valence band

    Returns
    -------
    None.

    """
    
    value1 = np.asarray([2, 5, 3.5, 9]) # example values for energy gap
    value2 = np.asarray([4, 9, 6, 2]) # example values for chemical potential
    
    expected_output = np.asarray([0.0099058050591114832, 3.3261138401355079e-6, 0.00029939891570513605, 6.6806384743914662e-5]) # expected results
    assert np.allclose(kev_DBMP(value1, value2).astype(float), expected_output)

def test_ke_DBMP():
    
    """
    function to test the function to calculate the thermal electronic conductivity k_e of the material

    Returns
    -------
    None.

    """
    
    value1 = np.asarray([2, 5, 3.5, 9]) # example values for energy gap
    value2 = np.asarray([4, 9, 6, 2]) # example values for chemical potential
    
    expected_output = np.asarray([11.071051221682763, 22.667035350654011, 13.378333192880682, 0.019589955973850104]) # expected results
    assert np.allclose(ke_DBMP(value1, value2).astype(float), expected_output)


def test_ZT_DBMP():
    
    """
    function to test the function to calculate the figure of merit ZT of the material

    Returns
    -------
    None.

    """
    
    value1 = np.asarray([2, 5, 3.5, 9]) # example values for energy gap
    value2 = np.asarray([4, 9, 6, 2]) # example values for chemical potential
    
    expected_output = np.asarray([0.59021616097800866, 0.21277958797786051, 0.46330560386124203, 0.13480006062089001])  # expected results
    assert np.allclose(ZT_DBMP(value1, value2, 1).astype(float), expected_output)

# testing of specific functions of DBM_Dirac model
def test_sigmac_DBMD():
    
    """
    function to test the function to calculate the electrical conductivity sigma for the conduction band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 2 # example value for energy gap
    value2 = 4 # example value for chemical potential
    
    expected_output = 0.6320015299793118 # expected result
    assert sigmac_DBMD(value1, value2).astype(float) == expected_output

    # test 2
    value1 = 1.5 # example value for energy gap
    value2 = 7 # example value for chemical potential
    
    expected_output = 0.9368293113655424 # expected result
    assert sigmac_DBMD(value1, value2).astype(float) == expected_output
    
def test_sigmav_DBMD():
    
    """
    function to test the function to calculate the electrical conductivity sigma for the valence band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 2 # example value for energy gap
    value2 = 4 # example value for chemical potential
    
    expected_output = 0.001101975029276735 # expected result
    assert sigmav_DBMD(value1, value2).astype(float) == expected_output
    
    # test 2
    value1 = 1.5 # example value for energy gap
    value2 = 7 # example value for chemical potential
    
    expected_output = 0.00010346458581792292 # expected result
    assert sigmav_DBMD(value1, value2).astype(float) == expected_output

def test_sigma_DBMD():
    
    """
    function to test the function to calculate the electrical conductivity sigma of the material

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 2 # example value for energy gap
    value2 = 4 # example value for chemical potential
    
    expected_output = 0.6331035050085886 # expected result
    assert sigma_DBMD(value1, value2).astype(float) == expected_output
    
    # test 2
    value1 = 1.5 # example value for energy gap
    value2 = 7 # example value for chemical potential
    
    expected_output = 0.9369327759513603 # expected result
    assert sigma_DBMD(value1, value2).astype(float) == expected_output

def test_Sc_DBMD():
    
    """
    function to test the function to calculate the Seebeck coefficient S for the conduction band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 2 # example value for energy gap
    value2 = 4 # example value for chemical potential
    
    expected_output = -0.7473427239793451 # expected result
    assert Sc_DBMD(value1, value2).astype(float) == expected_output
    
    # test 2
    value1 = 1.5 # example value for energy gap
    value2 = 7 # example value for chemical potential
    
    expected_output = -0.10200337819379099 # expected result
    
def test_Sv_DBMD():
    
    """
    function to test the function to calculate the Seebeck coefficient S for the valence band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 2 # example value for energy gap
    value2 = 4 # example value for chemical potential
    
    expected_output = 7.492339787057502 # expected result
    assert Sv_DBMD(value1, value2).astype(float) == expected_output
    
    # test 2
    value1 = 1.5 # example value for energy gap
    value2 = 7 # example value for chemical potential
    
    expected_output = 9.932629860956144 # expected result
    assert Sv_DBMD(value1, value2).astype(float) == expected_output

def test_S_DBMD():
    
    """
    function to test the function to calculate the Seebeck coefficient S of the material

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 2 # example value for energy gap
    value2 = 4 # example value for chemical potential
    
    expected_output = -0.7330007967833999 # expected result
    assert S_DBMD(value1, value2).astype(float) == expected_output
    
    # test 2
    value1 = 1.5 # example value for energy gap
    value2 = 7 # example value for chemical potential
    
    expected_output = -0.10089526329102308 # expected result
    assert S_DBMD(value1, value2).astype(float) == expected_output

def test_kec_DBMD():
    
    """
    function to test the function to calculate the thermal electronic conductivity k_e for the conduction band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 2 # example value for energy gap
    value2 = 4 # example value for chemical potential
    
    expected_output = 1.29197054949625 # expected result
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output)
    
    # test 2
    value1 = 1.5 # example value for energy gap
    value2 = 7 # example value for chemical potential
    
    expected_output = 2.79171801794985 # expected result
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output)

def test_kev_DBMD():
    
    """
    function to test the function to calculate the thermal electronic conductivity k_e for the valence band

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 2 # example value for energy gap
    value2 = 4 # example value for chemical potential
    
    expected_output = 0.00141700695019598 # expected result
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output)
    
    # test 2
    value1 = 1.5 # example value for energy gap
    value2 = 7 # example value for chemical potential
   
    expected_output = 0.000127430727024787 # expected result
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output)

def test_ke_DBMD():
    
    """
    function to test the function to calculate the thermal electronic conductivity k_e of the material

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 2 # example value for energy gap
    value2 = 4 # example value for chemical potential
    
    expected_output = 1.36807302691728 # expected result
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output)
    
    # test 2
    value1 = 1.5 # example value for energy gap
    value2 = 7 # example value for chemical potential
    
    expected_output = 2.8022625471581 # expected result
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output)

def test_ZT_DBMD():
    
    """
    function to test the function to calculate the figure of merit ZT of the material

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 2 # example value for energy gap
    value2 = 4 # example value for chemical potential
    value3 = 1 # example value for thermal lattice conductivity
    expected_output = 0.143644340674808 # expected result
    assert np.isclose(float(ZT_DBMD(value1, value2,1)), expected_output)
    
    # test 2
    value1 = 1.5 # example value for energy gap
    value2 = 7 # example value for chemical potential
    
    expected_output = 0.00250846407724928 # expected result
    assert np.isclose(float(ZT_DBMD(value1, value2, value3)), expected_output)

# testing of specific functions of SBM_Parabolic model
def test_func_Fi():
    
    """
    function to test the function to calculate the F_i function

    Returns
    -------
    None.

    """
    
    value1=-4 # example value for chemical potential
    value2=20 # example value for x
    
    # test 1: i = 0
    i = 0
    
    expected_output = 3.7751345441365816e-11 # expected result
    assert func_Fi(value2, i, value1) == expected_output
    
    # test 2: i = 1
    i = 1
    
    expected_output = 7.550269088273163e-10 # expected result
    assert func_Fi(value2, i, value1) == expected_output
    
    # test 3: i = 2
    i = 2
    
    expected_output = 1.5100538176546325e-08 # expected result
    assert func_Fi(value2, i, value1) == expected_output
  

def test_Fic():
    
    """
    function to test the function to calculate the F_i integral for the conduction band

    Returns
    -------
    None.

    """
    
    value1 = -8.5 # example value for chemical potential
    
    # test 1: i = 0
    i = 0
    
    expected_output = 0.000101723836064718 # expected result
    assert Fic(i, value1) == expected_output
    
    # test 2: i = 1
    i = 1
    
    expected_output = 0.00010172901005109025 # expected result
    assert Fic(i, value1) == expected_output
    
    # test 3: i = 2
    i = 2
    
    expected_output = 0.00020346319440044903 # expected result
    assert Fic(i, value1) == expected_output


def test_sigma_SBMP():
    
    """
    function to test the function to calculate the electric conductivity sigma of the material

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 6.7 # example value for chemical potential
    
    expected_output = 3.350615077475857 # expected result
    assert sigma_SBMP(value1) == expected_output
    
    # test 2
    value1 = -2 # example value for chemical potential
    
    expected_output = 0.06346400552148626 # expected result
    assert sigma_SBMP(value1) == expected_output

 
def test_S_SBMP():
    
    """
    function to test the function to calculate the Seebeck coefficient S of the material

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 6.7 # example value for chemical potential
    
    expected_output = 0.4893377712821068 # expected result
    assert S_SBMP(value1) == expected_output
    
    # test 2
    value1 = -2 # example value for chemical potential
    
    expected_output = 4.0643589013628905 # expected result
    assert S_SBMP(value1) == expected_output

def test_ke_SBMP():
    
    """
    function to test the function to calculate the thermal electronic conductivity k_e of the material

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 6.7 # example value for chemical potential
    
    expected_output = 10.266540736601016 # expected result
    assert ke_SBMP(value1) == expected_output
    
    # test 2
    value1 = -2 # example value for chemical potential
    
    expected_output = 0.12894139914706026 # expected result
    assert ke_SBMP(value1) == expected_output

def test_ZT_SBMP():
    
    """
    function to test the function to calculate the figure of merit ZT of the material

    Returns
    -------
    None.

    """
    
    # test 1
    value1 = 6.7 # example value for chemical potential
    
    expected_output = 0.07121171193576134 # expected result
    assert ZT_SBMP(value1, 1) == expected_output
    
    # test 2
    value1 = -2 # example value for chemical potential
    
    expected_output = 0.9286245953471025 # expected result
    assert ZT_SBMP(value1,1) == expected_output
