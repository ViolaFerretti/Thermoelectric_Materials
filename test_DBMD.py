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
    function to test the calculation of the figure of merit sigma for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = -5
    expected_output = 3.720897644224199e-05
    
    assert np.isclose(sigmac_DBMD(value1, value2), expected_output)
    
def test_sigmac_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the figure of merit sigma for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 0
    expected_output = 0.0054611779073790705
    
    assert np.isclose(sigmac_DBMD(value1, value2), expected_output)
    
def test_sigmac_DBMD_fixed_delta_3():
    
    """
    function to test the calculation of the figure of merit sigma for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 5
    expected_output = 0.335321634963535
    
    assert np.isclose(sigmac_DBMD(value1, value2), expected_output)

def test_sigmac_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band

    DOC

    """
    
    value1 = 0.5
    value2 = 2
    expected_output = 0.7333560692852861
    
    assert np.isclose(sigmac_DBMD(value1, value2), expected_output)

def test_sigmac_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band

    DOC

    """
    
    value1 = 7
    value2 = 2
    expected_output = 0.0013786998480445215
    assert np.isclose(sigmac_DBMD(value1, value2), expected_output)

def test_sigmac_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band

    DOC

    """
    
    value1 = 18
    value2 = 2
    expected_output = 1.0785594038432437e-08
    
    assert np.isclose(sigmac_DBMD(value1, value2), expected_output)

def test_sigmav_DBMD_fixed_delta_1():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band

    DOC
    """
    
    value1 = 4
    value2 = -5
    expected_output = 0.33532163496353523
    assert np.isclose(sigmav_DBMD(value1, value2), expected_output)

def test_sigmav_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band

    DOC
    """
    
    value1 = 4
    value2 = 0
    expected_output = 0.005461177907379074
    
    assert np.isclose(sigmav_DBMD(value1, value2), expected_output)
    
def test_sigmav_DBMD_fixed_delta_3():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band

    DOC
    """
    
    value1 = 4
    value2 = 5
    expected_output = 3.720897644224199e-05
    
    assert np.isclose(sigmav_DBMD(value1, value2), expected_output)

def test_sigmav_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band

    DOC

    """
    
    value1 = 0.5
    value2 = 2
    expected_output = 0.05622606843544534
    
    assert np.isclose(sigmav_DBMD(value1, value2), expected_output)

def test_sigmav_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band

    DOC

    """
    
    value1 = 7
    value2 = 2
    expected_output = 2.5348256669159954e-05
    
    assert np.isclose(sigmav_DBMD(value1, value2), expected_output)
    
def test_sigmav_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band

    DOC

    """
    
    value1 = 18
    value2 = 2
    expected_output = 1.733740683713239e-10
    
    assert np.isclose(sigmav_DBMD(value1, value2), expected_output)

def test_sigma_DBMD_fixed_delta_1():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = -5
    expected_output = 0.33535884393997745
    
    assert np.isclose(sigma_DBMD(value1, value2), expected_output)
    
def test_sigma_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 0
    expected_output = 0.010922355814758145
    
    assert np.isclose(sigma_DBMD(value1, value2), expected_output)
    
def test_sigma_DBMD_fixed_delta_3():
    
    """
    function to test the calculation of the electrical conductivity sigma for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 5
    expected_output = 0.3353588439399772
    
    assert np.isclose(sigma_DBMD(value1, value2), expected_output)

# S calculations 
def test_Sc_DBMD_fixed_delta_1():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC
    """
    
    value1 = 4
    value2 = -5
    expected_output = -10.632887749436646
    
    assert np.isclose(Sc_DBMD(value1, value2), expected_output)

def test_Sc_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC
    """
    
    value1 = 4
    value2 = 0
    expected_output = -5.6412813745790835
    
    assert np.isclose(Sc_DBMD(value1, value2), expected_output)
    
def test_Sc_DBMD_fixed_delta_3():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC
    """
    
    value1 = 4
    value2 = 5
    expected_output = -1.3454897739003142
    
    assert np.isclose(Sc_DBMD(value1, value2), expected_output)

def test_Sc_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC

    """
    
    value1 = 0.5
    value2 = 2
    expected_output = -0.7280120112460412
    
    assert np.isclose(Sc_DBMD(value1, value2), expected_output)
    
def test_Sc_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC

    """
    
    value1 = 7
    value2 = 2
    expected_output = -6.739623761989619
    
    assert np.isclose(Sc_DBMD(value1, value2), expected_output)
    
def test_Sc_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC

    """
    
    value1 = 18
    value2 = 2
    expected_output = -17.867681126718878
    
    assert np.isclose(Sc_DBMD(value1, value2), expected_output)

def test_Sv_DBMD_fixed_delta_1():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = -5
    expected_output = 1.345489773900313
    
    assert np.isclose(Sv_DBMD(value1, value2), expected_output)
    
def test_Sv_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 0
    expected_output = 5.64128137457915
    
    assert np.isclose(Sv_DBMD(value1, value2), expected_output)
    
def test_Sv_DBMD_fixed_delta_3():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 5
    expected_output = 10.632887749430298
    
    assert np.isclose(Sv_DBMD(value1, value2), expected_output)

def test_Sv_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC
    """
    
    value1 = 0.5
    value2 = 2
    expected_output = 3.7735151059871415
    
    assert np.isclose(Sv_DBMD(value1, value2), expected_output)
    
