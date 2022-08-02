/* Cliente para prueba de los algoritmos DFS y BFS
 * sobre grafos.
 */

fun main() {
    var grafoM: Grafo = Grafo(5)
    grafoM.agregarLado(0, 3)
    grafoM.agregarLado(3, 2)
    grafoM.agregarLado(0, 1)
    grafoM.agregarLado(1, 2)
    grafoM.agregarLado(2, 4)

    grafoM.toString()

    println()

    var bfs: BFS = BFS(grafoM)
    println(bfs.buscar(0, 4))

    var dfs: DFS = DFS(grafoM)
    println(dfs.buscar(0, 4))
}