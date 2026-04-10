package main

import (
	"fmt"
	"time"
)

var (
	item    chan int
	done    chan int
	allDone chan bool
)

func worker() {
	for {
		itemNum := <-item
		fmt.Println("Processing work from channel: ", itemNum)
		time.Sleep(time.Second)
		done <- itemNum
	}
}

func waitForWorkers(workItems int) {
	go func() {
		for i := 0; i < workItems; i++ {
			itemNum := <-done
			fmt.Println("Worker finished itemNum: ", itemNum)
		}
		allDone <- true
	}()
}

func startWorkers(numWorkers int, workerFn func()) {
	for i := 0; i < numWorkers; i++ {
		go workerFn()
	}
}

func sendItemsToWorkers(workItems int) {
	for i := 0; i < workItems; i++ {
		item <- i
	}
}

func main() {
	const (
		MAX_WORKERS     = 3
		MAX_CHAN_BUFFER = 10
		WORK_ITEMS      = 100
	)
	item = make(chan int, MAX_CHAN_BUFFER)
	done = make(chan int, MAX_CHAN_BUFFER)
	allDone = make(chan bool)

	defer close(item)
	defer close(done)
	defer close(allDone)

	startWorkers(MAX_WORKERS, worker)
	waitForWorkers(WORK_ITEMS)
	sendItemsToWorkers(WORK_ITEMS)
	<-allDone
}
