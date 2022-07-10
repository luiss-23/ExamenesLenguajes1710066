""" 
    Programa para obtener datos de cada una de las funciones y generar 
    una grafica comparativa
"""
from FuncionF import *
import time

if __name__ == "__main__" :
    n = int(input("Ingrese el número n para evaluar la funcion: "))
    tiRecursiva = time.time()
    frecursiva = f_recursiva(n)
    tfRecursiva = time.time() - tiRecursiva

    tiRecursivaCola = time.time()
    frecursivacola = f_recursiva_cola(n)
    tfRecursivaCola = time.time() - tiRecursivaCola

    tiIterativa = time.time()
    fiterativa = f_iterativa(n)
    tfIterativa = time.time() - tiIterativa

    print(f"Tiempo de corrida recursiva con n = {n} es: {tfRecursiva}")
    print(f"Tiempo de corrida recursiva de cola con n = {n} es: {tfRecursivaCola}")
    print(f"Tiempo de corrida iterativa con n = {n} es: {tfIterativa}")