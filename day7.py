""" Advent of Code 2021 day 7 """

import numpy as np

INPUT_FILE = "input7.txt"


def get_fuel(pos, target_pos):
    return abs(pos - target_pos)


def get_increasing_fuel(pos, target_pos):
    return sum(range(1, abs(pos - target_pos) + 1))


def get_sum_fuel_part2(positions):
    avg = int(np.average(positions))
    fuel = 0
    for pos in positions:
        fuel += get_increasing_fuel(pos, avg)
    return fuel


def get_sum_fuel_part1(positions):
    median = int(np.median(positions))
    fuel = 0
    for pos in positions:
        fuel += get_fuel(pos, median)
    return fuel


def read_input(file_name):
    return np.loadtxt(file_name, dtype=int, delimiter=",")


if __name__ == "__main__":
    positions = read_input(INPUT_FILE)

    print("Part 1:\t", get_sum_fuel_part1(positions))

    print("Part 2:\t", get_sum_fuel_part2(positions))

    exit()
    # very messy first attempt

    positions = np.loadtxt(INPUT_FILE, dtype=int, delimiter=",")

    print(np.mean(positions), "aaa")
    print(np.median(positions))
    print(positions)
    print(max(positions))

    maximum = max(positions)
    minimum = min(positions)

    min_fuel = maximum * len(positions)

    for i in range(minimum, maximum + 1):
        this_fuel = 0
        for pos in positions:
            this_fuel += abs(pos - i)
        min_fuel = min(min_fuel, this_fuel)

    print(min_fuel)

    min_fuel_2 = maximum * len(positions) * len(positions)

    for i in range(minimum, maximum + 1):
        this_fuel = 0
        for pos in positions:
            # for j in range(abs(pos-i+1)):
            #     this_fuel += j
            this_fuel += sum(list(range(1, abs(pos - i) + 1)))
        min_fuel_2 = min(min_fuel_2, this_fuel)

    print("2:", min_fuel_2)
