package main

import (
	"fmt"
)

type ChurchNumerals interface {
	sucesor()
	churchToNatural()
	naturalToChurch()
	add()
	mult()
}

type Church struct {
	numeroChurch *Church
}

func sucesor(n *Church) *Church {
	succ := new(Church)
	succ.numeroChurch = n
	return succ
}

func churchToNatural(n *Church) int {
	var natural int
	var current = n
	for current.numeroChurch != nil {
		natural += 1
		current = current.numeroChurch
	}
	return natural
}

func naturalToChurch(n int) Church {
	churchNumber := new(Church)
	for n > 0 {
		churchNumber = sucesor(churchNumber)
		n -= 1
	}
	return *churchNumber
}

func add(n, m *Church) Church {
	if m.numeroChurch == nil {
		return *n
	} else {
		suma := churchToNatural(n) + churchToNatural(m)
		res := naturalToChurch(suma)
		return res
	}
}

func mult(n, m *Church) Church {
	if m.numeroChurch == nil {
		return *m
	} else {
		mul := churchToNatural(n) * churchToNatural(m)
		res := naturalToChurch(mul)
		return res
	}
}

func main() {
	var x Church = naturalToChurch(3)
	var y Church = naturalToChurch(0)
	suma := add(&x, &y)
	multiplicacion := mult(&x, &y)
	fmt.Println(churchToNatural(&suma))
	fmt.Println(churchToNatural(&multiplicacion))
}
