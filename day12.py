"""Advent of Code 2021 day 12 """

INPUT_FILE = "input12.txt"


class Cave:
    def __init__(self, a, b):
        self.name = a
        self.neighbours = [b]

    def add_neighbour(self, b):
        if b in self.neighbours:
            return
        self.neighbours.append(b)

    def is_small_cave(self):
        return self.name.islower()


with open(INPUT_FILE) as f:
    input_text = f.readlines()

caves = {}
for line in input_text:
    a, b = line.strip().split("-")
    if a in caves.keys():
        caves[a].add_neighbour(b)
    else:
        caves[a] = Cave(a, b)
    if b in caves.keys():
        caves[b].add_neighbour(a)
    else:
        caves[b] = Cave(b, a)

paths = []
q = [[caves["start"], []]]
while len(q) > 0:
    curr, path = q.pop(0)

    if curr.name == "start" and len(path) > 0:
        continue
    elif curr.name == "end":
        paths.append(path + [curr.name])
        continue
    elif curr.is_small_cave() and curr.name in path:
        continue
    for n in curr.neighbours:
        q.append([caves[n], path + [curr.name]])


print()
print("Part 1:\t", len(paths))


paths = []
q = [[caves["start"], [], False]]
while len(q) > 0:
    curr, path, flag = q.pop(0)

    if curr.name == "start" and len(path) > 0:
        continue
    elif curr.name == "end":
        paths.append(path + [curr.name])
        continue
    elif curr.is_small_cave() and curr.name in path:
        if flag:
            continue
        else:
            flag = True
    for n in curr.neighbours:
        q.append([caves[n], path + [curr.name], flag])


print("Part 2:\t", len(paths))
