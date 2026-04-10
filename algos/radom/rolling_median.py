#!/usr/bin/env python3

import heapq
from collections import deque, defaultdict


class EpisodeRatingMedian():
    def __init__(self, window = 600):
        self.window = window
        self.lower, self.higher, self.q = [], [], deque()
        self.removed_count = 0

    def add_rating(self, timestamp: int, rating: int):
        self.q.append((timestamp, rating))

        if not self.lower or -rating <= -self.lower[0]:
            heapq.heappush(self.lower, -rating)
        else:
            heapq.heappush(self.higher, rating)
        self.__rebalance__()

    def __rebalance__(self):
        len_l, len_r = len(self.lower), len(self.higher)
        if len_l > len_r + 1:
            rating = heapq.heappop(self.lower)
            heapq.heappush(self.higher, -rating)
        elif len_l < len_r -1:
            rating = heapq.heappop(self.higher)
            heapq.heappush(self.lower, -rating)

    @property
    def median(self):
        self.removed_count += 1
        while self.q and self.q[0][0] > self.window:
            t_r = self.q.popleft()
            if -t_r[1] in self.lower:
                self.lower.remove(t_r[1])
            elif t_r[1] in self.higher:
                self.higher.remove(t_r[1])
            self.__rebalance__()
        len_l, len_r = len(self.lower), len(self.higher)

        if len_l == len_r:
            return (-self.lower[0] + self.higher[0])/2
        else:
            return -self.lower[0]


class EpisodeRatingTracker():
    def __init__(self):
        self.episode_rating = defaultdict(lambda: EpisodeRatingMedian())

    def add(self, e, r, t):
        self.episode_rating[e].add_rating(t, r)

    def median(self, e):
        return self.episode_rating[e].median

if __name__ == '__main__':
    t = EpisodeRatingTracker()
    t.add("Naruto_S1E1", 8, 100)
    t.add("Naruto_S1E1", 10, 200)
    t.add("Naruto_S1E1", 9, 700)
    t.add("Naruto_S1E1", 9, 300)

    median = t.median("Naruto_S1E1")
    print(median)