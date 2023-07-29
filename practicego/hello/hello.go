package main

import (
	"fmt"
	"sync"
)

func main() {
	var counter int
	var lock sync.Mutex
	var wg sync.WaitGroup

	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			lock.Lock()
			counter++
			lock.Unlock()
			wg.Done()
		}()

	}
	wg.Wait()
	fmt.Println(counter)
}
