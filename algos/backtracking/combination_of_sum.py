#!/usr/bin/env python3
"""
Given an integer array and a target value, find all unique combinations
in the array where the numbers in each combination sum to the target.
Each number in the array may be used an unlimited number of times in the
combination.
"""

from typing import List

def combination_of_sum(nums: List[int], target: int, start_index: int, current: List[int], result: List[List[int]]):
    if target == 0:
        result.append(current[:])
        return

    for i, num in enumerate(nums):
        if i < start_index or num > target:
            continue
        current.append(num)
        combination_of_sum(nums, target - num, i, current, result)
        current.pop()

def main():
    result = []
    combination_of_sum([1,2,3], 4, 0, [], result)
    print(result)

if __name__ == '__main__':
    main()