fun isNumber(s: String): Boolean {
    return when(s.toIntOrNull())
    {
        null -> false
        else -> true
    }
}

fun main(args: Array<String>) {
    if (args.size != 1) {
        println("Se debe introducir un solo argumento como entrada. La línea de comando debe ser:")
        println(">./BuddyClient.sh [n]")
        println("Donde n es la cantidad de bloques que manejara el simulador.")
        return
    }
    print("Introduzca su nombre: ")
    val usuario: String = readLine()!!
    println("\nHola ${usuario}! Bienvenido al simulador del BuddySystem.")
    println("Este simulador fue creado por el estudiante de Ing. en Computación Luis Blanco.")
    println("Espero que te diviertas haciendo uso de él! Ahora te dejo los comandos y algunos ejemplos")
    println("mediante los cuales puedes interactuar conmigo:")
    println("RESERVAR <nombre> <cantidad> : RESERVAR lenguajesEsIncreible 5")
    println("LIBERAR <nombre>             : LIBERAR lenguajesEsIncreible")
    println("MOSTRAR                      : MOSTRAR")
    println("SALIR                        : SALIR")

    val buddySystem = BuddySystem(args[0].toInt())

    while (true) {
        print("Ingrese la instruccion a relizar: ")
        println()
        val instruccion: String = readLine()!!
        val patternR = Regex("^RESERVAR($| )")
        val patternL = Regex("^LIBERAR($| )")
        val patternM = Regex("^MOSTRAR($| )")
        val patternS = Regex("^SALIR($| )")
        if (instruccion == "") {
            continue
        }

        if (patternR.containsMatchIn(instruccion)){
            val datosInstruccion: Array<String> = instruccion.split(" ").toTypedArray()
            if (datosInstruccion.size != 3) {
                println("La instrucción no se ha introducido correctamente, introduzcala nuevamente con el formato correcto.")
                continue
            } else {
                if (isNumber(datosInstruccion[2])) {
                    println(buddySystem.reservarEspacio(datosInstruccion[1], datosInstruccion[2].toInt()))
                } else {
                    println("Los datos de la instruccion no son correctos, introduzcala nuevamente con los datos correctos.")
                    continue
                }
            }
        } else if (patternL.containsMatchIn(instruccion)) {
            val datosInstruccion: Array<String> = instruccion.split(" ").toTypedArray()
            if (datosInstruccion.size != 2) {
                println("La instrucción no se ha introducido correctamente, introduzcala nuevamente con el formato correcto.")
                continue
            } else {
                println(buddySystem.liberar(datosInstruccion[1]))
            }
        } else if (patternM.containsMatchIn(instruccion)) {
            buddySystem.mostrar()
        } else if (patternS.containsMatchIn(instruccion)){
            println("Espero que hayas pasado un buen rato en le simulador, espero verte pronto!")
            return
        } else {
            println("No ha introducido una instrucción válida, inténtelo de nuevo.")
        }
    }
}