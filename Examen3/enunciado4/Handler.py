""" Implementacion del manejador de tablas de metodos 
    virtuales para un sistema orientado a objetos con 
    herencia simple y despacho dinamico de metodos. """

from dataclasses import dataclass


@dataclass
class Tipo():
    clase: str
    super_: object
    metodos: list

class Handler() :
    
    def __init__(self):
        self.tiposCreados = {}

    def class_(self, clase, super, metodos):

        if clase in self.tiposCreados:
            print(f"La clase {clase} ya ha sido creada anteriormente.")
            return
        elif super and not super in self.tiposCreados:
            print(f"La superclase {super} no existe, no se puede heredar de una clase inexistente.")
            return
        elif len(metodos) != len(set(metodos)):
            print(f"Se repiten definiciones en la lista de metodos.")

        if super :
            self.tiposCreados[clase] = Tipo(clase, super, metodos)
        else:
            self.tiposCreados[clase] = Tipo(clase, None, metodos)

    def describir(self, clase):

        if clase in self.tiposCreados:
            describirClase = self.tiposCreados[clase]
            listaMetodos = []
            if describirClase.super_ :
                for metodo in self.tiposCreados[clase].metodos:
                    listaMetodos.append((clase, metodo))

                superClase = self.tiposCreados[describirClase.super_]
                for metodo in superClase.metodos:
                    if (clase, metodo) in listaMetodos:
                        continue
                    else:
                        listaMetodos.append((superClase.clase, metodo))
            else:
                for metodo in self.tiposCreados[clase].metodos:
                    listaMetodos.append((clase, metodo))

            for element in listaMetodos:
                print(f"{element[1]} -> {element[0]} :: {element[1]}")
        else:
            print(f"La clase {clase} que se quiere describir no está definida.")
            return

