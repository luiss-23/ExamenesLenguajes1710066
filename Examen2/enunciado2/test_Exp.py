"""
    Programa para realizar los test de las funciones en ExpPrePost.py y 
    obtener la cobertura del codigo.
"""
from ExpPrePostFija import *

bool1 = True
bool2 = False
expPrefija = "| & => true true false true"
expPostfija = "true false => false | true false ^ | &"

def test_Conjuncion():
    assert(conjuncion(bool1, bool2) == False)

def test_Disyuncion():
    assert(disyuncion(bool1, bool2) == True)

def test_Implicacion():
    assert(implicacion(bool1, bool2) == False)

def test_Negacion():
    assert(negacion(bool1) == False)

def test_EvalPrefija():
    assert(evaluacionPrefija(expPrefija) == True)

def test_EvalPostfija():
    assert(evaluacionPostfija(expPostfija) == False)

def test_mostrarPrefija():
    assert(mostrarEvaluacionPrefija(expPrefija) == "(true => true) & false | true")

def test_mostrarPostfija():
    assert(mostrarEvaluacionPostfija(expPostfija) == "(true => false) | false & true | ^false")