#!/usr/bin/env python3

from collections import defaultdict, deque

episodes = {
  "E1": "E2",
  "E2": "E3",
  "E3": "E4",
  "E5": "E6",
  "E4": "E6",
  "E7": "E4",
  "E7": "E1",
  "E7": "E2",
  "E2": "E7",
}

def topological_sort(graph) -> None:
    # find in-degrees
    in_degress = defaultdict(int)
    for k,v in graph.items():
        in_degress[k] += 0
        for n in v:
            in_degress[n] += 1

    q = deque()
    for k,v in in_degress.items():
        if v == 0: q.append(k)

    visited = len(q)
    while q:
        e = q.pop()
        for n in graph[e]:
            in_degress[n] -= 1
            if in_degress[n] == 0:
                q.append(n)
                visited += 1
    print(f'Loop found: {visited != len(graph)}')


def longest_chain(e, graph, memo = defaultdict(int)) -> int:
    if e in memo:
        return memo[e]

    max_path = 1
    for n in graph[e]:
        max_path = max(max_path, longest_chain(n, graph, memo) + 1)
    memo[e] = max_path
    return max_path

def main():
    graph = defaultdict(list)

    for k,v in episodes.items():
        graph[k].append(v)

    print(graph)
    # print(longest_chain("E1", graph))
    topological_sort(graph)

if __name__ == '__main__':
    main()