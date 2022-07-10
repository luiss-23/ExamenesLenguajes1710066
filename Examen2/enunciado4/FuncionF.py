""" Implementacion de las diferentes funciones
    f del enunciado 4 
    Autor: Luis Carlos Blanco
    Carné: 1710066
"""

""" Para obtener los rangos en los que se define la funcion, obtenemos los
    siguientes valores
    
    alpha = ((X+Y)mod 5)+3
    beta = ((Y+Z)mod 5)+3 
    
    donde X = 0, Y = 6 e Z = 6, entonces
    alpha = 4
    beta = 5
"""

# Version recursiva de la funcion f
def f_recursiva(n: int) :
    """ Funcion f escrita de forma recursiva
        Recibe el n y retorna como resultado f(n)
    """
    if 0 <= n and n < 20 :
        return n
    else:
        return sum([f_recursiva(n - 5 * i) for i in range(1, 5)])

# Version recursiva de cola de la funcion f
def f_recursiva_cola(n: int) :
    """ Funcion f escrita de forma recursiva de cola
        Recibe el n y retorna como resultado f(n)
    """
    return f_recursiva_cola_aux(n, [i for i in range(21)], 19)

def f_recursiva_cola_aux(n: int, valFn: list, cb: int) :
    """ Funcion f auxiliar de f_recursiva_cola
        Recibe el n, una lista con los casos base y un numero base,
        retorna como resultado f(n)
    """
    if 0 <= n and n < 20 :
        return valFn[n]
    elif n == cb + 1 :
        return sum([valFn[20 - 5 * i] for i in range(1, 5)])
    else :
        valFn[-1] = sum([valFn[20 - 5 * i] for i in range(1, 5)])
        for i in range(1,21) :
            valFn[i - 1] = valFn[i]

        return f_recursiva_cola_aux(n, valFn, cb + 1)

# Version iterativa de la funcion f
def f_iterativa(n: int) :
    """ Funcion f escrita de forma iterativa
        Recibe el n y retorna como resultado f(n)
    """
    if 0 <= n and n < 20 :
        return n
    else:
        sum = 0
        for i in range(1, 5) :
            sum += f_iterativa(n - 5 * i)

    return sum
