#!/usr/bin/env python3

from collections import defaultdict


# time, user id, resource id
logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
]

def print_graph(r, graph):
    print()
    s = sum(graph.values())
    print(f'For {r}:', *[(g, graph[g]/s) for g in graph])


def transition_graph():
    user_log = defaultdict(list)
    for log in logs1:
        u, t, r = log[1], log[0], log[2]
        user_log[u].append((t,r))
    for user, pair in user_log.items():
        pair.sort()

    graph = defaultdict(list)
    starts = defaultdict(int)
    for user, pairs in user_log.items():
        starts[pairs[0][1]] += 1
        if len(pairs) == 1:
            graph[pairs[0][1]].append('end')
        for i in range(len(pairs) - 1):
            r, r_n = pairs[i][1], pairs[i+1][1]
            graph[r].append(r_n)
            if r_n in starts:
                starts.pop(r_n)
    print_graph('start', starts)
    for g in graph:
        items = defaultdict(int)
        for node in graph[g]:
            items[node] += 1
        print_graph(g, items)


def count_times_in_window(times, window):
    l, r = 0, 1
    max_count = 0
    count = 0
    while r < len(times):
        if (times[r] - times[l]) <= window:
            r+=1
            count += 1
            max_count = max(max_count, count)
            continue


        l += 1
        r = l+1
        count = 0
    return max_count


def highest_number_of_access(window: int):
    r_info = defaultdict(list)
    for log in logs1:
        u, t, r = log[1], log[0], log[2]
        r_info[r].append(int(t))

    max_resource, max_count = None, 0
    for r, times in r_info.items():
        times.sort()
        count = count_times_in_window(times, window)
        if count > max_count:
            max_resource, max_count = r, count

    print(max_resource, max_count)


def min_max_entry_for_users():
    user_min_max = {}
    for log in logs1:
        u, t, r = log[1], log[0], log[2]
        if u not in user_min_max:
            user_min_max[u] = [(t,r), (t,r)]
            continue
        if t < user_min_max[u][0][0]:
            user_min_max[u][0] = (t,r)
        if t > user_min_max[u][1][0]:
            user_min_max[u][1] = (t,r)
    print(user_min_max)


if __name__ == '__main__':
    min_max_entry_for_users()
    highest_number_of_access(500)
    transition_graph()