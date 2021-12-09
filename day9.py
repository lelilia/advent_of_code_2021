import numpy as np


INPUT_FILE = "testinput9.txt"

input = np.loadtxt(INPUT_FILE, dtype=str)
y = np.array([[a for a in b] for b in input]).astype(int)
y = np.pad(y, 1, "maximum")

minima_sum = 0
minima_indices = []

for i in range(1, len(y) - 1):
    for j in range(1, len(y[0] - 1)):
        if (
            y[i - 1][j] > y[i][j]
            and y[i + 1][j] > y[i][j]
            and y[i][j + 1] > y[i][j]
            and y[i][j - 1] > y[i][j]
        ):
            minima_indices.append([i, j])
            minima_sum += 1 + y[i][j]
print("Part 1:\t", minima_sum)

seen = np.zeros((len(y), len(y[0])))
seen = np.where(y == 9, 1, seen)

all_basins = []
while minima_indices:
    a, b = minima_indices.pop(0)
    basin_size = 0
    q = [[a, b]]
    while q:
        i, j = q.pop(0)
        if seen[i][j] == 1:
            continue
        seen[i][j] = 1
        basin_size += 1
        if seen[i - 1][j] == 0:
            q.append([i - 1, j])
        if seen[i + 1][j] == 0:
            q.append([i + 1, j])
        if seen[i][j + 1] == 0:
            q.append([i, j + 1])
        if seen[i][j - 1] == 0:
            q.append([i, j - 1])
    all_basins.append(basin_size)

print("Part 2:\t", np.prod(sorted(all_basins)[-3:]))
exit()

check = np.where(seen == 0)
all_basins = []
while len(check[0]) > 0:
    a, b = check[0][0], check[1][0]
    basin_size = 0

    q = [[a, b]]
    while q:
        i, j = q.pop(0)
        if seen[i][j] == 1:
            continue
        seen[i][j] = 1
        basin_size += 1
        if seen[i - 1][j] == 0:
            q.append([i - 1, j])
        if seen[i + 1][j] == 0:
            q.append([i + 1, j])
        if seen[i][j + 1] == 0:
            q.append([i, j + 1])
        if seen[i][j - 1] == 0:
            q.append([i, j - 1])
    all_basins.append(basin_size)
    check = np.where(seen == 0)
print(all_basins)
print("Part 2:\t", np.prod(sorted(all_basins)[-3:]))
