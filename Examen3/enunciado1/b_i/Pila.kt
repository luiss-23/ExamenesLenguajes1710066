class Pila<T>() : Secuencia<T> {

    var pila: MutableList<T> = mutableListOf()

    /* Funcion para agregar elementos a la pila, los elementos se 
     * agregran al inicio de la lista.
     */
    override fun agregar(e: T) {
        pila.add(0, e)
    }

    /* Funcion para remover elementos de la pila, el elemento que se 
     * remueve es el ultimo que se agrego.
     */
    override fun remover() : T {
        if (pila.size == 0) {
            throw RuntimeException("La pila no contiene elementos.")
        }
        var elemToRemove: T = pila[0]
        pila.removeAt(0)
        return elemToRemove
    }

    // Funcion para verificar si una pila esta vacia o no
    override fun vacio() : Boolean {
        if (pila.size == 0) {
            return true
        }
        return false
    }

    // Funcion para mostrar la pila como un string
    override fun toString() : String {
        var strPila = "\n"
        for (element in pila) {
            strPila += element.toString() + "\n"
        }
        return strPila
    }
}