import numpy as np

DEBUG = 1

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
        for index, val in np.ndenumerate(self.revealed):
            if val == 0:
                (x, y) = index
                if self.flagged[x][y] == -1:
                    return (x, y)
        for index, val in np.ndenumerate(self.revealed):
            if val == 0:
                (x, y) = index
                if self.flagged[x][y] == 0:
                    return (x, y)
        return -1

    def update_kb(self, x, y, clue):
        self.revealed[x][y] = 1
        self.clues[x][y] = clue
        # Flag new mines
        for i in range(x - 1, x + 2):
            if (i < 0) or (i >= self.flagged.shape[0]):
                continue
            for j in range(y - 1, y + 2):
                if (j < 0) or (j >= self.flagged.shape[1]):
                    continue
                if (i == x) and (j == y):
                    self.flagged[x][y] = -1
                    continue
                if (self.mines_total - self.mines_identified) == self.get_adj_hidden(i, j):
                    if DEBUG:
                        print("FLAGGING MINE: x = {}, y = {}".format(i, j))
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

    def set_all_adj_mine(self, x, y):
        for i in range(x - 1, x + 2):
            if (i < 0) or (i >= self.flagged.shape[0]):
                continue
            for j in range(y - 1, y + 2):
                if (j < 0) or (j >= self.flagged.shape[1]):
                    continue
                if (i == x) and (j == y):
                    continue
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


                