def test_Sv_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC
    """
    
    value1 = 7
    value2 = 2
    expected_output = 10.736506865669007
    
    assert np.isclose(Sv_DBMD(value1, value2), expected_output)
    
def test_Sv_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC
    """
    
    value1 = 18
    value2 = 2
    expected_output = 24.91636960481909
    
    assert np.isclose(Sv_DBMD(value1, value2), expected_output)

def test_S_DBMD_fixed_delta_1():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = -5
    expected_output = 1.3441607403139442
    
    assert np.isclose(S_DBMD(value1, value2), expected_output)
    
def test_S_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 0
    expected_output = 3.525874987028874e-14
    
    assert np.isclose(S_DBMD(value1, value2), expected_output)
    
def test_S_DBMD_fixed_delta_3():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 5
    expected_output = -1.344160740313946
    
    assert np.isclose(S_DBMD(value1, value2), expected_output)

def test_S_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC

    """
    
    value1 = 0.5
    value2 = 2
    expected_output = -0.40745869618727737
    
    assert np.isclose(S_DBMD(value1, value2), expected_output)
    
def test_S_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC

    """
    
    value1 = 7
    value2 = 2
    expected_output = -6.424115024613419
    
    
    assert np.isclose(S_DBMD(value1, value2), expected_output)
    
def test_S_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the Seebeck coefficient S for the conduction band

    DOC

    """
    
    value1 = 18
    value2 = 2
    expected_output = -17.190824978909973
    
    assert np.isclose(S_DBMD(value1, value2), expected_output)

# # ke calculations 
def test_kec_DBMD_fixed_delta_1():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = -5
    expected_output = 5.34101064720736e-5
    
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output)
    
def test_kec_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 0
    expected_output = 0.00786749220501892
    
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output)
    
def test_kec_DBMD_fixed_delta_3():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 5    
    expected_output = 0.616859374209206
    
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output)

def test_kec_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 0.5
    value2 = 2
    expected_output = 1.3600452591124
    
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output)
    
def test_kec_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 7
    value2 = 2
    expected_output = 0.00216163510819416
    
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output)
    
def test_kec_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 18
    value2 = 2
    expected_output = 1.89955154020879e-8
    
    assert np.isclose(float(kec_DBMD(value1, value2)), expected_output)

def test_kev_DBMD_fixed_delta_1():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = -5
    expected_output = 0.616859374209206
    
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output)
    
def test_kev_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 0
    expected_output = 0.00786749220501531
    
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output)
    
def test_kev_DBMD_fixed_delta_3():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 5
    expected_output = 5.34101064486054e-5
    
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output)

def test_kev_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 0.5
    value2 = 2
    expected_output = 0.0629572805725923
    
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output)
    
def test_kev_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 7
    value2 = 2
    expected_output = 3.96976135383729e-5
    
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output)
    
def test_kev_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 18
    value2 = 2
    expected_output = -1.28219689007053e-8
    
    assert np.isclose(float(kev_DBMD(value1, value2)), expected_output)

def test_ke_DBMD_fixed_delta_1():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = -5
    expected_output = 0.622250992759856
    
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output)
    
def test_ke_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 0
    expected_output = 0.363328642564888
    
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output)
    
def test_ke_DBMD_fixed_delta_3():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 5
    expected_output = 0.622250992759827
    
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output)

def test_ke_DBMD_fixed_eta_1():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 0.5
    value2 = 2
    expected_output = 2.48122027005063
    
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output)
    
def test_ke_DBMD_fixed_eta_2():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 7
    value2 = 2
    expected_output = 0.009803307084193
    
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output)
    
def test_ke_DBMD_fixed_eta_3():
    
    """
    function to test the calculation of the thermal electronic conductivity ke for the conduction band

    DOC

    """
    
    value1 = 18
    value2 = 2
    expected_output = 3.18509765205363e-7
    
    assert np.isclose(float(ke_DBMD(value1, value2)), expected_output)

# ZT calculation
def test_ZT_DBMD_fixed_delta_1():
    
    """
    function to test the calculation of the figure of merit ZT for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = -5
    expected_output = 0.373503029173528
    
    assert np.isclose(float(ZT_DBMD(value1, value2, 1)), expected_output)
    
def test_ZT_DBMD_fixed_delta_2():
    
    """
    function to test the calculation of the figure of merit ZT for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 0
    expected_output = 9.95977623275776e-30
    
    assert np.isclose(float(ZT_DBMD(value1, value2, 1)), expected_output)
    
def test_ZT_DBMD_fixed_delta_3():
    
    """
    function to test the calculation of the figure of merit ZT for the conduction band

    DOC

    """
    
    value1 = 4
    value2 = 5
    expected_output = 0.373503029173535
    
    assert np.isclose(float(ZT_DBMD(value1, value2, 1)), expected_output)

def test_ZT_DBMD_fixed_eta_1():
    
    """
    DOC

    """
    
    value1 = 0.5
    value2 = 2
    expected_output = 0.0376558966803113
    
    assert np.isclose(float(ZT_DBMD(value1, value2, 1)), expected_output)
    
def test_ZT_DBMD_fixed_eta_2():
    
    """
    DOC

    """
    
    value1 = 7
    value2 = 2
    expected_output = 0.057381489289831
    
    assert np.isclose(float(ZT_DBMD(value1, value2, 1)), expected_output)
    
def test_ZT_DBMD_fixed_eta_3():
    
    """
    DOC

    """
    
    value1 = 18
    value2 = 2
    expected_output = 3.23864213825014e-6
    
    assert np.isclose(float(ZT_DBMD(value1, value2, 1)), expected_output)
