#!/usr/bin/env python3

from typing import List

def permutations(nums: List[int], current: List[int], result: List[List[int]]):
    if len(current) == len(nums):
        result.append(current[:])
        return

    for num in nums:
        if num in current:
            continue

        current.append(num)
        permutations(nums, current, result)
        current.pop()

def main():
    result = []
    permutations([4, 5, 6], [], result)
    print(result)

if __name__ == '__main__':
    main()