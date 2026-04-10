#!/usr/bin/env python3
"""
Merge an array of intervals so there are no overlapping intervals,
and return the resultant merged intervals.
"""
from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    merged_intervals = []
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    for interval in sorted_intervals:
        if not merged_intervals:
            merged_intervals.append(interval)
            continue
        last_interval = merged_intervals[-1]
        if last_interval[1] >= interval[0]:
            # merge
            last_interval[1] = max(interval[1], last_interval[1])
            continue
        merged_intervals.append(interval)

    return merged_intervals

def main():
    print(merge([[3, 4], [7, 8], [2, 5], [6, 7], [1, 4]]))

if __name__ == '__main__':
    main()