""" Implementacion de los tipos de datos requeridos para el 
    enunciado 5 
    Autor: Luis Carlos Blanco
    Carne: 1710066
"""

class Atomico(object) :
    def __init__(self, n: str, r: int, a: int) :
        self.nombre = n
        self.representacion = r
        self.alineacion = a

    def __eq__(self, other) -> bool:
        return (self.nombre, self.representacion, self.alineacion) == (other.nombre, other.representacion, other.alineacion)
        

class Struct(object) :
    def __init__(self, n: str, t: list) :
        self.nombre = n
        self.tipos = t

    def __eq__(self, other) -> bool:
        return (self.nombre, self.tipos) == (other.nombre, other.tipos)

class Union(object) :
    def __init__(self, n: str, t: list) :
        self.nombre = n
        self.tipos = t

    def __eq__(self, other) -> bool:
        return (self.nombre, self.tipos) == (other.nombre, other.tipos)