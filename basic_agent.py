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

        self.dimension = d
        self.total_mines = n

        # Whether or not cell is mine or safe
        # 0 for unknown
        # 1 for mine
        # 2 for safe
        self.mine_or_safe = np.zeros((d, d))

        # If safe, number of mines surrounding it
        # -1 for unknown
        # 0-8 for mines
        self.clues = np.full((d, d), -1)

        # Number of safe squares adjacent
        self.adj_safe = np.zeros((d, d))

        # Number of mines adjacent
        self.adj_mine = np.zeros((d, d))

        # Number of hidden squares adjacent
        self.adj_hidden = np.zeros((d, d))

        for i in range(d):
            for j in range(d):
                if (i == 0 or i == d - 1) and (j == 0 or j == d - 1):
                    self.adj_hidden[i][j] = 3
                elif (i == 0 or i == d - 1) or (j == 0 or j == d - 1):
                    self.adj_hidden[i][j] = 5
                else:
                    self.adj_hidden = 8

    def query_next(self):
        pass

    def update_kb(self, x, y, clue):
        continue_flag = 1
        while continue_flag:
            continue_flag = 0
            for i in range(self.dimension):
                for j in range(self.dimension):
                    if (self.clues[i][j] - self.adj_mine[i][j] == self.adj_hidden[i][j]):
                        # Every hidden neighbor is a mine
                        self.mark_all_adj_mine(i, j)
                        continue_flag = 1
                    elif ((8 - self.clues[i][j]) - self.adj_safe[i][j] == self.adj_hidden[i][j]):
                        # Every hidden neighbor is safe
                        self.mark_all_adj_safe(i, j)
                        continue_flag = 1               
        return None

    def mark_all_adj_mine(self, i, j):
        pass

    def mark_all_adj_safe(self, i, j):
        pass


                