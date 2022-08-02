class Cola<T>() : Secuencia<T> {

    var cola: MutableList<T> = mutableListOf()

    override fun agregar(e: T) {
        cola.add(e)
    }

    override fun remover() : T {
        if (cola.size == 0) {
            throw RuntimeException("La cola no contiene elementos.")
        }
        var elemToRemove: T = cola[0]
        cola.removeAt(0)
        return elemToRemove
    }

    override fun vacio() : Boolean {
        if (cola.size == 0) {
            return true
        }
        return false
    }

    override fun toString() : String {
        var strCola = ""
        for (element in cola) {
            strCola += element.toString() + ", "
        }
        return strCola
    }
}