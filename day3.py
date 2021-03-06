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

print("Part 1:\t", int(gamma, 2) * int(epsilon, 2))


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

print("Part 2:\t", int(ox[0], 2) * int(co2[0], 2))

print("------")
print()

# second attempt
from statistics import mode
import numpy as np

INPUT_FILE = "input3.txt"

matrix = np.loadtxt(INPUT_FILE, dtype=str)
matrix = np.array([list(binary_string) for binary_string in matrix]).astype(int)


def get_int(string):
    """return the int value of a binary string"""
    return int(string, 2)


def get_string(array):
    """return the string for the array"""
    return "".join([str(x) for x in array])


def get_gamma_and_epsilon(matrix):
    gamma = [mode(matrix[:, i]) for i in range(matrix[0].size)]
    gamma = get_string(gamma)
    string_length = len(gamma)
    gamma = get_int(gamma)
    epsilon = 2 ** string_length - 1 - gamma
    return gamma, epsilon


def get_reduced(matrix_original, bias):
    matrix = matrix_original.copy()
    number_of_columns = matrix[0].size
    for i in range(number_of_columns):
        matrix_length = len(matrix)
        mode = sum(matrix[:, i]) / matrix_length * 2 // 1
        if matrix_length > 1:
            matrix = matrix[matrix[:, i] == (mode + bias) % 2]
    co2_string = get_string(matrix[0])
    return get_int(co2_string)


gamma, epsilon = get_gamma_and_epsilon(matrix)

print("Part 1:\t", gamma * epsilon)

oxygen = get_reduced(matrix, 0)
co2 = get_reduced(matrix, 1)

print("Part 2:\t", oxygen * co2)
