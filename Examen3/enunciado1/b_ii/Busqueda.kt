/* Implementacion de los algoritmos de busqueda para buscar
 * distancias de un vertice a otro en grafos
 */

/* Clase abstracta Busqueda donde se define la funcion
 * buscar, la cual sera extendida por las clases BFS y DFS
 */
abstract class Busqueda {
    abstract fun buscar(d: Int, h: Int) : Int
}

// Clases de datos que contienen informacion relevante para cada uno de 
// los algoritmos de busqueda.
data class InformacionBFS(var distancia: Int, var explorado: Boolean)
data class InformacionDFS(var d: Int, var p: Int, var exp: Boolean, var ti: Int, var tf: Int)

/* Clase BFS que extiende la clase abstracta Busqueda e implementa el 
 * algoritmo de busqueda BFS
 */
class BFS(val g: Grafo) : Busqueda() {
    override fun buscar(d: Int, h: Int) : Int {
        if (d >= g.cantidadVertices || h >= g.cantidadVertices || d < 0 || h< 0) {
            throw RuntimeException("El vertice ${d} o ${h} no pertenecen al grafo.")
        }

        var informacionVertices = MutableList(g.cantidadVertices) {InformacionBFS(-1, false)}
        var q: MutableList<Int> = mutableListOf()

        informacionVertices[d].distancia = 0
        informacionVertices[d].explorado = true
        q.add(d)

        while (q.size != 0) {
            var currentV = q.removeAt(0)
            for (v in g.grafo[currentV]) {
                if (!informacionVertices[v].explorado) {
                    informacionVertices[v].distancia = informacionVertices[currentV].distancia + 1
                    q.add(v)
                }
            }

            informacionVertices[currentV].explorado = true
        }

        return informacionVertices[h].distancia
    }
}

/* Clase DFS que extiende la clase abstracta Busqueda e implementa el 
 * algoritmo de busqueda DFS
 */
class DFS(val g: Grafo) : Busqueda() {
    var tiempo: Int = 0 // variable global de dfs
    var informacionVertices = MutableList(g.cantidadVertices) {InformacionDFS(-1, -1, false, 0, 0)}

    override fun buscar(d: Int, h: Int) : Int {
        if (d >= g.cantidadVertices || h >= g.cantidadVertices || d < 0 || h< 0) {
            throw RuntimeException("El vertice ${d} o ${h} no pertenecen al grafo.")
        }
        informacionVertices[d].d = 0
        dfsVisit(d)

        var distanciaH: Int = informacionVertices[h].d

        informacionVertices = MutableList(g.cantidadVertices) {InformacionDFS(-1, -1, false, 0, 0)}

        return distanciaH
    }

    fun dfsVisit(v: Int) {
        tiempo += 1
        informacionVertices[v].ti = tiempo
        informacionVertices[v].exp = true

        for (vf in g.grafo[v]) {
            if (!informacionVertices[vf].exp) {
                informacionVertices[vf].p = v
                informacionVertices[vf].d = informacionVertices[v].d + 1
                dfsVisit(vf)
            }
        }

        tiempo += 1
        informacionVertices[v].tf = tiempo
    }
}
