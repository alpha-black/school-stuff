#!/usr/bin/env python3

from typing import List, Set

def combinations(nums: List[str], current:List[int], index: int, result: List[List[int]]):
    if index == len(nums):
        result.append(current[:])
        return

    current.append(nums[index])
    combinations(nums, current, index+1, result)
    current.pop()
    combinations(nums, current, index+1, result)

def main():
    result = []
    combinations([4,5,6], [], 0, result)
    print(result)

if __name__ == '__main__':
    main()