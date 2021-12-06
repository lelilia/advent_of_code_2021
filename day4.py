""" Advent of Code 2021 day 4 """
import numpy as np

INPUT_FILE = "input4.txt"

with open(INPUT_FILE) as f:
    input = f.read()


class Board:
    def __init__(self, string):
        self.board = np.fromstring(string, dtype=int, sep=" ")
        self.board.resize((5, 5))
        self.seen = []

    def set_number(self, number):
        self.board = np.where(self.board == number, 10000, self.board)

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


class Boards:
    def __init__(self, input):
        self.numbers = None
        self.boards = []
        self.winners = []
        self.read_input(input)
        self.find_winner()

    def read_input(self, input):
        numbers, *boards = input.split("\n\n")
        self.numbers = [int(x) for x in numbers.split(",")]
        self.get_boards(boards)

    def get_boards(self, boards):
        for board in boards:
            b = Board(board)
            self.boards.append(b)

    def find_winner(self):
        while len(self.numbers) > 0:
            number = self.numbers.pop(0)
            for board in self.boards:
                board.set_number(number)
                if board.check_win():
                    self.winners.append(number * (board.sum() % 10000))
                    self.boards.remove(board)


b = Boards(input)
print("Part 1:\t", b.winners[0])
print("Part 2:\t", b.winners[-1])
