import numpy as np
import random

class BasicAgent:
    def __init__(self, d, n): 
        self.d = d
        self.n = n
        self.score = 0

        self.revealed = np.zeros((d, d))
        self.is_mine = np.zeros((d, d))
        self.is_safe = np.zeros((d, d))

        self.clues = np.full((d, d), np.NaN)

        self.n_hidden = d ** 2

    def query_next(self):
        
        # Investigate next hidden square known to be safe
        for i in range(self.d):
            for j in range(self.d):
                if (self.revealed[i][j] == 0) and (self.is_safe[i][j] == 1):
                    return (i, j)

        # Choose a random hidden square
        target = random.randrange(0, self.n_hidden)
        counter = 0
        for i in range(self.d):
            for j in range(self.d):
                if (self.revealed[i][j] == 0):
                    if (counter == target):
                        return (i, j)
                    else:
                        counter += 1
        
        # No safe options left
        return -1

    def update_kb(self, x, y, clue):

        # Instant knowledge gain
        if (clue == "mine"):
            # Hit a mine
            self.is_mine[x][y] = 1
            self.revealed[x][y] = 1
            self.n_hidden -= 1
        else:
            self.clues[x][y] = clue
            self.is_safe[x][y] = 1
            self.revealed[x][y] = 1
            self.n_hidden -= 1

        # Reevaluation with new knowledge
        do_another_loop = 1
        while(do_another_loop):
            do_another_loop = 0
            for i in range(0, self.d):
                for j in range(0, self.d):

                    # Get values for checks
                    adj_any, adj_mine, adj_safe, adj_hidden = self.count_adjacent(i, j)
                    cur_clue = self.clues[i][j]

                    # Check to see if all adjacent are mines
                    if (cur_clue - adj_mine == adj_hidden):
                        self.set_adjacent(i, j, "mine")

                    # Check to see if all adjacent are safe
                    if ((adj_any - cur_clue) - adj_safe == adj_hidden):
                        self.set_adjacent(i, j, "safe")
        
        return None

    def count_adjacent(self, x, y):
        adj_any = 0
        adj_mine = 0
        adj_safe = 0
        adj_hidden = 0
        for i in range(x - 1, x + 2):
            if (i < 0) or (i >= self.d):
                continue
            for j in range(y - 1, y + 2):
                if (j < 0) or (j >= self.d):
                    adj_any += 1
                    if (self.is_mine[i][j] == 1):
                        adj_mine += 1
                        # Mine safely identified add to score
                        self.score += 1
                    if (self.is_safe[i][j] == 1):
                        adj_safe += 1
                    if (self.revealed[i][j] == 0):
                        adj_hidden += 1
        return adj_any, adj_mine, adj_safe, adj_hidden

    def set_adjacent(self, x, y, mode):
        for i in range(x - 1, x + 2):
            if (i < 0) or (i >= self.d):
                continue
            for j in range(y - 1, y + 2):
                if (j < 0) or (j >= self.d):
                    if (mode == "mine"):
                        self.is_mine[i][j] = 1
                    if (mode == "safe"):
                        self.is_safe[i][j] = 1
        return None

    def get_score(self):
        return self.score / self.n
