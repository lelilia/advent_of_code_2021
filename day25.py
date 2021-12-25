""" Advent of Code 2021 day 25 - Sea Cucumber """

import numpy as np

INPUT_FILE = "input25.txt"


def print_area(area):
    p_area = np.where(area == 0, ".", area)
    p_area = np.where(area == 1, ">", p_area)
    p_area = np.where(area == 2, "v", p_area)
    print("\n".join(["".join(a) for a in p_area]))


with open(INPUT_FILE) as f:
    data = f.read().strip().split("\n")

area = np.array([[a for a in b] for b in data])
area = np.where(area == ".", 0, area)
area = np.where(area == ">", 1, area)
area = np.where(area == "v", 2, area).astype(int)


row_mod, col_mod = area.shape

step = 0
something_moved = True
while something_moved:
    step += 1
    something_moved = False
    rows, cols = np.where(area == 1)
    new_area = area.copy()
    while len(rows) > 0:
        row, rows = rows[0], rows[1:]
        col, cols = cols[0], cols[1:]
        if area[row, (col + 1) % col_mod] == 0:
            new_area[row, (col + 1) % col_mod] = 1
            new_area[row, col] = 0
            something_moved = True
    area = new_area.copy()
    rows, cols = np.where(area == 2)
    new_area = area.copy()
    while len(rows) > 0:
        row, rows = rows[0], rows[1:]
        col, cols = cols[0], cols[1:]
        if area[(row + 1) % row_mod, col] == 0:
            new_area[(row + 1) % row_mod, col] = 2
            new_area[row, col] = 0
            something_moved = True
    area = new_area.copy()

print()
print(step)
