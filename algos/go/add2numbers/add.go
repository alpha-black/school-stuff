package main

import (
	"fmt"
)

type node struct {
	val  int
	next *node
}

func add(list1, list2 *node) *node {
	var head *node
	var cur *node
	carry := 0

	for list1 != nil && list2 != nil {
		val := list1.val + list2.val + carry
		carry = int(val / 10)
		val = val % 10
		new := &node{val, nil}

		if head == nil {
			head = new
			cur = head

		} else {
			cur.next = new
			cur = new
		}
		list1 = list1.next
		list2 = list2.next
	}
	if carry != 0 {
		cur.next = &node{carry, nil}
	}
	return head
}

func createList(nums []int) *node {
	var head *node
	var cur *node
	for _, num := range nums {
		if head == nil {
			head = &node{num, nil}
			cur = head
			continue
		}
		new := &node{num, nil}
		cur.next = new
		cur = new
	}
	return head
}

func printList(list *node) {
	for n := list; n != nil; n = n.next {
		fmt.Println(n.val)
	}
}

func main() {
	list1 := createList([]int{1, 3, 5})
	list2 := createList([]int{2, 4, 6})
	printList(list1)
	printList(list2)
	fmt.Println("After adding")
	printList(add(list1, list2))

}
