""" Advent of Code 2021 day 5"""

import numpy as np

INPUT_FILE = "input5.txt"
GRID_SIZE = 1000


with open(INPUT_FILE) as f:
    input = f.readlines()

grid = np.zeros((GRID_SIZE, GRID_SIZE))

for line in input:
    x1, y1, x2, y2 = line.replace(" -> ", ",").split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    if x1 == x2:
        grid[x1, y1 : y2 + 1] += 1
        grid[x1, y2 : y1 + 1] += 1

    if y1 == y2:
        grid[x1 : x2 + 1, y1] += 1
        grid[x2 : x1 + 1, y1] += 1


print(np.count_nonzero(grid > 1))

grid = np.zeros((GRID_SIZE, GRID_SIZE))
for line in input:
    x1, y1, x2, y2 = line.replace(" -> ", ",").split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    if x1 == x2:
        grid[x1, y1 : y2 + 1] += 1
        grid[x1, y2 : y1 + 1] += 1

    if y1 == y2:
        grid[x1 : x2 + 1, y1] += 1
        grid[x2 : x1 + 1, y1] += 1

    if abs(x1 - x2) == abs(y1 - y2):
        if x1 > x2:
            if y1 > y2:
                for i in range(y1 - y2 + 1):
                    grid[x1 - i, y1 - i] += 1
            if y1 < y2:
                for i in range(x1 - x2 + 1):
                    grid[x1 - i, y1 + i] += 1
        if x1 < x2:
            if y1 > y2:
                for i in range(y1 - y2 + 1):
                    grid[x1 + i, y1 - i] += 1
            if y1 < y2:
                for i in range(x2 - x1 + 1):
                    grid[x1 + i, y1 + i] += 1

print(np.count_nonzero(grid > 1))

# refactor


def sort_values(a1, a2):
    return [min(a1, a2), max(a1, a2)]


with open(INPUT_FILE) as f:
    input_text = f.readlines()

grid1 = np.zeros((GRID_SIZE, GRID_SIZE))
grid2 = np.zeros((GRID_SIZE, GRID_SIZE))

for line in input_text:
    [x1, y1, x2, y2] = [int(x) for x in line.replace(" -> ", ",").split(",")]

    if x1 == x2:
        y1, y2 = sort_values(y1, y2)
        grid1[y1 : y2 + 1, x1] += 1
        grid2[y1 : y2 + 1, x1] += 1

    if y1 == y2:
        x1, x2 = sort_values(x1, x2)
        grid1[y1, x1 : x2 + 1] += 1
        grid2[y1, x1 : x2 + 1] += 1

    if x2 - x1 == y2 - y1:
        # diagonal ascending
        x1, x2 = sort_values(x1, x2)
        y1, y2 = sort_values(y1, y2)

        for i in range(x2 - x1 + 1):
            grid2[y1 + i, x1 + i] += 1

    if x2 - x1 == y1 - y2:
        # diagonal decending
        x1, x2 = sort_values(x1, x2)
        y1, y2 = sort_values(y1, y2)

        for i in range(x2 - x1 + 1):
            grid2[y2 - i, x1 + i] += 1


print("Part 1:\t", np.count_nonzero(grid1 > 1))
print("Part 2:\t", np.count_nonzero(grid2 > 1))
