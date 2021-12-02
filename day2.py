""" Advent of Code 2021 day 2 """

with open("input2.txt") as f:
    directions = f.readlines()

x = 0
y = 0
for direction in directions:
    command, steps = direction.split()
    if command == "forward":
        x += int(steps)
    elif command == "down":
        y += int(steps)
    else:
        y -= int(steps)

print("Part 1:\t", x * y)

aim = 0
x = y = 0
for direction in directions:
    command, steps = direction.split()
    if command == "down":
        aim += int(steps)
    elif command == "up":
        aim -= int(steps)
    else:
        x += int(steps)
        y += aim * int(steps)
print("Part 2:\t", x * y)
