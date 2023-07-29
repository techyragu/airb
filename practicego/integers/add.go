package main

import "fmt"

func add(a int, b int) int {
	return a + b
}

func main() {
	fmt.Println(add(5, 7))
	var s []int
	fmt.Println(len(s))
}
