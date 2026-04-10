package main

import (
	"fmt"
	"sync/atomic"
)

type WaitGroup interface {
	Go(func())
	Wait()
}

type WaitGroupImp struct {
	done       chan bool
	goRoutines atomic.Uint32
}

func NewWaitGroup() WaitGroupImp {
	return WaitGroupImp{
		done: make(chan bool),
	}
}

func (wg *WaitGroupImp) Go(f func()) {
	wg.goRoutines.Add(1)
	go func(f func()) {
		f()
		wg.done <- true
	}(f)
}

func (wg *WaitGroupImp) Wait() {
	subRoutines := wg.goRoutines.Load()
	for range subRoutines {
		<-wg.done
	}
	fmt.Println("All subroutines have finished executing")
}
