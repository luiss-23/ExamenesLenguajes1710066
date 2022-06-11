""" 
    Programa para realizar los test correspondientes al archivo Quaterniones.py 
    asi como tambien para obtener la cobertura del codigo, la cual debe ser mayor
    a un 80%.
"""

import Quaterniones as qt
import pytest
import math


quaternion = qt.Quaternion(1, -2, 3, -4)
quaternion2 = qt.Quaternion(4, 5, 6, 7)

def test_errores_sum() :
    with pytest.raises(TypeError):
        assert(quaternion + 'ReySkywalker')

def test_error_mult() :
    with pytest.raises(TypeError):
        assert(quaternion * 'KateBishop')

def test_error_eq() :
    with pytest.raises(TypeError):
        assert(quaternion2 == 'WandaMaximoff')

def test_str() :
    assert(str(quaternion) == '1 - 2i + 3j - 4k')

def test_equal_quaterniones() : 
    assert(quaternion == qt.Quaternion(1, -2, 3, -4))

def test_suma_quaterniones() : 
    assert(quaternion + quaternion2 == qt.Quaternion(5, 3, 9, 3))

def test_suma_quaternion_int() : 
    assert(quaternion + 10 == qt.Quaternion(11, -2, 3, -4)) 

def test_suma_quaternion_float() : 
    assert(quaternion + 10.3 == qt.Quaternion(11.3, -2, 3, -4))

def test_suma_quaterniones_conjugada() : 
    assert(quaternion + ~quaternion2 == qt.Quaternion(5, -7, -3, -11)) 

def test_suma_quaterniones_conjugada2() : 
    assert(~quaternion + ~quaternion2 == qt.Quaternion(5, -3, -9, -3)) 

def test_conjugada() : 
    assert(~quaternion == qt.Quaternion(1, 2, -3, 4)) 

def test_mult_quaterniones() : 
    assert(quaternion * quaternion2 == qt.Quaternion(24, 42, 12, -36))

def test_mult_quaternion_int() : 
    assert(quaternion * 3 == qt.Quaternion(3, -6, 9, -12))

def test_mult_quaternion_float() : 
    assert(quaternion * 3.5 == qt.Quaternion(3.5, -7, 10.5, -14))

def test_abs_quaternion() : 
    assert(+quaternion == math.sqrt(30))

def test_operacion_compuesta() :
    assert(quaternion * quaternion2 + ~quaternion + 3 == qt.Quaternion(28, 44, 9, -32))