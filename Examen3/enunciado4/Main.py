""" Implementador simulador del Handler creado para 
    manejar tablas virtuales de metodos """

import re
import Handler as h
if __name__ == '__main__' :
    simulador = h.Handler()
    while True :
        instruccion = input('<instruccion>: ')
        if instruccion == '':
            pass
        elif re.match('^CLASS($| )', instruccion):
            datosEval = instruccion.split(' ')
            print(datosEval)
            if ':' in datosEval:
                nombreClase = datosEval[1]
                nombreSuper = datosEval[3]
                listaMetodos = datosEval[4:]
                simulador.class_(nombreClase, nombreSuper, listaMetodos)
            else: 
                nombreClase = datosEval[1]
                listaMetodos = datosEval[2:]
                simulador.class_(nombreClase, None, listaMetodos)
        elif re.match('^DESCRIBIR($| )', instruccion):
            datosEval = instruccion.split(' ')
            nombreClase = datosEval[1]
            simulador.describir(nombreClase)
        elif re.match('^SALIR($| )', instruccion):
            print("Gracias por interactuar conmigo, hasta luego!")
            exit()
        else :
            print("Ingrese un comando válido.")