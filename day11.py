""" Advent of Code 2021 day 11 """

import numpy as np


INPUT_FILE = "input11.txt"

input_txt = np.loadtxt(INPUT_FILE, dtype=str)
matrix = np.array([list(a) for a in input_txt]).astype(int)
mask = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
flash_count = 0
step = 0
while True:
    matrix += 1
    flashed = np.zeros((len(matrix), len(matrix[0])))
    # chain reaction
    a, b = np.where((matrix > 9) & (flashed == 0))
    flashed = np.where(matrix > 9, 1, flashed)
    while len(a) > 0:
        # one step
        while len(a) > 0:
            x, a = a[0], a[1:]
            y, b = b[0], b[1:]

            if x > 0 and y > 0:
                matrix[x - 1, y - 1] += 1
            if x > 0:
                matrix[x - 1, y] += 1
            if x > 0 and y < len(matrix[0]) - 1:
                matrix[x - 1, y + 1] += 1
            if y > 0:
                matrix[x, y - 1] += 1
            if y < len(matrix[0]) - 1:
                matrix[x, y + 1] += 1
            if x < len(matrix) - 1 and y > 0:
                matrix[x + 1, y - 1] += 1
            if x < len(matrix) - 1:
                matrix[x + 1, y] += 1
            if x < len(matrix) - 1 and y < len(matrix[0]) - 1:
                matrix[x + 1, y + 1] += 1
        a, b = np.where((matrix > 9) & (flashed == 0))
        flashed = np.where(matrix > 9, 1, flashed)
    matrix = np.where(flashed == 1, 0, matrix)
    flash_count += np.count_nonzero(flashed)
    step += 1
    if step == 100:
        print("Part 1:\t", flash_count)
    if len(np.where(flashed == 0)[0]) == 0:
        print("Part 2:\t", step)
        break
