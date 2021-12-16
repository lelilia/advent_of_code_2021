""" Advent of Code 2021 day 16 """

import numpy as np

INPUT_FILE = "input16.txt"


def get_version(binary):
    v, binary = binary[:3], binary[3:]
    return int(v, 2), binary


def get_type(binary):
    t, binary = binary[:3], binary[3:]
    return int(t, 2), binary


def parse_packages(binary):
    packet = ""
    while True:
        start, binary = binary[:1], binary[1:]
        packet, binary = packet + binary[:4], binary[4:]
        if start == "0":
            return int(packet, 2), binary


def get_length_id(binary):
    i, binary = binary[:1], binary[1:]
    return int(i, 2), binary


def get_length(binary, length):
    l, binary = binary[:length], binary[length:]
    return int(l, 2), binary


def get_number_packages(binary, length):
    number, binary = binary[:length], binary[length:]
    return int(number, 2), binary


def parse_package(binary):
    global sum_versions
    v, binary = get_version(binary)

    sum_versions += v
    t, binary = get_type(binary)
    if t == 4:
        packet, binary = parse_packages(binary)
        return packet, binary
    else:
        packages = []
        packet = None
        i, binary = get_length_id(binary)
        if i == 0:
            length = 15
            l, binary = get_length(binary, length)
            sub_packages, binary = binary[:l], binary[l:]
            while sub_packages:
                packet, sub_packages = parse_package(sub_packages)
                packages.append(packet)
        else:
            length = 11
            number, binary = get_number_packages(binary, length)
            for _ in range(number):
                packet, binary = parse_package(binary)
                packages.append(packet)
        if t == 0:
            packet = sum(packages)
        elif t == 1:
            packet = np.prod(packages)
        elif t == 2:
            packet = min(packages)
        elif t == 3:
            packet = max(packages)
        elif t == 5:
            packet = 1 if packages[0] > packages[1] else 0
        elif t == 6:
            packet = 1 if packages[0] < packages[1] else 0
        elif t == 7:
            packet = 1 if packages[0] == packages[1] else 0
    return packet, binary


with open(INPUT_FILE) as f:
    input = f.read()

sum_versions = 0
binary = bin(int(input, 16))[2:].zfill((len(input) - 1) * 4)

res, packages = parse_package(binary)
print("Part 1:\t", sum_versions)
print("Part 2:\t", res)
