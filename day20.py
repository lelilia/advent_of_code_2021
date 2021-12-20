""" Advent of Codee 2021 day 20 """

import numpy as np

INPUT_FILE = "input20.txt"

MASK = np.array([[256, 128, 64], [32, 16, 8], [4, 2, 1]])


def get_input(input_file):
    with open(input_file) as f:
        algo, data = f.read().strip().split("\n\n")

    algo = get_algo(algo)
    matrix = get_matrix(data.split("\n"))
    return algo, matrix


def get_matrix(matrix_data):
    matrix = np.array([[a for a in b] for b in matrix_data])
    matrix = np.where(matrix == ".", 0, matrix)
    matrix = np.where(matrix == "#", 1, matrix).astype(int)
    return matrix


def get_algo(algo_data):
    return algo_data.replace("#", "1").replace(".", "0")


def run_n_steps(n, matrix, algo):
    for step in range(n):
        padding_value = int(algo[0]) if step % 2 == 1 else int(algo[511])
        matrix = np.pad(matrix, 2, constant_values=padding_value)
        new_matrix = np.zeros(matrix.shape, dtype=int)

        for i in range(1, len(matrix) - 1):
            for j in range(1, len(matrix[0]) - 1):
                index = np.sum(MASK * matrix[i - 1 : i + 2, j - 1 : j + 2])
                new_matrix[i, j] = int(algo[index])
        matrix = new_matrix[1:-1, 1:-1].copy()
    return np.sum(matrix)


if __name__ == "__main__":
    algo, matrix = get_input(INPUT_FILE)
    print("Part 1:\t", run_n_steps(2, matrix, algo))
    print("Part 2:\t", run_n_steps(50, matrix, algo))
