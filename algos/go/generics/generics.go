package main

import (
	"fmt"
)

type Number interface {
	int | float32
}

func genericSum[V Number](nums []V) V {
	var ret V
	for _, i := range nums {
		ret += i
	}
	return ret
}

func main() {
	fmt.Println("Generic sum: ", genericSum[int]([]int{1, 2, 3, 4}))
	fmt.Println("Generic sum: ", genericSum[float32]([]float32{1.2, 2.3, 3.4, 4.5}))
}
