""" Advent of Code 2021 day 15 """

import numpy as np

INPUT_FILE = "testinput15.txt"


def get_matrix(input_file):
    input = np.loadtxt(input_file, dtype=str)
    matrix = np.array([[a for a in b] for b in input]).astype(int)
    return matrix


def get_larger_matrix_one_dim(matrix, axis):
    larger_matrix = matrix
    for _ in range(4):
        matrix = matrix + 1
        matrix = np.where(matrix == 10, 1, matrix)
        larger_matrix = np.concatenate((larger_matrix, matrix), axis)
    return larger_matrix


def get_larger_matrix(matrix):
    matrix = get_larger_matrix_one_dim(matrix, 1)
    matrix = get_larger_matrix_one_dim(matrix, 0)
    return matrix


def get_minimal_risk_path(matrix):
    n, m = matrix.shape
    dist = np.full(matrix.shape, np.inf)
    seen = np.full(matrix.shape, False)
    dist[0, 0] = 0

    while True:

        min_unseen = np.amin(np.where(seen == True, np.inf, dist))
        res = np.where((dist == min_unseen) & (seen == False))
        if len(res[0]) == 0:
            break
        curr = (res[0][0], res[1][0])
        # break if curr is end
        if curr == (n - 1, m - 1):
            return dist[curr]
        curr_dist = dist[curr]
        seen[curr] = True

        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x = curr[0] + i
            y = curr[1] + j
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and not seen[x, y]:
                new_dist = curr_dist + matrix[x, y]
                if new_dist < dist[x, y]:
                    dist[x, y] = new_dist


if __name__ == "__main__":
    matrix = get_matrix(INPUT_FILE)
    print("Part 1:\t", get_minimal_risk_path(matrix))

    larger_matrix = get_larger_matrix(matrix)
    print("Part 2:\t", get_minimal_risk_path(larger_matrix))
