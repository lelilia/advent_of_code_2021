""" Advent of Code 2021 day 14 """

INPUT_FILE = "input14.txt"


def read_input(filename):
    with open(filename) as f:
        input_text = f.read()
    return input_text


def parse_input(input_text):
    polymere_string, _, *instructions = input_text.strip().split("\n")
    polymere = {}
    rules = {}

    for instruction in instructions:
        left, right = instruction.strip().split(" -> ")
        rules[left] = [left[0] + right, right + left[1]]

    for i in range(len(polymere_string) - 1):
        substr = polymere_string[i : i + 2]
        if substr in polymere:
            polymere[substr] += 1
        else:
            polymere[substr] = 1

    first = polymere_string[0:2]
    last = polymere_string[-2:]
    return rules, polymere, first, last


def run_n_times(n, rules, polymere, first, last):
    for _ in range(n):
        new_polymere = {}
        for key, value in polymere.items():
            for k in rules[key]:
                if k in new_polymere:
                    new_polymere[k] += value
                else:
                    new_polymere[k] = value
        first = rules[first][0]
        last = rules[last][1]
        polymere = new_polymere.copy()
    return polymere, first, last


def count_difference(polymere, first, last):
    counter = {}
    for key, value in polymere.items():
        for char in key:
            if char in counter:
                counter[char] += value / 2
            else:
                counter[char] = value / 2

    counter[first[0]] += 0.5
    counter[last[1]] += 0.5

    return int(max(counter.values()) - min(counter.values()))


def find_difference(input, times):
    input = read_input(input)
    rules, polymere, first, last = parse_input(input)
    polymere, first, last = run_n_times(times, rules, polymere, first, last)

    return count_difference(polymere, first, last)


if __name__ == "__main__":

    print("Part 1:\t", find_difference(INPUT_FILE, 10))

    print("Part 2:\t", find_difference(INPUT_FILE, 40))
