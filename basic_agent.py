import numpy as np
import random

DEBUG = 0

class BasicAgent:
    """
    BasicAgent

    Parameters:
    d (int > 0): The board is a square of size d * d
    n (int between 0 and d ** 2): There are n mines on the board

    Fields:
    revealed (numpy array): The agent's progress exploring the board. The values in a cell mean the following:
        0: Hidden
        1: Explored
    clues (numpy array): The agent's clues for the board so far. The values in a cell mean the following:
        -1: Unknown
        0-8: The number of adjacent mines to the square
    flagged (numpy array): The cells which have been flagged as a mine by the agent. The values in a cell mean the following:
        -1: Flagged as safe
        0: Not flagged as mine
        1: Flagged as mine
    mines_total: same as n in parameters
    """
    def __init__(self, d, n):
        self.revealed = np.zeros((d, d))
        self.clues = np.full((d, d), -1)
        self.flagged = np.zeros((d, d))
        self.mines_total = n
        self.mines_identified = 0

    def query_next(self):
        possible_nexts = []
        for i in range(9):
            for index, val in np.ndenumerate(self.clues):
                if (val == i):
                    (x, y) = index
                    possible_nexts.extend(self.get_neighbors(x, y))
            if len(possible_nexts) > 0:
                (x, y) = random.choice(possible_nexts)
                return (x, y)
        x = random.randrange(0, len(self.clues))
        y = random.randrange(0, len(self.clues))
        return (x, y)

    def get_neighbors(self, x, y):
        neighbors = []
        for i in range(x - 1, x + 2):
            if (i < 0) or (i >= self.revealed.shape[0]):
                continue
            for j in range(y - 1, y + 2):
                if (j < 0) or (j >= self.revealed.shape[1]):
                    continue
                if (i == x) and (j == y):
                    continue
                neighbors.append((i, j))
        return neighbors

    def update_kb(self, x, y, clue):
        if DEBUG:
            print("SAFE CELL, UPDATING KNOWLEDGE BASE")
        self.revealed[x][y] = 1
        self.clues[x][y] = clue
        self.flag_new_mines()

    def flag_new_mines(self):
        for index, val in np.ndenumerate(self.revealed):
            x, y = index
            if self.revealed[x][y] == 0:
                continue
            for i in range(x - 1, x + 2):
                if (i < 0) or (i >= self.flagged.shape[0]):
                    continue
                for j in range(y - 1, y + 2):
                    if (j < 0) or (j >= self.flagged.shape[1]):
                        continue
                    if (i == x) and (j == y):
                        self.flagged[x][y] = -1
                        continue
                    if (self.clues[i][j]) == (self.get_adj_hidden(i, j)):
                        self.set_all_adj_mine(i, j)
                    if (self.mines_total - self.mines_identified) == self.get_adj_hidden(i, j): 
                        self.set_all_adj_mine(i, j)
                    if (8 - self.clues[i][j]) - self.get_adj_safe(i, j) == self.get_adj_hidden(i, j):
                        self.set_all_adj_safe(i, j)

    def get_adj_hidden(self, x, y):
        adj_hidden = 0
        for i in range(x - 1, x + 2):
            if (i < 0) or (i >= self.revealed.shape[0]):
                continue
            for j in range(y - 1, y + 2):
                if (j < 0) or (j >= self.revealed.shape[1]):
                    continue
                if (i == x) and (j == y):
                    continue
                if self.revealed[i][j] == 0:
                    adj_hidden += 1
        return adj_hidden

    def get_adj_safe(self, x, y):
        adj_safe = 0
        for i in range(x - 1, x + 2):
            if (i < 0) or (i >= self.flagged.shape[0]):
                continue
            for j in range(y - 1, y + 2):
                if (j < 0) or (j >= self.flagged.shape[1]):
                    continue
                if (i == x) and (j == y):
                    continue
                if self.flagged[i][j] == -1:
                    adj_safe += 1
        return adj_safe

    def get_adj_mine(self, x, y):
        adj_mine = 0
        for i in range(x - 1, x + 2):
            if (i < 0) or (i >= self.flagged.shape[0]):
                continue
            for j in range(y - 1, y + 2):
                if (j < 0) or (j >= self.flagged.shape[1]):
                    continue
                if (i == x) and (j == y):
                    continue
                if self.flagged[i][j] == 1:
                    adj_mine += 1
        return adj_mine

    def set_all_adj_mine(self, x, y):
        for i in range(x - 1, x + 2):
            if (i < 0) or (i >= self.flagged.shape[0]):
                continue
            for j in range(y - 1, y + 2):
                if (j < 0) or (j >= self.flagged.shape[1]):
                    continue
                if (i == x) and (j == y):
                    continue
                if (self.revealed[i][j] == 0):
                    if DEBUG:
                            print("FLAGGING MINE: x = {}, y = {}".format(i, j))
                    self.flagged[i][j] = 1

    def set_all_adj_safe(self, x, y):
        for i in range(x - 1, x + 2):
            if (i < 0) or (i >= self.flagged.shape[0]):
                continue
            for j in range(y - 1, y + 2):
                if (j < 0) or (j >= self.flagged.shape[1]):
                    continue
                if (i == x) and (j == y):
                    continue
                self.flagged[i][j] = -1


                