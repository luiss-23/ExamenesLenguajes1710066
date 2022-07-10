""" Implementacion del simulador de manejador de tipos
    Autor: Luis Carlos Blanco 
    Carne: 1710066 """

import DataTypes as t
from math import gcd
import itertools

def mcm(list: list) :
    mcm = 1
    for i in list:
        mcm = mcm * i // gcd(mcm, i)

    return mcm

class Simulador(object) :
    
    def __init__(self):
        self.atomos = {}
        self.structs = {}
        self.unions = {}

    def addAtomo(self, nombre: str, representacion: int, alineacion: int) :
        if self.atomos.get(nombre) :
            print(f"Ya existe un atomo con nombre {nombre}")
            return

        if self.structs.get(nombre) :
            print(f"Ya existe un struct con nombre {nombre}")
            return

        if self.unions.get(nombre) :
            print(f"Ya existe una union con nombre {nombre}")
            return

        self.atomos[nombre] = t.Atomico(nombre, representacion, alineacion)

    def addStruct(self, nombre: str, listaTipos: list) :
        if self.atomos.get(nombre) :
            print(f"Ya existe un atomo con nombre {nombre}")
            return

        if self.structs.get(nombre) :
            print(f"Ya existe un struct con nombre {nombre}")
            return

        if self.unions.get(nombre) :
            print(f"Ya existe una union con nombre {nombre}")
            return

        for tipo in listaTipos :
            if not (self.atomos.get(tipo) or self.structs.get(tipo) or self.unions.get(tipo)) :
                print(f"El tipo {tipo} no ha sido definido.")
                return        

        self.structs[nombre] = t.Struct(nombre, listaTipos)

    def addUnion(self, nombre: str, listaTipos: list) :
        if self.atomos.get(nombre) :
            print(f"Ya existe un atomo con nombre {nombre}")
            return

        if self.structs.get(nombre) :
            print(f"Ya existe un struct con nombre {nombre}")
            return

        if self.unions.get(nombre) :
            print(f"Ya existe una union con nombre {nombre}")
            return

        for tipo in listaTipos :
            if not (self.atomos.get(tipo) or self.structs.get(tipo) or self.unions.get(tipo)) :
                print(f"El tipo {tipo} no ha sido definido.")
                return        

        self.unions[nombre] = t.Union(nombre, listaTipos)

    def obtenerTipo(self, nombre: str) :
        return (self.atomos.get(nombre) or self.structs.get(nombre) or self.unions.get(nombre))

    def obtenerTamanyoTipo(self, tipo) :
        if isinstance(tipo, t.Atomico) :
            return tipo.representacion
        elif isinstance(tipo, t.Union) :
            tamanyoTipos = []
            for ty in tipo.tipos :
                tamanyoTipos.append(self.obtenerTamanyoTipo(self.obtenerTipo(ty)))
            return max(tamanyoTipos)
        else :
            tamanyoStruct = 0
            for ty in tipo.tipos:
                tamanyoStruct += self.obtenerTamanyoTipo(self.obtenerTipo(ty))
            return tamanyoStruct

    def alineacion(self, tipo) :
        if isinstance(tipo, t.Atomico) :
            return tipo.alineacion
        elif isinstance(tipo, t.Union) :
            alineacionTipos = []
            for ty in tipo.tipos :
                alineacionTipos.append(self.alineacion(self.obtenerTipo(ty)))
            return mcm(alineacionTipos)
        else :
            return self.alineacion(self.obtenerTipo(tipo.tipos[0]))
            
    def desperdicio(self, i:int, a: int) :
        if i % a != 0 :
            return a - (i % a)
        else: return 0

    def tamanyoDesperdicioSinEmpaquetar(self, i, dt, tipo) :
        if isinstance(tipo, t.Atomico) :
            desperdicioTipo = self.desperdicio(i, self.alineacion(tipo))
            dt += desperdicioTipo

            i = i + desperdicioTipo + tipo.representacion
            return (i, dt)
        elif isinstance(tipo, t.Union) :
            alineacionUnion = self.alineacion(tipo) 
            desperdicioTipo = self.desperdicio(i, alineacionUnion)

            dt += desperdicioTipo

            i = i + desperdicioTipo + self.obtenerTamanyoTipo(tipo)

            return (i, dt)
        else :
            alineacionStruct = self.alineacion(tipo)
            desperdicioTipo = self.desperdicio(i, alineacionStruct)
            i += desperdicioTipo
            dt += desperdicioTipo

            (itemp, dtemp) = (0, 0)

            for ty in tipo.tipos:
                (itemp, dtemp) = self.tamanyoDesperdicioSinEmpaquetar(itemp, dtemp, self.obtenerTipo(ty))

            i += itemp
            dt += dtemp
            return (i, dt)

    def tamanyoDesperdicioReordenando(self, i: int, dt: int, tipo) :
        if isinstance(tipo, t.Atomico) :
            desperdicioTipo = self.desperdicio(i, self.alineacion(tipo))
            dt += desperdicioTipo

            i += desperdicioTipo + tipo.representacion
            return (i, dt)
        elif isinstance(tipo, t.Struct) :
            copiaCampos = tipo.tipos[:]
            copiaI = i
            copiaDt = dt

            permutacionesStruct = list(itertools.permutations(tipo.tipos))
            espacioPermutacion = []

            for element in permutacionesStruct :
                tipo.tipos = element

                (itemp, dtemp) = (0, 0)
                for ty in tipo.tipos :
                    (itemp, dtemp) = (self.tamanyoDesperdicioReordenando(itemp, dtemp, self.obtenerTipo(ty)))

                i += itemp
                dt += dtemp

                espacioPermutacion.append((itemp, dtemp))

                dt = copiaDt
                i = copiaI

            tipo.tipos = copiaCampos

            return min(espacioPermutacion)
        else :
            alineacionUnion = self.alineacion(tipo)
            desperdicioTipo = self.desperdicio(i, alineacionUnion)

            dt += desperdicioTipo
            i = i + desperdicioTipo + self.obtenerTamanyoTipo(tipo)

            return (i, dt)

    def describirTipo(self, nombre: str) :
        if not (self.atomos.get(nombre) or self.structs.get(nombre) or self.unions.get(nombre)) :
            print(f"El tipo {nombre} no ha sido definido.")
            return

        tipoActual = self.obtenerTipo(nombre)

        # Se guardan todos los tipos de registros sin empaquetar
        (espacioOcupado, desperdicio) = self.tamanyoDesperdicioSinEmpaquetar(0, 0, tipoActual)
        alineacion = self.alineacion(tipoActual)
        print(f"Del tipo '{nombre}' se obtienen los siguientes datos si el tipo se guarda sin empaquetamiento:")
        print(f"Tamanyo: {espacioOcupado}")
        print(f"Desperdicio: {desperdicio}")
        print(f"Alineacion: {alineacion}")

        # Se guardan todos los tipos con empaquetamiento
        espacioOcupado = self.obtenerTamanyoTipo(tipoActual)
        alineacion = self.alineacion(tipoActual)
        desperdicio = 0         # No hay desperdicio ya que se esta empaquetando
        print(f"Del tipo '{nombre}' se obtienen los siguientes datos si el tipo se guarda con empaquetamiento:")
        print(f"Tamanyo: {espacioOcupado}")
        print(f"Desperdicio: {desperdicio}")
        print(f"Alineacion: {alineacion}")

        # Se guardan todos los tipos reordenando en la memoria
        (espacioOcupado, desperdicio) = self.tamanyoDesperdicioReordenando(0, 0, tipoActual)
        alineacion = self.alineacion(tipoActual)
        print(f"Del tipo '{nombre}' se obtienen los siguientes datos si el tipo se guarda sin empaquetamiento:")
        print(f"Tamanyo: {espacioOcupado}")
        print(f"Desperdicio: {desperdicio}")
        print(f"Alineacion: {alineacion}")


        