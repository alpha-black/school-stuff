#!/usr/bin/env python3

teleporters1 = ["5,10", "6,22", "39,40", "40,49", "47,29"]
teleporters3 = ["10,8", "11,5", "12,1", "13,9", "2,15"]
teleporters2 = ["5,10", "6,22", "39,40", "40,49", "47,29"]


def finishable_helper(tele, die, start, end):
    if start >= end:
        return True

    while end > start and end not in tele:
        end -= 1
    new_end = end
    for count in range(end, end-die-1, -1):
        if count not in tele and count >= start:
            new_end = count
    if new_end == end:
        return False

    return finishable_helper(tele, die, start, new_end)

def finishable(tele, die, start, end):
    for i in range(len(tele)):
        t = tele[i].split(',')
        tele[i] = int(t[0])
    tele.sort()
    return finishable_helper(tele, die, start, end)

if __name__ == '__main__':
    print(finishable(teleporters3, 4, 0, 20))
    print(finishable(teleporters1, 4, 9, 20))
    print(finishable(teleporters2, 1, 4, 6))