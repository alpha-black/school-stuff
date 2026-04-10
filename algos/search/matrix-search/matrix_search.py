#!/usr/bin/env python3
"""
Determine if a target value exists in a matrix. Each row of the matrix is
sorted in non-decreasing order, and the first value of each row is greater
than or equal to the last value of the previous row.
"""
from typing import List, Tuple

def matrix_search(m: List[List[int]], val) -> Tuple[int, int]:
    rows = len(m)
    cols = len(m[0])

    left, right = 0, (rows * cols) - 1

    while left <= right:
        index = (left + right)//2
        row, col = (index // cols), (index % cols)

        if m[row][col] == val:
            return row, col
        if val < m[row][col]:
            right = index -1
        else:
            left = index +1
    return -1, -1


def main():
    m = [[2,3,4,6],[7,10,11,17],[20,21,24,33]]
    print(matrix_search(m, 21))
    print(matrix_search(m, 17))
    print(matrix_search(m, 31))
    print(matrix_search(m, 33))
    print(matrix_search(m, 4))

if __name__ == '__main__':
    main()