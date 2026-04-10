#!/usr/bin/env python3
"""
You are given an array of coin values and a target amount of money.
Return the minimum number of coins needed to total the target amount.
If this isn't possible, return ‐1. You may assume there's an unlimited
supply of each coin.
"""

from typing import List

def min_coins(coins: List[int], target: int) -> int:
    ret = [float('inf')] * (target + 1)
    ret[0] = 0

    for i in range(1, target+1):
        for coin in coins:
            if coin > i:
                continue
            ret[i] = min(ret[i], 1+ret[i-coin])

    return ret[target] if ret[target] != float('inf') else -1

def main():
    print(min_coins([1,2,3], 5))
    print(min_coins([2,4], 5))

if __name__ == '__main__':
    main()