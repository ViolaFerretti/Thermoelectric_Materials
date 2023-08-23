# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:22:02 2023

@author: viola
"""
import functions
from functions import *
import numpy as np
from hypothesis import given
import hypothesis.strategies as st

from DBM_Parabolic import *
from DBM_Dirac import *
from SBM_Parabolic import *

# testing of specific functions of 2BM_Parabolic model

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_sigmac_DBMP(value1,value2):
    print(value1,value2)
    expected_output = 2*F1c(value1,value2)+(value2-value1)*2*F0c(value1,value2)
    assert sigmac_DBMP(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_sigmav_DBMP(value1,value2):
    print(value1,value2)
    expected_output = -2*F1v(value1,value2)+(value2+value1)*(-2)*F0v(value1,value2)
    assert sigmav_DBMP(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_sigma_DBMP(value1,value2):
    print(value1,value2)
    expected_output = sigmac_DBMP(value1,value2)+sigmav_DBMP(value1,value2)
    assert sigma_DBMP(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_Sc_DBMP(value1,value2):
    print(value1,value2)
    expected_output = -(2*F2c(value1,value2)+(value2-value1)*2*F1c(value1,value2)) / (2*F1c(value1,value2)+(value2-value1)*2*F0c(value1,value2))#+small)
    assert Sc_DBMP(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_Sv_DBMP(value1,value2):
    print(value1,value2)
    expected_output = -(-2*F2v(value1,value2)+(value1+value2)*(-2)*F1v(value1,value2)) / (-2*F1v(value1,value2)+(value1+value2)*(-2)*F0v(value1,value2))#+small)
    assert Sv_DBMP(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_S_DBMP(value1,value2):
    print(value1,value2)
    expected_output = (sigmac_DBMP(value1,value2)*Sc_DBMP(value1,value2)+sigmav_DBMP(value1,value2)*Sv_DBMP(value1,value2))/(sigmac_DBMP(value1,value2)+sigmav_DBMP(value1,value2))
    assert S_DBMP(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_kec_DBMP(value1,value2):
    print(value1,value2)
    expected_output = (F3c(value1,value2)+(value2-value1)*2*F2c(value1,value2)) - ((2*F2c(value1,value2)+(value2-value1)*2*F1c(value1,value2))**2/(2*F1c(value1,value2)+(value2-value1)*2*F0c(value1,value2)))#+small) )
    assert kec_DBMP(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_kev_DBMP(value1,value2):
    print(value1,value2)
    expected_output = (F3v(value1,value2)+(value1+value2)*(-2)*F2v(value1,value2)) - ((-2*F2v(value1,value2)+(value1+value2)*(-2)*F1v(value1,value2))**2/(-2*F1v(value1,value2)+(value1+value2)*(-2)*F0v(value1,value2)))#+small) )
    assert kev_DBMP(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_ke_DBMP(value1,value2):
    print(value1,value2)
    expected_output = ((sigmac_DBMP(value1,value2)*sigmav_DBMP(value1,value2))/(sigmac_DBMP(value1,value2)+sigmav_DBMP(value1,value2)))*(Sc_DBMP(value1,value2)-Sv_DBMP(value1,value2))**2+kec_DBMP(value1,value2)+kev_DBMP(value1,value2)
    assert ke_DBMP(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_ZT_DBMP(value1,value2):
    print(value1,value2)
    expected_output = ((S_DBMP(value1,value2)**2)*sigma_DBMP(value1,value2))/(ke_DBMP(value1,value2)+1)#+kp(x))
    assert ZT_DBMP(value1,value2,1) == expected_output

# testing of specific functions of 2BM_Dirac model

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_sigmac_DBMD(value1,value2):
    print(value1,value2)
    expected_output = F0c(value1,value2)-Gic(0,value1,value2)
    assert sigmac_DBMD(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_sigmav_DBMD(value1,value2):
    print(value1,value2)
    expected_output = F0v(value1,value2)-Giv(0,value1,value2)
    assert sigmav_DBMD(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_sigma_DBMD(value1,value2):
    print(value1,value2)
    expected_output = sigmac_DBMD(value1,value2)+sigmav_DBMD(value1,value2)
    assert sigma_DBMD(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_Sc_DBMD(value1,value2):
    print(value1,value2)
    expected_output = -(F1c(value1,value2)-Gic(1,value1,value2))/(F0c(value1,value2)-Gic(0,value1,value2))
    assert Sc_DBMD(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_Sv_DBMD(value1,value2):
    print(value1,value2)
    expected_output = -(F1v(value1,value2)-Giv(1,value1,value2))/(F0v(value1,value2)-Giv(0,value1,value2))
    assert Sv_DBMD(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_S_DBMD(value1,value2):
    print(value1,value2)
    expected_output = (sigmac_DBMD(value1,value2)*Sc_DBMD(value1,value2)+sigmav_DBMD(value1,value2)*Sv_DBMD(value1,value2))/(sigmac_DBMD(value1,value2)+sigmav_DBMD(value1,value2))
    assert S_DBMD(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_kec_DBMD(value1,value2):
    print(value1,value2)
    expected_output = (F2c(value1,value2)-Gic(2,value1,value2))-((F1c(value1,value2)-Gic(1,value1,value2))**2)/(F0c(value1,value2)-Gic(0,value1,value2))
    assert kec_DBMD(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_kev_DBMD(value1,value2):
    print(value1,value2)
    expected_output = (F2v(value1,value2)-Giv(2,value1,value2))-((F1v(value1,value2)-Giv(1,value1,value2))**2)/(F0v(value1,value2)-Giv(0,value1,value2))
    assert kev_DBMD(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_ke_DBMD(value1,value2):
    print(value1,value2)
    expected_output = ((sigmac_DBMD(value1,value2)*sigmav_DBMD(value1,value2))/(sigmac_DBMD(value1,value2)+sigmav_DBMD(value1,value2)))*(Sc_DBMD(value1,value2)-Sv_DBMD(value1,value2))**2+kec_DBMD(value1,value2)+kev_DBMD(value1,value2)
    assert ke_DBMD(value1,value2) == expected_output

@given(value1=st.floats(min_value=0,max_value=10),value2=st.floats(min_value=-10,max_value=10))
def test_ZT_DBMD(value1,value2):
    print(value1,value2)
    expected_output = ((S_DBMD(value1,value2)**2)*sigma_DBMD(value1,value2))/(ke_DBMD(value1,value2)+1)#+kp(x))
    assert ZT_DBMD(value1,value2,1) == expected_output

# testing of specific functions of 1BM_Parabolic model

@given(value1=st.floats(min_value=-10,max_value=10),value2=st.floats(-100,100))
def test_func_Fi(value1,value2):
    
    #test 1: i=0
    i=0
    expected_output=(value2)**i/(exp1(value2-value1))
    assert func_Fi(value2, i, value1)==expected_output
    
    #test 2: i=1
    i=1
    expected_output=(value2)**i/(exp1(value2-value1))
    assert func_Fi(value2, i, value1)==expected_output
    
    #test 3: i=2
    i=2
    expected_output=(value2)**i/(exp1(value2-value1))
    assert func_Fi(value2, i, value1)==expected_output
    
@given(value1=st.floats(min_value=-10,max_value=10))   
def test_Fic(value1):
    
    #test 1: i=0
    i=0
    expected_output=0.5*quad(func_Fi, 0,100, (i,value1))[0]
    assert Fic(i, value1)==expected_output
    
    #test 2: i=1
    i=1
    expected_output=0.5*quad(func_Fi, 0,100, (i,value1))[0]
    assert Fic(i, value1)==expected_output
    
    #test 3: i=2
    i=2
    expected_output=0.5*quad(func_Fi, 0,100, (i,value1))[0]
    assert Fic(i, value1)==expected_output
    
@given(value1=st.floats(min_value=-10,max_value=10)) 
def test_sigma_SBMP(value1):
    expected_output=Fic(0,value1)
    assert sigma_SBMP(value1)==expected_output
    
@given(value1=st.floats(min_value=-10,max_value=10))     
def test_S_SBMP(value1):
    expected_output=(2*Fic(1,value1)-value1*Fic(0,value1))/Fic(0,value1)
    assert S_SBMP(value1)==expected_output

@given(value1=st.floats(min_value=-10,max_value=10)) 
def test_ke_SBMP(value1):
    expected_output=3*Fic(2,value1)-4*value1*Fic(1,value1)+(value1**2)*Fic(0,value1)-((2*Fic(1,value1)-value1*Fic(0,value1))**2)/Fic(0,value1)
    print(type(expected_output))
    assert ke_SBMP(value1)==expected_output
    
@given(value1=st.floats(min_value=-10,max_value=10)) 
def test_ZT_SBMP(value1):
    expected_output=((S_SBMP(value1)**2)*sigma_SBMP(value1))/(ke_SBMP(value1)+1)#+kp(x))
    assert ZT_SBMP(value1,1)==expected_output