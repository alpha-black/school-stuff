package main

import (
	"fmt"
	"time"
)

func worker() {
	timeSeconds := 5
	fmt.Println("Worker doing something")
	time.Sleep(time.Second * time.Duration(timeSeconds))
	fmt.Println("Worker done")
}

func main() {
	wg := NewWaitGroup()
	for range 10 {
		wg.Go(worker)
	}
	wg.Wait()
}
