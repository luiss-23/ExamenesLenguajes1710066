""" Implementacion del simulador de operaciones con 
    expresiones pre y post fijas.
    Autor: Luis Carlos Blanco
    Carne: 1710066 """

import re
from ExpPrePostFija import *

if __name__ == '__main__' :
    print("Bienvenido al simulador de evaluación de operaciones en orden pre y")
    print("post fijo. Puedes interactuar conmigo mediante los siguientes comandos:")
    print("EVAL <orden> <expresion>, donde <orden> debe ser PRE o POST y <expresion> es la\nexpresion que se quiere evaluar.")
    print("MOSTRAR <orden> <expresion>, donde <orden> es igual que el comando anterior y\n<expresion> es la expresion que se quiere mostrar.")
    print("SALIR para salir del simulador.")
    while True :
        instruccion = input('<instruccion>: ')
        if instruccion == '':
            pass
        elif re.match('^EVAL($| )', instruccion):
            datosEval = instruccion.split(' ')
            print(datosEval)
            ordenEval = datosEval[1]
            if ordenEval != 'PRE' and ordenEval != 'POST' :
                print("Ingrese un orden válido, PRE o POST")
                continue
            else:
                expresionEval = datosEval[2:]
                print(expresionEval)
                strExpresion = ' '.join(expresionEval)
                print(strExpresion)
                if ordenEval == 'PRE' :
                    print(evaluacionPrefija(strExpresion))
                else :
                    print(evaluacionPostfija(strExpresion))
        elif re.match('^MOSTRAR($| )', instruccion):
            datosEval = instruccion.split(' ')
            ordenEval = datosEval[1]
            if ordenEval != "PRE" and ordenEval != "POST" :
                print("Ingrese un orden válido, PRE o POST")
                continue
            else:
                expresionEval = datosEval[2:]
                strExpresion = ' '.join(expresionEval)
                if ordenEval == "PRE" :
                    print(mostrarEvaluacionPrefija(strExpresion))
                else :
                    print(mostrarEvaluacionPostfija(strExpresion))
        elif re.match('^SALIR($| )', instruccion):
            print("Gracias por interactuar conmigo, hasta luego!")
            exit()
        else :
            print("Ingrese un comando válido.")

