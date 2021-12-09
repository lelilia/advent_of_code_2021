import numpy as np


INPUT_FILE = "input9.txt"

input = np.loadtxt(INPUT_FILE, dtype=str)
y = np.array([[a for a in b] for b in input]).astype(int)


minima_sum = 0
y = np.pad(y, 1, "maximum")


for i in range(1, len(y) - 1):
    for j in range(1, len(y[0]- 1)):
        if y[i-1][j] > y[i][j] and y[i+1][j] > y[i][j] and y[i][j+1] > y[i][j] and y[i][j-1] > y[i][j]:
            minima_sum += 1 + y[i][j]
print("Part 1:\t",minima_sum)

seen = np.zeros((len(y), len(y[0])))
seen = np.where(y==9, 1, seen)

check = np.where(seen == 0)
all_basins = []
while len(check[0]) > 0:
    i, j = check[0][0], check[1][0]
    basin_size = 0

    q = [[i, j]]
    seen[i][j] = 1
    while q:
        i, j = q.pop(0)
        seen[i][j] = 1
        basin_size += 1
        if seen[i-1][j] == 0 and [i-1, j] not in q:
            q.append([i-1,j])
        if seen[i+1][j] == 0 and [i + 1, j] not in q:
            q.append([i+1, j])
        if seen[i][j+1] == 0 and [i, j+1] not in q:
            q.append([i, j+1])
        if seen[i][j-1] == 0 and [i, j - 1] not in q:
            q.append([i, j-1])
    all_basins.append(basin_size)
    check = np.where(seen == 0)

print("Part 2:\t", np.prod(sorted(all_basins)[-3:]))
