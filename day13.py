import numpy as np

INPUT_FILE = "input13.txt"

with open(INPUT_FILE) as f:
    input_txt = f.read()

dots, folds = input_txt.strip().split("\n\n")
paper = {}

for dot in dots.strip().split("\n"):
    x, y = dot.split(",")
    paper[int(x), int(y)] = 1

for i, fold in enumerate(folds.strip().split("\n")):
    _, _, instructions = fold.split()
    direction, foldline = instructions.split("=")
    foldline = int(foldline)
    new_dict = {}
    if direction == "x":
        for key, value in paper.items():
            if value == 0:
                continue
            x, y = key
            if x <= foldline:
                new_dict[(x, y)] = paper[(x, y)]
            if x > foldline:
                new_dict[(2 * foldline - x, y)] = 1
    elif direction == "y":
        for key, value in paper.items():
            if value == 0:
                continue
            x, y = key
            if y <= foldline:
                new_dict[(x, y)] = paper[(x, y)]
            if y > foldline:
                new_dict[(x, 2 * foldline - y)] = 1
    if i == 0:
        print("Part 1:\t", sum(new_dict.values()))

    paper = new_dict.copy()


decode = np.full((6, 40), " ")
for key in paper.keys():
    x, y = key
    decode[y][x] = "#"

print("Part 2:")
print("\n".join(["".join(decode[i, :]) for i in range(6)]))
