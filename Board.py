from copy import deepcopy
from os import system
from random import randint, seed


MAX_COL = 4
MAX_ROW = 4
SHUFFLE_MAGNITUDE = 10


class Board:
    """Models the board for our game"""

    def __init__(self):
        """Construct the board"""
        self.goal = [[" 1", " 2", " 3", " 4"],
                     [" 5", " 6", " 7", " 8"],
                     [" 9", "10", "11", "12"],
                     ["13", "14", "15", "__"]]

        self.board = deepcopy(self.goal)

        self.e_loc = [MAX_ROW - 1, MAX_COL - 1]

        self.moves = {0: self.move_up, 1: self.move_down, 2: self.move_right, 3: self.move_left}

    def __repr__(self):
        """Represent the board"""
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                print(self.board[i][j], end=" ")
            print()
        return ""

    def refresh(self):
        """Clear this screen and print the board"""

        system("clear")
        print('Welcome to the game of the Fifteen\n')
        print(self)

        if self.board == self.goal:
            print('\nCongrats! You Won!')
            return False

        return True

    def shuffle(self):
        """Randomizes board using succession of legal moves"""
        seed()
        for i in range(SHUFFLE_MAGNITUDE):
            m = randint(0, 3)
            self.moves[m](self.board, self.e_loc)

        # optionally move the empty space to the lower right corner
        for i in range(MAX_ROW):
            self.moves[2](self.board, self.e_loc)

        for i in range(MAX_COL):
            self.moves[1](self.board, self.e_loc)

    def move(self, board, e_loc, x, y):
        """Make legal move"""

        if e_loc[0] + x < 0 or e_loc[0] + x > 3 or e_loc[1] + y < 0 or e_loc[1] + y > 3:
             return board, e_loc
        # swap
        board[e_loc[0]][e_loc[1]], board[e_loc[0] + x][e_loc[1] + y] = \
            board[e_loc[0] + x][e_loc[1] + y], board[e_loc[0]][e_loc[1]]

        e_loc[0] += x
        e_loc[1] += y
        return board, e_loc

    def move_up(self, board, e_loc):
        return self.move(board, e_loc, -1, 0)

    def move_down(self, board, e_loc):
        return self.move(board, e_loc, 1, 0)

    def move_right(self, board, e_loc):
        return self.move(board, e_loc, 0, 1)

    def move_left(self, board, e_loc):
        return self.move(board, e_loc, 0, -1)

    def solve(self):
        """Solves the game using BSF algorithm"""
        #self.board = deepcopy(self.goal)

