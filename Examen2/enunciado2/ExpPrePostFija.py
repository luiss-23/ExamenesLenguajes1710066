""" Se implementa una libreria con funciones para el manejo de expresiones pre y 
    postfijas 
    Autor: Luis Carlos Blanco.
    Carne: 1710066
"""

def conjuncion(val1: bool, val2: bool) :
    """ Funcion usada para evaluar una conjuncion entre
        dos booleanos.
        Recibe dos operandos booleanos y retorna el resultado
        de la evaluacion.
    """
    return val1 and val2

def disyuncion(val1: bool, val2: bool) :
    """ Funcion usada para evaluar una disyuncion entre
        dos booleanos.
        Recibe dos operandos booleanos y retorna el resultado
        de la evaluacion.
    """
    return val1 or val2

def implicacion(val1: bool, val2: bool) :
    """ Funcion usada para evaluar una implicacion entre
        dos booleanos.
        Recibe dos operandos booleanos y retorna el resultado
        de la evaluacion.
    """
    return not(val1) or val2

def negacion(val1: bool) :
    """ Funcion usada para evaluar la negacion de un booleano
        Recibe el booleando y retorna su negado.
    """
    return not(val1)

def evaluacionPrefija(exp: str) :
    """ Funcion usada para evaluar una expresion escrita en orden prefijo
        Recibe la expresion y retorna como resultado la evaluacion de la misma.
    """
    arrExp = exp.split(" ")

    arrOperadores = []
    arrOperandos = []

    for i in range(0, len(arrExp)) :
        if arrExp[i] == "true" or arrExp[i] == "false" :
            if arrExp[i] == "true" :
                arrOperandos.append(True)
            elif arrExp[i] == "false" :
                arrOperandos.append(False)

            while (len(arrOperandos) != 1) :
                valorB = arrOperandos.pop()
                valorA = arrOperandos.pop()

                operador = arrOperadores.pop()

                if operador == "&" :
                    resultado = conjuncion(valorA, valorB)
                elif operador == "|" :
                    resultado = disyuncion(valorA, valorB)
                elif operador == "=>" :
                    resultado = implicacion(valorA, valorB)
                elif operador == "^" :
                    resultado = negacion(valorA)
                    arrOperandos.append(resultado)
                    arrOperandos.append(valorB)
                    continue
                
                arrOperandos.append(resultado)

        elif arrExp[i] == "&" or arrExp[i] == "|" or arrExp[i] == "=>" or arrExp[i] == "^" :
            arrOperadores.append(arrExp[i])

    return arrOperandos.pop()

def mostrarEvaluacionPrefija(exp: str) :
    """ Funcion usada para mostra una expresion escrita en orden prefijo
        Recibe la expresion y retorna como resultado la expresion en orden infijo.
    """
    arrExp = exp.split(" ")     

    sizeExp = len(arrExp) - 1
    strExp = ""
    infixExp = []
    while sizeExp >= 0 :
        if arrExp[sizeExp] == "true" or arrExp[sizeExp] == "false" :
            infixExp.append(arrExp[sizeExp])
            sizeExp -= 1
        else:
            if arrExp[sizeExp] == "&":
                strExp = infixExp.pop() + ' ' + arrExp[sizeExp] + ' ' + infixExp.pop()
                infixExp.append(strExp)
                sizeExp -= 1
            elif arrExp[sizeExp] == "|":
                strExp = infixExp.pop() + ' ' + arrExp[sizeExp] + ' ' + infixExp.pop()
                infixExp.append(strExp)
                sizeExp -= 1
            elif arrExp[sizeExp] == "=>":
                strExp = '(' + infixExp.pop() + ' ' + arrExp[sizeExp] + ' ' + infixExp.pop() + ')'
                infixExp.append(strExp)
                sizeExp -= 1
            elif arrExp[sizeExp] == "^":
                strExp = arrExp[sizeExp] + infixExp.pop()
                infixExp.append(strExp)
                sizeExp -= 1

    return infixExp.pop()

def evaluacionPostfija(exp: str) :
    """ Funcion usada para evaluar una expresion escrita en orden postfijo
        Recibe la expresion y retorna como resultado la evaluacion de la misma.
    """
    
    arrExp = exp.split(" ")
    evExp = []

    for i in range(0, len(arrExp)) :
        if arrExp[i] == "true" or arrExp[i] == "false" :
            if arrExp[i] == "true" :
                evExp.append(True)
            elif arrExp[i] == "false" :
                evExp.append(False)
        else:
            if arrExp[i] == "&" :
                op1 = evExp.pop()
                op2 = evExp.pop()
                res = conjuncion(op2, op1)
            elif arrExp[i] == "|" :
                op1 = evExp.pop()
                op2 = evExp.pop()
                res = disyuncion(op2, op1)
            elif arrExp[i] == "=>" :
                op1 = evExp.pop()
                op2 = evExp.pop()
                res = implicacion(op2, op1)
            elif arrExp[i] == "^" :
                op1 = evExp.pop()
                res = negacion(op1)
            
            evExp.append(res)

    return evExp.pop()

def mostrarEvaluacionPostfija(exp: str) :
    """ Funcion usada para mostra una expresion escrita en orden postfijo
        Recibe la expresion y retorna como resultado la expresion en orden infijo.
    """
    arrExp = exp.split(" ")     

    i = 0
    strExp = ""
    infixExp = []

    for i in range(0, len(arrExp)) :
        if arrExp[i] == "true" or arrExp[i] == "false" :
            infixExp.insert(0, arrExp[i])
        else :
            if arrExp[i] == "&":
                op1 = infixExp.pop(0)
                op2 = infixExp.pop(0)
                strExp = op2 + ' ' + arrExp[i] + ' ' + op1
                infixExp.insert(0, strExp)
            elif arrExp[i] == "|":
                op1 = infixExp.pop(0)
                op2 = infixExp.pop(0)
                strExp = op2 + ' ' + arrExp[i] + ' ' + op1
                infixExp.insert(0, strExp)
            elif arrExp[i] == "=>":
                op1 = infixExp.pop(0)
                op2 = infixExp.pop(0)
                strExp = '(' + op2 + ' ' + arrExp[i] + ' ' + op1 + ')'
                infixExp.insert(0, strExp)
            elif arrExp[i] == "^":
                op1 = infixExp.pop(0)
                strExp = arrExp[i] + op1
                infixExp.insert(0, strExp)

    return infixExp.pop(0)
