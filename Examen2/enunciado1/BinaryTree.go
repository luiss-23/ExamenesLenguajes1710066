/* Programa que implementa un arbol binario y algunas funciones para verificar que es
un maxHeap, el recorrido pre y post order del arbol.
Autor: Luis Carlos Blanco
Carne: 1710066 */

package main

import "fmt"

type Hoja struct {
	dato          int
	ramaIzquierda *Hoja
	ramaDerecha   *Hoja
}

func (raiz *Hoja) recorridoPreOrder(array *[]int) *[]int {
	if raiz != nil {
		*array = append(*array, raiz.dato)
		raiz.ramaIzquierda.recorridoPreOrder(array)
		raiz.ramaDerecha.recorridoPreOrder(array)
	}
	return array
}

func (raiz *Hoja) recorridoPostOrder(array *[]int) *[]int {
	if raiz != nil {
		raiz.ramaIzquierda.recorridoPostOrder(array)
		raiz.ramaDerecha.recorridoPostOrder(array)
		*array = append(*array, raiz.dato)
	}
	return array
}

func esMaxHeap(array *[]int, i, n int) bool {
	if i >= int((n-1)/2) {
		return true
	}

	if (*array)[i] >= (*array)[2*i+1] && (*array)[i] >= (*array)[2*i+2] &&
		esMaxHeap(array, 2*i+1, n) && esMaxHeap(array, 2*i+2, n) {
		return true
	}

	return false
}

func esMaxHeapSimetrico(arr1, arr2 *[]int) {
	if len((*arr1)) != len((*arr2)) {
		fmt.Println("Los arboles no tienen el mismo tamanyo.")
		return
	}

	for i := 0; i < len((*arr1))-1; i++ {
		if (*arr1)[i] != (*arr2)[i] {
			fmt.Println("No es MaxHeap simétrico.")
			return
		}
	}

	fmt.Println("Es MaxHeap simétrico.")
}

func main() {
	maxHeap := Hoja{9, nil, nil}
	maxHeap.ramaIzquierda = &Hoja{8, nil, nil}
	maxHeap.ramaDerecha = &Hoja{8, nil, nil}
	maxHeap.ramaIzquierda.ramaIzquierda = &Hoja{7, nil, nil}
	maxHeap.ramaIzquierda.ramaDerecha = &Hoja{6, nil, nil}
	maxHeap.ramaDerecha.ramaIzquierda = &Hoja{6, nil, nil}
	maxHeap.ramaDerecha.ramaDerecha = &Hoja{7, nil, nil}

	var recorridoPre []int
	var recorridoPost []int
	maxHeap.recorridoPreOrder(&recorridoPre)
	maxHeap.recorridoPostOrder(&recorridoPost)
	esmax := esMaxHeap(&recorridoPre, 0, len(recorridoPre)-1)
	fmt.Println(recorridoPre)
	fmt.Println(recorridoPost)
	fmt.Println(esmax)
	esMaxHeapSimetrico(&recorridoPre, &recorridoPost)
}
