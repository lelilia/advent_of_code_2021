with open("input3.txt") as f:
    input = f.readlines()

def find_most_common(input, index):
    entry = [a[index] for a in input]
    one = entry.count("1")
    zero = entry.count("0")
    if one > zero:
        return 1
    elif one < zero:
        return 0
    return 2


gamma = ""
epsilon = ""

for i in range(len(input[0])):
    most_common = find_most_common(input, i)
    if most_common != 2:
        gamma += str(most_common)
        epsilon += str((most_common + 1) % 2)

print ("Part 1:\t", int(gamma, 2) * int(epsilon, 2))


ox = input.copy()
i = 0
while len(ox) > 1 and i < len(input[0]):

    entry = [a[i] for a in ox]
    number_one = entry.count("1")
    number_zero = entry.count("0")
    if number_one >= number_zero and len(ox) > 1:
        ox = [a for a in ox if a[i] == "1"]
    elif number_one < number_zero and len(ox) > 1:
        ox = [a for a in ox if a[i] == "0"]
    else:
        break

    i += 1



co2 = input.copy()

i = 0

while len(co2) > 1 and i < len(input[0]):

    entry = [a[i] for a in co2]
    number_one = entry.count("1")
    number_zero = entry.count("0")
    if number_one < number_zero and len(co2) > 1:
        co2 = [a for a in co2 if a[i] == "1"]
    elif number_one >= number_zero and len(co2) > 1:
        co2 = [a for a in co2 if a[i] == "0"]
    else:
        break

    i += 1


print("Part 2:\t", int(ox[0], 2) * int(co2[0],2))