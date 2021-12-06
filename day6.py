""" Advent of Code 2021 day 6 """

import numpy as np

INPUT_FILE = "input6.txt"


def read_file(filename):
    return np.loadtxt(filename, dtype=int, delimiter=",")


def initialize_fishes(input):
    fishes = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fish in input:
        fishes[fish] += 1
    return fishes


def after_days(n, fishes):
    spawn_day = 0
    for day in range(n):
        new_day = (spawn_day - 2) % 9
        fishes[new_day] += fishes[spawn_day]
        spawn_day = (spawn_day + 1) % 9
    return sum(fishes.values())


if __name__ == "__main__":

    fish_input = read_file(INPUT_FILE)
    fishes = initialize_fishes(fish_input)

    print("Part 1:\t", after_days(80, fishes))

    fishes = initialize_fishes(fish_input)
    print("Part 2:\t", after_days(256, fishes))
    exit()

    # ------ First Attempt -------
    class Fish:
        def __init__(self, timer=9):
            self.timer = timer
            self.spawn = False

        def __repr__(self):
            return str(self.timer)

        def next_day(self):
            if self.timer > 0:
                self.timer -= 1
                self.spawn = False
            else:
                self.timer = 6
                self.spawn = True

    fishes = []
    input = np.loadtxt(filename, dtype=int, delimiter=",")
    for f in input:
        fishes.append(Fish(f))
    for day in range(80):
        for f in fishes:
            f.next_day()
            if f.spawn:

                fishes.append(Fish())
                # fishes.append(Fish())
    # print(fishes)

    print(len(fishes))

    empty_fish_bucket = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    print(empty_fish_bucket)

    fish_buckets = {**empty_fish_bucket}

    for f in input:
        fish_buckets[f] += 1

    print(fish_buckets)
    for day in range(256):
        new_fish = {**empty_fish_bucket}
        for i in range(6):
            new_fish[i] = fish_buckets[i + 1]
        new_fish[6] = fish_buckets[0] + fish_buckets[7]
        new_fish[7] = fish_buckets[8]
        new_fish[8] = fish_buckets[0]
        fish_buckets = {**new_fish}

    print(fish_buckets)
    summe = 0
    for value in fish_buckets.values():
        summe += value
    print(summe)
