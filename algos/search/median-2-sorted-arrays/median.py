#!/usr/bin/env python3
"""
Given two sorted integer arrays, find their median value as if they
were merged into a single sorted sequence.
"""

from typing import List

def median(nums1: List[int], nums2: List[int]) -> float:
    half_len = (len(nums1) + len(nums2)) // 2
    nums1, nums2 = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)

    m = len(nums1)
    n = len(nums2)
    left, right = 0, m - 1

    while True:
        l1_index = (left + right)//2
        l2_index = half_len - (l1_index + 1) - 1

        l1 = float('-inf') if l1_index < 0 else nums1[l1_index]
        l2 = float('-inf') if l2_index < 0 else nums2[l2_index]
        r1 = float('inf') if l1_index + 1 >= m else nums1[l1_index + 1]
        r2 = float('inf') if l2_index + 1 >= n else nums2[l2_index + 1]

        if l1 > r2:
            right = l1_index - 1
        elif l2 > r1:
            left = l1_index + 1
        else:
            return (max(l1, l2) + min(r1, r2)) / 2.0 if (m + n) % 2 == 0 else min(r1, r2)

def main():
    print(median([1,3,5,7,9], [2,4,6,8,10]))
    print(median([1,2,3,4,5], [6,7,8,9,10]))

if __name__ == '__main__':
    main()