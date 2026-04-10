#!/usr/bin/env python3
"""
Find the k most frequently occurring strings in an array, and return them
sorted by frequency in descending order. If two strings have the same frequency,
sort them in lexicographical order.
"""
from dataclasses import dataclass
from typing import List
import heapq

@dataclass
class HeapString:
    name: str
    count: int = 0

    # hack for max heap
    def __lt__(self, other: 'HeapString'):
        if self.count == other.count:
            return self.name < other.name
        return self.count > other.count

    def __gt__(self, other: 'HeapString'):
        return self.count > other.count

    def __eq__(self, other: 'HeapString'):
        return self.count == other.count


def find_k_most_frequent_strings(strings: List[str], k: int) -> None:
    ret = []
    q: List[HeapString] = []
    for s in strings:
        found = False
        for qq in q:
            if qq.name == s:
                qq.count += 1
                found = True
        if not found:
            q.append(HeapString(s, 1))


    heapq.heapify(q)
    for _ in range(k):
        ret.append(heapq.heappop(q).name)

    return ret

def main():
    print(find_k_most_frequent_strings(
        ['go', 'coding', 'byte', 'byte', 'go', 'interview', 'go', 'byte'], 2,
    ))

if __name__ == '__main__':
    main()