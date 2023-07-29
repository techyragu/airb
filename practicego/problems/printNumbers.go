package main

func PrintNumbers(n int, ch chan int) {
	for i := 1; i <= n; i++ {
		ch <- i
	}

}

func PrintFib(n int, ch chan int) {
	a, b := 0, 1
	for i := 1; i <= n; i++ {
		ch <- a
		a, b = b, a+b
	}
}

// func main() {
// 	ch := make(chan int)
// 	n := 10

// 	//go PrintNumbers(n, ch)
// 	go PrintFib(n, ch)

// 	for v := range ch {
// 		fmt.Println(v)
// 	}

// }
