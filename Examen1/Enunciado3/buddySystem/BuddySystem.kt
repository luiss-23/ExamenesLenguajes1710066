/* 
 * Implementacion del BuddySystem
 * Autor: Luis Carlos Blanco
 * Carné: 17-10066
 */

import kotlin.math.*

public class Bloque(val i: Int, val f: Int) {
    var direcciones: Pair<Int, Int> = Pair(i, f)
    var capacidad: Int = f - i + 1

    fun direccionInicial() : Int {
        return direcciones.first
    }

    fun direccionFinal() : Int {
        return direcciones.second
    }

    fun divisionBloque() : Pair<Bloque, Bloque> {
        var direccionI: Int = direccionInicial() + ((direccionFinal() - direccionInicial()) / 2)
        var direccionF: Int = direccionInicial() + ((direccionFinal() - direccionInicial() + 1) / 2)

        return Pair(Bloque(direccionInicial(), direccionI), Bloque(direccionF, direccionFinal()))
    }

    override fun toString() : String {
        return "[dI: ${i}, dF: ${f}]"
    }
}
 
fun log2(n: Int): Double {
    return ln(n.toDouble()) / ln(2.0)
}

public class BuddySystem(val bloques: Int) {
    var bloquesOcupados: MutableMap<String, Bloque> = mutableMapOf()
    var numeroDeBloques: Int = floor(log2(bloques)).toInt()
    var memoriaLibre: MutableList<MutableList<Bloque>> = MutableList(numeroDeBloques+1) { mutableListOf() }
        
    init {
        var basePotencia: Double = 2.0
        var potencia = basePotencia.pow(numeroDeBloques) - 1
        memoriaLibre[memoriaLibre.size - 1].add(Bloque(0, potencia.toInt()))
    }

    fun reservarEspacio(nombre: String, cantidad: Int) : String {
        if (bloquesOcupados.contains(nombre)) {
            return "${nombre} ya ha sido reservado."
        }

        var ubicacionBloque: Int = ceil(log2(cantidad)).toInt()

        if (memoriaLibre[ubicacionBloque].size > 0) {
            var bloque: Bloque = memoriaLibre[ubicacionBloque].removeAt(0)
            bloquesOcupados[nombre] = bloque 
            return "El bloque ${nombre} ha sido reservado."
        }

        var i: Int = ubicacionBloque + 1
        while (i != memoriaLibre.size) {
            if (memoriaLibre[i].size > 0) {
                break
            }
            i += 1
        }
        if (memoriaLibre.size == i) {
            return "No se puede resrevar el bloque ${nombre} ya que no hay memoria suficiente."
        }

        var dividirBloque: Bloque = memoriaLibre[i].removeAt(0)
        while (i - 1 >= ubicacionBloque) {
            var bloquesDivididos: Pair<Bloque, Bloque> = dividirBloque.divisionBloque()
            memoriaLibre[i - 1].add(bloquesDivididos.second)
            dividirBloque = bloquesDivididos.first
            i -= 1
        }
        bloquesOcupados[nombre] = dividirBloque

        return "El bloque ${nombre} ha sido reservado."
    }

    fun liberar(nombre: String) : String {
        var liberarBloque: Bloque? = bloquesOcupados.get(nombre)
        if (liberarBloque == null) {
            return "No existe el bloque ${nombre}."
        }
        var ubicacionBloque: Int = ceil(log2(liberarBloque.capacidad)).toInt()
        memoriaLibre[ubicacionBloque].add(liberarBloque)

        unionBloque(liberarBloque)
        bloquesOcupados.remove(nombre)
        return "El bloque con nombre ${nombre} ha sido liberado."
    }

    fun unionBloque(bloque: Bloque?) {
        if (bloque == null) {
            return
        } else {
            var ubicacionBloque: Int = ceil(log2(bloque.capacidad)).toInt()
            var buddyNumber: Int = bloque.direccionInicial() / bloque.capacidad

            var direccionBuddy: Int
            if (buddyNumber % 2 != 0) {
                direccionBuddy = bloque.direccionInicial() - bloque.capacidad
            } else {
                direccionBuddy = bloque.direccionInicial() + bloque.capacidad
            }
            var bloqueUnido: Bloque? = null
            var listaBloques = memoriaLibre[ubicacionBloque]
            for (bloques in 0..(listaBloques.size - 1)) {
                if (listaBloques[bloques].direccionInicial() == direccionBuddy) {
                    if (buddyNumber % 2 == 0) {
                        bloqueUnido = Bloque(bloque.direccionInicial(), listaBloques[bloques].direccionFinal())
                        memoriaLibre[ubicacionBloque + 1].add(bloqueUnido)
                    } else {
                        bloqueUnido = Bloque(listaBloques[bloques].direccionInicial(), bloque.direccionFinal())
                        memoriaLibre[ubicacionBloque + 1].add(bloqueUnido)
                    }
                    memoriaLibre[ubicacionBloque].removeLast()
                    memoriaLibre[ubicacionBloque].removeAt(bloques)
                    break
                }
            }
            unionBloque(bloqueUnido)
        }
    }

    fun mostrar() : String {
        var bloquesLibres: MutableList<Bloque> = mutableListOf()
        for (element in memoriaLibre) {
            for (bloque in element) {
                bloquesLibres.add(bloque)
            }
        }

        bloquesLibres.sortedBy { it.direccionInicial() }
        println("A continuacion se imprimen los bloques que se encuentran libres en la memoria:")
        for (bloques in bloquesLibres) {
            println(bloques.toString())
        }
        println("Ahora se imprimen los bloques que tienen datos con el formato <nombre, bloque>:")
        bloquesOcupados.forEach { entry ->
            println("${entry.key} : ${entry.value}")
        }
        return ""
    }
}
