package main

import "fmt"

type User struct {
	name  string
	email string
}

func main() {
	u1 := User{}
	fmt.Println(u1)
}
