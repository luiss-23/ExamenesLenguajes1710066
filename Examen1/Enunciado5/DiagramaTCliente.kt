/*
 * Programa cliente encargado de verificar el funcionamiento del simulador del Diagrama T para saber
 * si un programa es ejecutable en una maquina. 
 */

fun main(args: Array<String>) {
    if (args.size != 0) {
        println("No se deben introducir argumentos de entrada. La línea de comando debe ser:")
        println(">./DiagramaT.sh")
        return
    }
    print("Introduzca su nombre: ")
    val usuario: String = readLine()!!
    println("\nHola ${usuario}! Bienvenido al simulador del Diagrama T.")
    println("Este simulador fue creado por el estudiante de Ing. en Computación Luis Blanco.")
    println("Espero que te diviertas haciendo uso de él! Ahora te dejo los comandos y algunos ejemplos")
    println("mediante los cuales puedes interactuar conmigo:")
    println("Se pueden manejar programas, traductores e interpretes de la siguiente forma:")
    println("PROGRAMA <nombre> <lenguaje>")
    println("INTERPRETE <lenguaje_base> <lenguaje>")
    println("TRADUCTOR <lenguaje_base> <lenguaje_origen> <lenguaje_destino>")
    println("Se puede hacer uso de las siguientes instrucciones:")
    println("DEFINIR <tipo> [<argumentos>] : DEFINIR PROGRAMA kateBishop Python3")
    println("EJECUTABLE <nombre>           : EJECUTABLE kateBishop")
    println("SALIR                         : SALIR")

    print("Introduza el lenguaje local que ejecutara la máquina: ")
    val lenguajeLocal: String = readLine()!!
    println()
    if (lenguajeLocal == "") {
        println("Se debe introducir un lenguaje local para la maquina.")
        return
    }
    val diagramaT = DiagramaT(lenguajeLocal)

    while (true) {
        print("Ingrese la instruccion a relizar: ")
        println()
        val instruccion: String = readLine()!!
        val patternD = Regex("^DEFINIR($| )")
        val patternE = Regex("^EJECUTABLE($| )")
        val patternS = Regex("^SALIR($| )")
        if (instruccion == "") {
            continue
        }

        if (patternD.containsMatchIn(instruccion)){
            val datosInstruccion: Array<String> = instruccion.split(" ").toTypedArray()
            if (datosInstruccion[1] == "PROGRAMA") {
                if (datosInstruccion.size != 4) {
                    println("La instrucción no se ha introducido correctamente, introduzcala nuevamente con el formato correcto.")
                    continue
                } else {
                    println(diagramaT.definir(datosInstruccion.toMutableList()))
                }
            } else if (datosInstruccion[1] == "INTERPRETE") {
                if (datosInstruccion.size != 4) {
                    println("La instrucción no se ha introducido correctamente, introduzcala nuevamente con el formato correcto.")
                    continue
                } else {
                    println(diagramaT.definir(datosInstruccion.toMutableList()))
                }
            } else if (datosInstruccion[1] == "TRADUCTOR") {
                if (datosInstruccion.size != 5) {
                    println("La instrucción no se ha introducido correctamente, introduzcala nuevamente con el formato correcto.")
                    continue
                } else {
                    println(diagramaT.definir(datosInstruccion.toMutableList()))
                }
            } else { 
                println("Solamente se pueden definir PROGRAMAS, TRADUCTORES o INTERPRETES, intentelo de nuevo.")
                continue
            }
        } else if (patternE.containsMatchIn(instruccion)) {
            val datosInstruccion: Array<String> = instruccion.split(" ").toTypedArray()
            if (datosInstruccion.size != 2) {
                println("La instrucción no se ha introducido correctamente, introduzcala nuevamente con el formato correcto.")
                continue
            } else {
                println(diagramaT.ejecutar(datosInstruccion[1]))
            }
        } else if (patternS.containsMatchIn(instruccion)) {
            println("Espero te hayas divertido, regresa pronto!")
            return
        } else {
            println("No ha introducido una instrucción válida, inténtelo de nuevo.")
        }
    }
}