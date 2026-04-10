#!/usr/bin/env python3

from collections import defaultdict, deque

graph1 = [[1,3], [2,3], [4,2], [4,7]]
graph2 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
    (12, 9),(15, 13),
]

def common_ancestor(x, y):
    graph = defaultdict(list)
    in_degrees = defaultdict(int)

    for g in graph2:
        graph[g[0]].append(g[1])
        in_degrees[g[0]] += 0
        in_degrees[g[1]] += 1

    zin_degrees = []
    for g, count in in_degrees.items():
        if count == 0:
            zin_degrees.append(g)

    q = deque()
    for i in range(0, len(zin_degrees)):
        q.append(zin_degrees[i])
        found_x, found_y = False, False
        while q:
            node = q.pop()
            for child in graph[node]:
                in_degrees[child] -= 1
                if child == x: found_x = True
                if child == y: found_y = True
                if found_y and found_x:
                    print('Found')
                    return
                if in_degrees[child] == 0:
                    q.append(child)
    # print(zin_degrees)
    print('Not found')

def in_degrees(graph):
    map = defaultdict(int)
    for g in graph:
        map[g[0]] += 0
        map[g[1]] += 1
    parents, child_with_one_parent = [], []
    for node, in_degrees in map.items():
        if in_degrees == 0:
            parents.append(node)
        if in_degrees == 1:
            child_with_one_parent.append(node)

    print(parents, child_with_one_parent)

if __name__ == '__main__':
    # in_degrees(graph1)
    common_ancestor(3,8)