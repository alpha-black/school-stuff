#!/usr/bin/env python3

from typing import List

class UnionFind():
    def __init__(self, n):
        # self.points = [i for i in range(n)]
        self.sizes = [1] * n
        self.parent = [i for i in range(n)]

    def union(self, x, y) -> bool:
        p_x, p_y = self.find(x), self.find(y)
        if p_x == p_y: return False

        if self.sizes[x] > self.sizes[y]:
            self.sizes[x] += self.sizes[y]
            self.parent[p_y] = p_x
        else:
            self.sizes[y] += self.sizes[x]
            self.parent[p_x] = p_y
        return True

    def find(self, x):
        if self.parent[x] == x: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


def minimum_spanning_tree(points: List[List[int]]) -> None:
    n = len(points)
    distances = []
    for x in range(n):
        for y in range(x+1, n):
            distances.append(
                (abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1]),
                x, y)
            )
    distances.sort()
    print(distances)

    union_find = UnionFind(n)
    connections = 0
    total_distance = 0
    for distance in distances:
        if connections == n - 1:
            break
        if union_find.union(distance[1], distance[2]):
            connections += 1
            total_distance += distance[0]

    print(total_distance)

if __name__ == '__main__':
    points = [[1, 1], [2, 6], [3, 2], [4, 3], [7, 1]]
    minimum_spanning_tree(points)