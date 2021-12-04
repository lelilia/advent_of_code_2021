""" Advent of Code 2021 day 4 """
import numpy as np

INPUT_FILE = "input4.txt"

with open(INPUT_FILE) as f:
    input = f.read()


class Board():
    def __init__(self, string):
        self.board = np.fromstring(string, dtype=int, sep=" ")
        self.board.resize((5,5))
        self.seen = []

    def check_number(self, number):
        result = np.where(self.board == number)
        if len(result[0]) > 0:
            self.board[result[0][0],result[1][0]] = 10000

    def check_win(self):
        return self.check_win_row() or self.check_win_col()

    def check_win_row(self):
        for i in range(5):
            if np.sum(self.board[i, :]) == 50000:
                return True
        return False

    def check_win_col(self):
        for i in range(5):
            if np.sum(self.board[:, i]) == 50000:
                return True
        return False

    def sum(self):
        return self.board.sum()

class Boards():
    def __init__(self, input):
        self.numbers = None
        self.boards = []
        self.read_input(input)

    def read_input(self, input):
        numbers, *boards = input.split("\n\n")
        self.numbers = numbers.split(",")
        self.get_boards(boards)

    def get_boards(self, boards):
        for board in boards:
            b = Board(board)
            self.boards.append(b)
            b.check_number(1)

class BoardsPart1(Boards):
    def __init__(self, input):
        super().__init__(input)
        self.play_numbers()

    def play_numbers(self):
        for number in self.numbers:
            for board in self.boards:
                board.check_number(int(number))
            for board in self.boards:
                if board.check_win():
                    print("Part 1:\t", int(number) * (board.sum() % 10000))
                    return

class BoardsPart2(Boards):
    def __init__(self, input):
        super().__init__(input)
        self.pick_last()

    def pick_last(self):
        for number in self.numbers:

            for board in self.boards:
                board.check_number(int(number))
            for board in self.boards:
                if board.check_win():
                    self.boards.remove(board)
            if len(self.boards) == 0:

                print("Part 2:\t", int(number) * (board.sum() % 10000))
                return


BoardsPart1(input)
BoardsPart2(input)
