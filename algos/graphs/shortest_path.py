#!/usr/bin/env python3

from typing import List
import heapq

from node import GraphNode


def create_graph(num: int, edges: List[List], start: int):
    nodes: List[GraphNode] = []
    for i in range(num):
        nodes.append(GraphNode(i, [], []))

    for edge in edges:
        nodes[edge[0]].neighbors.append(edge[1])
        nodes[edge[0]].weights.append(edge[2])
        nodes[edge[1]].neighbors.append(edge[0])
        nodes[edge[1]].weights.append(edge[2])
    return nodes

def shortest_path(nodes: List[GraphNode], start: int, num: int):
    path = [float('inf')] * num
    current, path[start] = start, 0
    visited, covered_dist = [], 0

    while current not in visited:
        visited.append(current)
        next = current
        min_weight = float('inf')
        for i, w in enumerate(nodes[current].weights):
            w += covered_dist
            if min_weight > w and nodes[current].neighbors[i] not in visited:
                min_weight = w
                next = nodes[current].neighbors[i]
            if path[nodes[current].neighbors[i]] > w:
                path[nodes[current].neighbors[i]] = w

        covered_dist += min_weight
        current = next

    path = [p if p != float('inf') else -1 for p in path]
    return path

def main():
   start = 0
   nodes = create_graph(6, [
        [0, 1, 5],
        [0, 2, 3],
        [1, 2, 1],
        [1, 3, 4],
        [2, 3, 4],
        [2, 4, 5],
    ], start)
   print(f'Shortest path from {start}: {shortest_path(nodes, 0, 6)}')

if __name__ == '__main__':
    main()