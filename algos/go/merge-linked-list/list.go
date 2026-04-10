package main

import (
	"fmt"
)

type node struct {
	val  int
	next *node
}

func mergeList(list1, list2 *node) *node {

	var low *node
	var high *node

	ret := list1
	if list1.val > list2.val {
		ret = list2
	}

	for list1 != nil && list2 != nil {
		if list1.val <= list2.val {
			low, high = list1, list2
			list1 = list1.next
		} else {
			low, high = list2, list1
			list2 = list2.next
		}
		low.next = high
	}
	return ret
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
	fmt.Println("After merging")
	printList(mergeList(list1, list2))

}
