""" Implementacion del cliente que mostrar el uso del Simulador
    Autor: Luis Carlos Blanco
    Carne: 1710066
"""

import Simulador as S
import re

if __name__ == '__main__' :
    print("Bienvenido al simulador de manejo de tipos de datos")
    print("Puedes interactuar conmigo mediante los siguientes comandos:")
    print("ATOMICO <nombre> <representacion> <alineacion>")
    print("STRUCT <nombre> <[tipos]>")
    print("UNION <nombre> <[tipos]>")
    print("donde <nombre> representa el nombre que tendra el dato a definir,")
    print("<representacion> es la cantidad de bytes que ocupa el tipo")
    print("<alineacion> es los bytes en los que se debe alinear el tipo")
    print("<[tipos]> es un arreglo que contiene los tipos que conforman el STRUCT o la UNION")
    print("DESCRIBIR <nombre> mostrarar informacion segun ciertas condiciones del tipo de dato en <nombre>")
    print("SALIR para salir del simulador.")
    mtd = S.Simulador()
    while True :
        instruccion = input('<instruccion>: ')
        if instruccion == '':
            pass
        elif re.match('^ATOMICO($| )', instruccion):
            datosAtomico = instruccion.split(' ')
            mtd.addAtomo(datosAtomico[1], int(datosAtomico[2]), int(datosAtomico[3]))
        elif re.match('^STRUCT($| )', instruccion):
            datosStruct = instruccion.split(' ')
            listaT = datosStruct[2:]
            mtd.addStruct(datosStruct[1], listaT)
        elif re.match('^UNION($| )', instruccion):
            datosUnion = instruccion.split(' ')
            listaT = datosUnion[2:]
            mtd.addUnion(datosUnion[1], listaT)
        elif re.match('^DESCRIBIR($| )', instruccion):
            datosDescribir = instruccion.split(' ')
            mtd.describirTipo(datosDescribir[1])
        elif re.match('^SALIR($| )', instruccion):
            print("Gracias por interactuar conmigo, hasta luego!")
            exit()
        else :
            print("Ingrese un comando válido.")

