#!/usr/bin/env python3
"""
Determine the number of distinct ways to climb a staircase of n steps by
taking either 1 or 2 steps at a time.
"""


def stairs(num: int) -> int:
    ret = [0, 1, 2]
    for i in range(3, num+1):
        rett = ret[i-1]+ ret[i-2]
        ret.append(rett)
    return rett

def main():
    print(stairs(4))

if __name__ == '__main__':
    main()