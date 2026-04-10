#!/usr/bin/env python3

from collections import defaultdict
from typing import Dict

instructions = [
    ("A", "B"),
    ("C", "B"),
    ("D", "E"),
    ("B", "T1"),
    ("E", "T2"),
    ("F", "E"),
    ("G", "H")
]


treasure_rooms = {"T1", "T2"}

def main():
    in_degress: Dict[str, int] = defaultdict(int)
    instruction_map = defaultdict(list)
    for instruction in instructions:
        in_degress[instruction[1]] += 1
        instruction_map[instruction[0]].append(instruction[1])

    res = []
    for k,v in in_degress.items():
        if v >= 2:
            for treasure_room in treasure_rooms:
                if treasure_room in instruction_map[k]:
                    res.append(k)
    print(res)

if __name__ == '__main__':
    main()