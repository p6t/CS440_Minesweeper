import numpy as np
import random

DEBUG = 0

class BasicAgent:
    def __init__(self, d, n): 

        self.dimension = d
        self.total_mines = n
        self.safely_marked = 0

        # if hidden
        # 1 if revealed
        self.revealed = np.zeros((d, d))

        # Whether or not cell is mine or safe
        # 0 for unknown
        # 1 for mine
        # 2 for safe
        self.mine_or_safe = np.zeros((d, d))

        # If safe, number of mines surrounding it
        # -999 for unknown
        # 0-8 for mines
        self.clues = np.full((d, d), -999)

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
                elif (i == 0 or i == d - 1):
                    self.adj_hidden[i][j] = 5
                elif (j == 0 or j == d - 1):
                    self.adj_hidden[i][j] = 5
                else:
                    self.adj_hidden[i][j] = 8

    def query_next(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if (self.mine_or_safe[i][j] == 2):
                    return (i, j)
        return self.random_hidden_selection()

    def update_kb(self, x, y, clue):
        if(clue == -999):
            # Hit a mine
            self.mine_or_safe[x][y] = 1
        else:
            self.clues[x][y] = clue
            self.mine_or_safe[x][y] = 2
            self.revealed[x][y] = 1
        #print(self.clues)
        
        continue_flag = 1
        while continue_flag:
            #print("A LOOP")
            continue_flag = 0
            for i in range(self.dimension):
                for j in range(self.dimension):
                    #print("CLUE, LOCATION: {}, ({}, {})".format(self.clues[i][j], i, j))
                    #print("SAFE CLAUSE EVAL: {} of {}".format((8 - self.clues[i][j]) - self.adj_safe[i][j], self.adj_hidden[i][j]))
                    #print("MINE CLAUSE EVAL: {} of {}".format(self.clues[i][j] - self.adj_mine[i][j], self.adj_hidden[i][j]))
                    if (self.clues[i][j] - self.adj_mine[i][j] == self.adj_hidden[i][j]):
                        # Every hidden neighbor is a mine
                        print("MARK ALL ADJACENT MINE")
                        self.mark_all_adj_mine(i, j)
                        self.update_adj_mine(i, j)
                        self.update_adj_hidden(i, j)
                        continue_flag = 1
                    elif ((self.num_adj(i, j) - self.clues[i][j]) - self.adj_safe[i][j] == self.adj_hidden[i][j]):
                        #print("Uh oh")
                        # Every hidden neighbor is safe
                        print("MARK ALL ADJACENT SAFE")
                        if (self.mine_or_safe[i][j] != 2):
                            continue_flag = 1 
                        self.mark_all_adj_safe(i, j)
                        self.update_adj_safe(i, j)
                        self.update_adj_hidden(i, j)           
        return None

    def num_adj(self, i, j):
        if (i == 0 or i == self.dimension - 1) and (j == 0 or j == self.dimension - 1):
            return 3
        if (i == 0 or i == self.dimension - 1) or (j == 0 or j == self.dimension - 1):
            return 5
        return 8

    def mark_all_adj_mine(self, x, y):
        for i in range(x-1, x+1):
            if (i < 0 or i >= self.dimension):
                continue
            for j in range(y-1, y+1):
                if (j < 0 or j >= self.dimension):
                    continue
                if (self.mine_or_safe[i][j] == 0):
                    self.mine_or_safe[i][j] == 1
                    self.safely_marked += 1
        return None

    def mark_all_adj_safe(self, x, y):
        for i in range(x-1, x+1):
            if (i < 0 or i >= self.dimension):
                continue
            for j in range(y-1, y+1):
                if (j < 0 or j >= self.dimension):
                    continue
                if (self.mine_or_safe[i][j] == 0):
                    self.mine_or_safe[i][j] == 2
        return None

    def update_adj_hidden(self, x, y):
        new_val = 0
        for i in range(x-1, x+1):
            if (i < 0 or i >= self.dimension):
                continue
            for j in range(y-1, y+1):
                if (j < 0 or j >= self.dimension):
                    continue
                if (self.revealed[i][j] == 0):
                    new_val += 1
        self.adj_hidden[x][y] = new_val
        return None

    def update_adj_mine(self, x, y):
        new_val = 0
        for i in range(x-1, x+1):
            if (i < 0 or i >= self.dimension):
                continue
            for j in range(y-1, y+1):
                if (j < 0 or j >= self.dimension):
                    continue
                if (self.mine_or_safe[i][j] == 1):
                    new_val += 1
        self.adj_mine[x][y] = new_val
        return None

    def update_adj_safe(self, x, y):
        new_val = 0
        for i in range(x-1, x+1):
            if (i < 0 or i >= self.dimension):
                continue
            for j in range(y-1, y+1):
                if (j < 0 or j >= self.dimension):
                    continue
                if (self.mine_or_safe[i][j] == 2):
                    new_val += 1
        self.adj_safe[x][y] = new_val
        return None

    def random_hidden_selection(self):
        num_hidden = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if (self.mine_or_safe[i][j] == 0):
                    num_hidden += 1
        selection_index = random.randint(0, num_hidden - 1)
        #print("SELECTION INDEX: {} of {}".format(selection_index, num_hidden))
        n = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if (self.mine_or_safe[i][j] == 0):
                    if (n == selection_index):
                        return (i, j)
                    n += 1
        return -1

                