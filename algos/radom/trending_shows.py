#!/usr/bin/env python3

import heapq
from collections import defaultdict
from dataclasses import dataclass

events = [("A", 10), ("B", 5), ("A", 2), ("C", 9)]
k = 2


def main():
    e_map = {}
    for event in events:
        if event[0] not in e_map: e_map[event[0]] = 0
        e_map[event[0]] += event[1]

    e_heap = [(v, k) for k, v in e_map.items()]
    heapq.heapify(e_heap)
    for _ in range(k):
        print(heapq.heappop(e_heap))

if __name__ == '__main__':
    main()