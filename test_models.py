# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:22:02 2023

@author: viola
"""
import functions
from functions import *
import numpy as np
from mpmath import *

from DBM_Parabolic import *
from DBM_Dirac import *
from SBM_Parabolic import *

# testing of specific functions of 2BM_Parabolic model

def test_sigmac_DBMP(): 
    value1 = np.asarray([2,3,4,9])
    value2 = np.asarray([7,2,6,8])
    #print(sigmac_DBMP(value1,value2))
    expected_output = np.asarray([10.0134307,   0.62652338,  4.25385602,  0.62652338])
    assert np.allclose(sigmac_DBMP(value1, value2), expected_output)

def test_sigmav_DBMP():
    value1 = np.asarray([2,3,4,9])
    value2 = np.asarray([7,2,6,8])
    #print(sigmav_DBMP(value1,value2))
    expected_output = np.asarray([2.46804379e-04, 1.34306970e-02, 9.07977984e-05, 8.27987528e-08])
    assert np.allclose(sigmav_DBMP(value1, value2), expected_output)

def test_sigma_DBMP():
    value1 = np.asarray([2,5,0.5,9])
    value2 = np.asarray([7,8,6,2])
    print(sigma_DBMP(value1,value2))
    expected_output = np.asarray([1.00136775e+01, 6.09717922e+00, 1.10111615e+01, 1.85633603e-03])
    assert np.allclose(sigma_DBMP(value1, value2), expected_output)

def test_Sc_DBMP():
    value1 = np.asarray([2,5,0.5,9])
    value2 = np.asarray([7,8,6,2])
    print(Sc_DBMP(value1,value2))
    expected_output = np.asarray([-0.64769772271443649, -0.99906753097473289,
    -0.5921557118310008, -9.0004557793968374])
    
    assert np.allclose(Sc_DBMP(value1, value2).astype(float), expected_output)

# @given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_Sv_DBMP():
    value1 = np.asarray([2,5,0.5,9])
    value2 = np.asarray([7,8,6,2])
    print(Sv_DBMP(value1,value2))
    expected_output = np.asarray([11.000061701939575, 15.000001130166538,
    8.5007512804651828, 13.000008350806922])
    assert np.allclose(Sv_DBMP(value1, value2).astype(float), expected_output)

def test_S_DBMP():
    value1 = np.asarray([2,5,0.5,9])
    value2 = np.asarray([7,8,6,2])
    print(S_DBMP(value1,value2))
    expected_output = np.asarray([-0.64741064356330968, -0.99905566872723073,
    -0.58967452643603291, -8.6045769140110089])
    assert np.allclose(S_DBMP(value1, value2).astype(float), expected_output)

def test_kec_DBMP():
    value1 = np.asarray([2,5,0.5,9])
    value2 = np.asarray([7,8,6,2])
    print(kec_DBMP(value1,value2))
    expected_output = np.asarray([29.383543652975188, 16.302089684568426,
    32.803953624335598, 0.0036462812001165634])
    assert np.allclose(kec_DBMP(value1, value2).astype(float), expected_output)

def test_kev_DBMP():
    value1 = np.asarray([2,5,3.5,9])
    value2 = np.asarray([4,9,6,2])
    print(kev_DBMP(value1,value2))
    expected_output = np.asarray([0.0099058050591114832, 3.3261138401355079e-6,
    0.00029939891570513605, 6.6806384743914662e-5])
    assert np.allclose(kev_DBMP(value1, value2).astype(float), expected_output)

def test_ke_DBMP():
    value1 = np.asarray([2,5,3.5,9])
    value2 = np.asarray([4,9,6,2])
    print(ke_DBMP(value1,value2))
    expected_output = np.asarray([11.071051221682763, 22.667035350654011,
    13.378333192880682, 0.019589955973850104])
    assert np.allclose(ke_DBMP(value1, value2).astype(float), expected_output)


def test_ZT_DBMP():
    value1 = np.asarray([2,5,3.5,9])
    value2 = np.asarray([4,9,6,2])
    print(ZT_DBMP(value1, value2, 1))
    expected_output = np.asarray([0.59021616097800866, 0.21277958797786051,
    0.46330560386124203, 0.13480006062089001])
    assert np.allclose(ZT_DBMP(value1, value2, 1).astype(float), expected_output)

# testing of specific functions of 2BM_Dirac model

def test_sigmac_DBMD():
    value1 = 2
    value2 = 4
    print(sigmac_DBMD(value1, value2))
    expected_output = 0.6320015299793118
    assert np.allclose(sigmac_DBMD(value1, value2).astype(float), expected_output)

    value1 = 1.5
    value2 = 7
    print(sigmac_DBMD(value1, value2))
    expected_output = 0.9368293113655424
    assert np.allclose(sigmac_DBMD(value1, value2).astype(float), expected_output)

def test_sigmav_DBMD():
    value1 = 2
    value2 = 4
    print(sigmav_DBMD(value1, value2))
    expected_output = 0.001101975029276735
    assert np.allclose(sigmav_DBMD(value1, value2).astype(float), expected_output)
    
    value1 = 1.5
    value2 = 7
    print(sigmav_DBMD(value1, value2))
    expected_output = 0.00010346458581792292
    assert np.allclose(sigmav_DBMD(value1, value2).astype(float), expected_output)

def test_sigma_DBMD():
    value1 = 2
    value2 = 4
    print(sigma_DBMD(value1, value2))
    expected_output = 0.6331035050085886
    assert np.allclose(sigma_DBMD(value1, value2).astype(float), expected_output)
    
    value1 = 1.5
    value2 = 7
    print(sigma_DBMD(value1, value2))
    expected_output = 0.9369327759513603
    assert np.allclose(sigma_DBMD(value1, value2).astype(float), expected_output)

def test_Sc_DBMD():
    value1 = 2
    value2 = 4
    print(Sc_DBMD(value1, value2))
    expected_output = -0.7473427239793451
    assert np.allclose(Sc_DBMD(value1, value2).astype(float), expected_output)
    
    value1 = 1.5
    value2 = 7
    print(Sc_DBMD(value1, value2))
    expected_output = -0.10200337819379099
    assert np.allclose(Sc_DBMD(value1, value2).astype(float), expected_output)

def test_Sv_DBMD():
    value1 = 2
    value2 = 4
    print(Sv_DBMD(value1, value2))
    expected_output = 7.492339787057502
    assert np.allclose(Sv_DBMD(value1, value2).astype(float), expected_output)
    
    value1 = 1.5
    value2 = 7
    print(Sv_DBMD(value1, value2))
    expected_output = 9.932629860956144
    assert np.allclose(Sv_DBMD(value1, value2).astype(float), expected_output)

def test_S_DBMD():
    value1 = 2
    value2 = 4
    print(S_DBMD(value1, value2))
    expected_output = -0.7330007967833999
    assert np.allclose(S_DBMD(value1, value2).astype(float), expected_output)
    
    value1 = 1.5
    value2 = 7
    print(S_DBMD(value1, value2))
    expected_output = -0.10089526329102308
    assert np.allclose(S_DBMD(value1, value2).astype(float), expected_output)

def test_kec_DBMD():
    value1 = 2
    value2 = 4
    print(kec_DBMD(value1, value2))
    expected_output = 1.29197054949625
    assert np.allclose(float(kec_DBMD(value1, value2)), expected_output)
    
    value1 = 1.5
    value2 = 7
    print(kec_DBMD(value1, value2))
    expected_output = 2.79171801794985
    assert np.allclose(float(kec_DBMD(value1, value2)), expected_output)

def test_kev_DBMD():
    value1 = 2
    value2 = 4
    print(kev_DBMD(value1, value2))
    expected_output = 0.00141700695019598
    assert np.allclose(float(kev_DBMD(value1, value2)), expected_output)
    
    value1 = 1.5
    value2 = 7
    print(kev_DBMD(value1, value2))
    expected_output = 0.000127430727024787
    assert np.allclose(float(kev_DBMD(value1, value2)), expected_output)

def test_ke_DBMD():
    value1 = 2
    value2 = 4
    print(ke_DBMD(value1, value2))
    expected_output = 1.36807302691728
    assert np.allclose(float(ke_DBMD(value1, value2)), expected_output)
    
    value1 = 1.5
    value2 = 7
    print(ke_DBMD(value1, value2))
    expected_output = 2.8022625471581
    assert np.allclose(float(ke_DBMD(value1, value2)), expected_output)

def test_ZT_DBMD():
    value1 = 2
    value2 = 4
    print(ZT_DBMD(value1, value2, 1))
    expected_output = 0.143644340674808
    assert np.allclose(float(ZT_DBMD(value1, value2,1)), expected_output)
    
    value1 = 1.5
    value2 = 7
    print(ZT_DBMD(value1, value2, 1))
    expected_output = 0.00250846407724928
    assert np.allclose(float(ZT_DBMD(value1, value2, 1)), expected_output)

# testing of specific functions of 1BM_Parabolic model

def test_func_Fi():
    
    value1=-4
    value2=20
    
    # test 1: i=0
    i=0
    print(func_Fi(value2, i, value1))
    expected_output=3.7751345441365816e-11
    assert func_Fi(value2, i, value1)==expected_output
    
    #test 2: i=1
    i=1
    print(func_Fi(value2, i, value1))
    expected_output=7.550269088273163e-10
    assert func_Fi(value2, i, value1)==expected_output
    
    #test 3: i=2
    i=2
    print(func_Fi(value2, i, value1))
    expected_output=1.5100538176546325e-08
    assert func_Fi(value2, i, value1)==expected_output
  

def test_Fic():
    
    value1=-8.5
    
    #test 1: i=0
    i=0
    print(Fic(i, value1))
    expected_output=0.000101723836064718
    assert Fic(i, value1)==expected_output
    
    #test 2: i=1
    i=1
    print(Fic(i, value1))
    expected_output=0.00010172901005109025
    assert Fic(i, value1)==expected_output
    
    #test 3: i=2
    i=2
    print(Fic(i, value1))
    expected_output=0.00020346319440044903
    assert Fic(i, value1)==expected_output


def test_sigma_SBMP():
    value1=6.7
    print(sigma_SBMP(value1))
    expected_output=3.350615077475857
    assert sigma_SBMP(value1)==expected_output

 
def test_S_SBMP():
    value1=6.7
    print(S_SBMP(value1))
    expected_output=0.4893377712821068
    assert S_SBMP(value1)==expected_output


def test_ke_SBMP():
    value1=6.7
    print(ke_SBMP(value1))
    expected_output=10.266540736601016
    assert ke_SBMP(value1)==expected_output


def test_ZT_SBMP():
    value1=6.7
    print(ZT_SBMP(value1,1))
    expected_output=0.07121171193576134
    assert ZT_SBMP(value1,1)==expected_output
