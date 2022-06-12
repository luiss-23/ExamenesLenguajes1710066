/* 
 * Programa de respuesta a pregunta 5 del examen 1
 * Autor: Luis Blanco
 * Carné: 1710066 */

/* 
 * Implementacion de clase DiagramaT la cual tendrá funciones a usar en un simulador en el que se verá si un
 * definido un lenguaje local, programas en distinto lenguajes, traductores de lenguajes e interpretes
 * se puede ejecutar un programa en una máquina
 */
public class DiagramaT(l: String) {
    var programas: MutableMap<String, String> = mutableMapOf()
    var interprete: MutableMap<String, String> = mutableMapOf()
    var traductor: MutableMap<String, Pair<String, String>> = mutableMapOf()

    var local: String = l

    /*
     * Funcion que agrega datos al mapa correspondiente dependiendo de si la instruccion es
     * DEFINIR [PROGRAMA, INTERPRETE, TRADUCTOR] 
     */
    fun definir(datos: MutableList<String>) : String {
        if (datos[1] == "PROGRAMA") {
            programas[datos[2]] = datos[3]
            return "Se definió el programa '${datos[2]}', ejecutable en '${datos[3]}'"
        } else if (datos[1] == "INTERPRETE") {
            interprete[datos[3]] = datos[2]
            return "Se definió un intérprete para '${datos[3]}', escrito en '${datos[2]}'"
        } else if (datos[1] == "TRADUCTOR") {
            traductor[datos[3]] = Pair(datos[2], datos[4])
            return "Se definió un traductor de '${datos[3]}' hacia '${datos[4]}', escrito en '${datos[2]}'"
        }
        return "La instrucción no es válida, ingrese una instrucción correcta."
    }

    /* 
     * Funcion que verifica si un programa dado se puede ejecutar en la maquina
     */
    fun ejecutar(p: String) : String {
        if (programas.keys.contains(p)) {
            if (programas[p] == local) {
                return "Si, es posible ejecutar el programa '${p}'"
            } else if (interprete.keys.contains(programas[p])) {
                if (interprete[programas[p]] == local) {
                    return "Si, es posible ejecutar el programa '${p}'"
                } else {
                    buscarTraductor(programas[p]!!, p)
                }
            } else {
                buscarTraductor(programas[p]!!, p)
            }
        } else {
            return "El programa '${p}' no está definido."
        }
        return ""
    }

    /* 
     * Funcion auxiliar de ejecutar que busca los traductores o interpretes de un lenguaje para un programa,
     * ambos datos son dados como argumento de entrada.
     */
    fun buscarTraductor(l: String, p: String) : String {
        if (traductor.keys.contains(l)) {
            if (traductor[l]!!.first == local) {
                if (traductor[l]!!.second == local) {
                    return "Si, es posible ejecutar el programa '${p}'"
                } else if (interprete.keys.contains(traductor[l]!!.second)) {
                    if (interprete[traductor[l]!!.second] == local) {
                        print("Si, es posible ejecutar el programa '${p}'")
                    } else {
                        return "No es posible ejecutar el programa '${p}'"
                    }
                } else {
                    buscarTraductor(traductor[l]!!.second, p)
                }
            } else if (interprete.keys.contains(traductor[l]!!.first)) {
                if (interprete[traductor[l]!!.first] == local) {
                    if (traductor[l]!!.second == local) {
                        return "Si, es posible ejecutar el programa '${p}'"
                    } else if (interprete.keys.contains(traductor[l]!!.second)) {
                        if (interprete[traductor[l]!!.second] == local) {
                            return "Si, es posible ejecutar el programa '${p}'"
                        } else {
                            buscarTraductor(traductor[l]!!.second, p)
                        }
                    } else {
                        buscarTraductor(traductor[l]!!.second, p)
                    }
                }
            } else {
                buscarTraductor(traductor[l]!!.first, p)
            }
        } else {
            return "No es posible ejecutar el programa '${p}'"
        }
        return ""
    }
}