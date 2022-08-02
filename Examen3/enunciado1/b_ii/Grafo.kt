/* Implementacion del tipo de datos Grafo y dos algoritmos
 * de busqueda sobre el mismo.
 */

/* Clase donde se implementa un grafo y funciones para 
 * agregar lados al grafo y mostrarlo como string.
 */
class Grafo(val n: Int) {
    // grafo: representa un grafo con listas de adayacencias.
    // cantidadDeVertices guarda la cantidad de vertices del grafo.
    var grafo: MutableList<MutableList<Int>> = MutableList(n) {mutableListOf()}
    var cantidadVertices: Int = n

    /* Funcion en la que se agrega un lado al grafo, en caso de que
     * uno de los vertices no pertenezca al grafo, se lanza una runtime
     */
    fun agregarLado(vi: Int, vf: Int) {
        if (vi >= n || vf >= n || vi < 0 || vf < 0) {
            throw RuntimeException("El vertice ${vi} o ${vf} no pertenecen al grafo.")
        } else if (grafo[vi].contains(vf)) {
            throw RuntimeException("Ya existe el lado (${vi}, ${vf}).")
        }

        grafo[vi].add(vf)
    }

    // Funcion para mostrar el contenido del grafo.
    override fun toString() : String {
        for (v in 0..(grafo.size - 1)) {
            print("Vertice ${v}: ")
            println(grafo[v].toString())
        }
        return ""
    }
}