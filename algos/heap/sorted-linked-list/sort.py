#!/usr/bin/env python3
"""
Given k singly linked lists, each sorted in ascending order,
combine them into one sorted linked list.
"""
import heapq
from dataclasses import dataclass
from typing import List

@dataclass
class Node:
    val: int
    next: 'Node' = None

    def __lt__(self, other):
        return self.val < other.val


def create_list(nums: List[int]) -> Node:
    head, current = None, None
    for num in nums:
            n = Node(num, None)
            if head is None:
                head, current = n, n
                continue

            current.next = n
            current = n
    return head


def print_list(head: Node) -> None:
    current = head
    while current is not None:
        print(current.val)
        current = current.next


def combine_sorted_lists(list_nums: List[Node]) -> Node:
    ret_head, current = None, None
    q = []
    for num in list_nums:
        heapq.heappush(q, num)

    while len(q) != 0:
        smallest_node = heapq.heappop(q)
        if smallest_node.next:
            heapq.heappush(q, smallest_node.next)
        if ret_head == None:
            ret_head, current = smallest_node, smallest_node
            continue

        current.next = smallest_node
        current = current.next

    return ret_head


def main():
    nums1 = create_list([1,6])
    nums2 = create_list([1,4,6])
    nums3 = create_list([3,7])
    nums4 = create_list([4,10])
    combined = combine_sorted_lists([nums1, nums2, nums3, nums4])
    print_list(combined)

if __name__ == '__main__':
    main()