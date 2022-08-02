/* Se implementa la Inteface Secuencia de la cual van a extender
 * Pila y Cola, con las funciones que deben de manejar estas subclases.
 */

interface Secuencia<T> {
    // Funcion para agregar elementos a la secuencia
    fun agregar(e: T) 

    // Funcion para remover elementos de una secuencia
    fun remover() : T

    //  Funcion para mostrar si una secuencia es vacia
    fun vacio() : Boolean
}