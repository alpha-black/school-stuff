#!/usr/bin/env python3

altitudes = [0,1,2,1]
snow_1 = [[1,0,1,0], [0,0,0,0], [1,1,0,2]]

def best_day_to_cross(alts, snow_all_days):
    new_alts = alts
    ret = [float('inf')]*len(snow_all_days)

    for i in range(len(snow_all_days)):
        climbs = 0
        for j in range(len(alts)):
            new_alts[j] += snow_all_days[i][j]
            if i >= 1 and snow_all_days[i-1][j] == 0 and snow_all_days[i][j] == 0:
                new_alts[j] -= 1
            if j > 1 and abs(new_alts[j-1] - new_alts[j]) > 1:
               climbs = float('-inf')
            if j > 0 and new_alts[j] > new_alts[j-1]:
                climbs += 1
        ret[i] = min(ret[i], climbs)
    print(ret)

if __name__ == '__main__':
    best_day_to_cross(altitudes, snow_1)