""" 
    Programa en python para resolver la pregunta 4 del examen 1 de 
    Lenguajes de Programacion en donde se pide sobrecargar algunos operadores 
    aritmeticos binarios y otros operadores prefijos para realizar operaciones con 
    quaterniones sin necesidad de hacer el llamado de funciones externas 
    Autor Luis Carlos Blanco
    Carne 1710066
"""

import math

def sign(n) :
    """Funcion auxiliar que devolvera un string con el signo del numero que se pasa como argumento"""
    if (n >= 0) :
        return '+'
    else :
        return '-'

class Quaternion(object):
    """Clase Quaternion que representa un elemento de tipo Quaternion
        Un quaternion es una extension de los numeros complejos y se 
        reprresenta de la siguiente forma:
        a + bi + cj + dk
        En la presenta clase se sobrecargaran algunas operaciones aritmeticas
        definidas en python para que los quaterniones puedan operarse sin hacer llamadas
        adicionales a funciones.
    """

    # Constructor de un objeto de tipo Quaternion
    def __init__(self, a, bi, cj, dk) :
        self.a = a
        self.bi = bi
        self.cj = cj
        self.dk = dk

    def __eq__(self, q) :
        """
            Sobrecarga del operador == para realizar la conmparacion entre dos quaterniones
        """
        if (isinstance(q, Quaternion)) :
            return (self.a == q.a and self.bi == q.bi and self.cj == q.cj and self.dk == q.dk)
        
        raise TypeError("Unsupported operand type(s) for ==: 'Quaternion' and '{}'".format(type(q)))

    def __str__(self) -> str:
        """
            Sobrecarga de la funcion str() para convertir un quaternion en un string
        """
        return '{} {} {}i {} {}j {} {}k'.format(self.a, sign(self.bi), abs(self.bi), 
                                                sign(self.cj), abs(self.cj), sign(self.dk), abs(self.dk))

    def __add__(self, q) :
        """
            Sobrecarga del operador binario + para realizar la suma entre dos quaterniones o 
            un quaternion y un numero entero o float.
        """
        if (isinstance(q, int) or isinstance(q, float)) :
            return Quaternion(self.a + q, self.bi, self.cj, self.dk)
        elif (isinstance(q, Quaternion)) :
            return Quaternion(self.a + q.a, self.bi + q.bi, self.cj + q.cj, self.dk + q.dk)

        raise TypeError("Unsupported operand type(s) for +: 'Quaternion' and '{}'".format(type(q)))

    def __invert__(self) :
        """
            Sobrecarga del operador prefijo ~ para obtener la conjugada de un quaternion
        """
        return Quaternion(self.a, -self.bi, -self.cj, -self.dk)

    def __mul__(self, q) :
        """
            Sobrecarga del operador binario * para realizar la multiplicacion entre dos quaterniones o 
            un quaternion y un numero entero o float.
        """
        if (isinstance(q, int) or isinstance(q, float)) :
            return Quaternion(self.a * q, self.bi * q, self.cj * q, self.dk * q)
        elif (isinstance(q, Quaternion)) :
            return Quaternion(self.a * q.a - self.bi * q.bi - self.cj * q.cj - self.dk * q.dk,
                              self.a * q.bi + self.bi * q.a + self.cj * q.dk - self.dk * q.cj,
                              self.a * q.cj - self.bi * q.dk + self.cj * q.a + self.dk * q.bi,
                              self.a * q.dk + self.bi * q.cj - self.cj * q.bi + self.dk * q.a)

        raise TypeError("Unsupported operand type(s) for *: 'Quaternion' and '{}'".format(type(q)))

    def __pos__(self) :
        """
            Sobrecarga del operador prefijo + para obtener el modulo de un quaternion
        """
        return  math.sqrt(self.a**2 + self.bi**2 + self.cj**2 + self.dk**2)