/* 
 * Implementacion del BuddySystem
 * Autor: Luis Carlos Blanco
 * Carné: 17-10066
 */

import kotlin.math.*

/*
 * Clase Bloque que va a definir un objeto de tipo Bloque, el cual sera util para la implementacion
 * del buddy system, tambien se implementa algunas operaciones sobre bloques.
 */
public class Bloque(val i: Int, val f: Int) {
    /* Variables:
     * capacidad: nos dira cual es la capacidad que tiene un bloque que tiene un bloque con direccion
     * inicial y final i y j respectivamente.
     * direcciones: par que contendra las direcciones inicial y fional de un obejto de tipo Bloque.
     */
    var direcciones: Pair<Int, Int> = Pair(i, f)
    var capacidad: Int = f - i + 1

    /* 
     * Funcion direccionInicial que nos devolvera la direccion inicial de un bloque
     */
    fun direccionInicial() : Int {
        return direcciones.first
    }

    /* 
     * Funcion direccionFinal que nos devolvera la direccion final de un bloque
     */
    fun direccionFinal() : Int {
        return direcciones.second
    }

    /* 
     * Funcion divisionBloque que dado un bloque nos devolvera un par con dos bloques que resultaron de la 
     * division del bloque con el que se llama a la funcion.
     */
    fun divisionBloque() : Pair<Bloque, Bloque> {
        var direccionI: Int = direccionInicial() + ((direccionFinal() - direccionInicial()) / 2)
        var direccionF: Int = direccionInicial() + ((direccionFinal() - direccionInicial() + 1) / 2)

        return Pair(Bloque(direccionInicial(), direccionI), Bloque(direccionF, direccionFinal()))
    }

    /* 
     * Sobrecarga de la funcion toString() para mostra como string un elemento de tipo bloque.
     */
    override fun toString() : String {
        return "[dI: ${i}, dF: ${f}]"
    }
}

/* 
 * Funcion log2 que recibe un entero y nos devuelve el logaritmo en base 2 de dicho
 * entero
 */
fun log2(n: Int): Double {
    return ln(n.toDouble()) / ln(2.0)
}


/*
 * Clase BuddySystem que implementara el sistema buddy system para almacenar datos dado un numero
 * de bloques.
 */
public class BuddySystem(val bloques: Int) {
    /* Variables:
     * bloqueOcupados: Diccionario que llevara los bloques ocupados del sistema junto con su valor asociado.
     * numeroDeBloques: Entero que almacenara la cantidad de bloques que manejara el sistema.
     * memoriaLibre: lista de listas que contendra los bloques que aun no han sido ocupados.
     */
    var bloquesOcupados: MutableMap<String, Bloque> = mutableMapOf()
    var numeroDeBloques: Int = floor(log2(bloques)).toInt()
    var memoriaLibre: MutableList<MutableList<Bloque>> = MutableList(numeroDeBloques+1) { mutableListOf() }
        
    init {
        var basePotencia: Double = 2.0
        var potencia = basePotencia.pow(numeroDeBloques) - 1
        memoriaLibre[memoriaLibre.size - 1].add(Bloque(0, potencia.toInt()))
    }

    /* 
     * Funcion que se encargara de reservar un espacio en el sistema para almacenar el bloque 
     * nombre y se especifica la cantidad de memoria que requiere el bloque.
     * En primer lugar se ubica el bloque libre en el que se puede almacenar el bloque dado,
     * en caso de que no haya bloques libres en la ubicacion que corresponde, se procede a buscar 
     * un bloque libre cuyo tamanio sea mayor que el tamanio requerido. En caso que no se consigan 
     * bloques disponibles para la cantidad de memoria requerida, entonces no se puede agregar el elemento.
     */
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

    /* 
     * Funcion que libera el bloque con nombre nombre y lo deja disponible para hacer uso de el y 
     * poder almacenar otro bloque cuando sea requerido. En caso de que el nombre dado no exista entonces 
     * no se libera ningun bloque.
     */
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

    /* 
     * Funcion auxiliar de la funcion liberar, la cual se encargara de unir el bloque que se esta liberando 
     * con uno de los bloques libres
     */
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

    /* 
     * Funcion que muestra como se encuentra el buddy system en el momento que el usuario lo pida,
     * muestra los bloques libres y los bloques ocupados junto con sus datos.
     */
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
