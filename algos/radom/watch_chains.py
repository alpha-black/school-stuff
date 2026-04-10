#!/usr/bin/env python3

from collections import defaultdict


logs = [
    ("user1", "Naruto", 1),
    ("user1", "Bleach", 2),
    ("user1", "One Piece", 3),
    ("user2", "Bleach", 4),
    ("user2", "Naruto", 5),
    ("user2", "One Piece", 6),
    ("user2", "Bleach", 7),
]


def main():
    user_log = defaultdict(list)
    for log in logs:
        user_log[log[0]].append((log[2], log[1]))

    pairs = defaultdict(int)
    most_common_pair = ()
    pair_count_max = 0
    for user, shows in user_log.items():
        shows.sort()
        for i in range(len(shows) - 1):
            pairs[(shows[i][1], shows[i+1][1])] += 1
            if pairs[(shows[i][1], shows[i+1][1])] > pair_count_max:
                pair_count_max = pairs[(shows[i][1], shows[i+1][1])]
                most_common_pair = (shows[i][1], shows[i+1][1])

    print(user_log)
    print(pairs)
    print(f'Most common pair {most_common_pair}')


if __name__ == '__main__':
    main()