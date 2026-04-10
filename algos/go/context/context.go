package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

const (
	NUM_WORKERS = 10
)

func worker(ctx context.Context, id int) {

	for {
		select {
		case <-ctx.Done():
			fmt.Println("Got ctx done for:", id)
			return
		default:
			fmt.Println("Processing something:", id)
			time.Sleep(time.Second)
		}
	}
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), time.Second*10)
	defer cancel()

	var wg sync.WaitGroup
	id := 0
	for i := 0; i < NUM_WORKERS; i++ {
		wg.Go(func() {
			worker(ctx, id)
		})
		id++
	}

	time.Sleep(time.Second * 3)
	fmt.Println("Cancel context")
	cancel()

	wg.Wait()
	fmt.Println("Exiting main")
}
