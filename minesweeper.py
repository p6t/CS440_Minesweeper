import numpy as np
import matplotlib.pyplot as plt

def generate_board(d, n):
    # Check inputs
    #if board dim is less than one (zero or below)
    #if amount of mines is less than zero (any negative number)
    if (d < 1) or (n < 0) or (n > d ** 2):
        return -1
    # 0 corresponds to empty space
    #fill board with zero values for empty spaces
    board = np.zeros(d ** 2)
    #add n bombs
    for i in range(int(n)):
        # 1 corresponds to a mine
        board[i] = 1
    #shuffle the order of the bombs in the array
    np.random.shuffle(board)
    #make the array a 2D array
    board = board.reshape((d, d))
    return board

def play_minesweeper(board, total_mines, agent):
    """
    Agent must have the following functions:

    agent.query_next(): returns (x, y) int tuple for where to look in the board next
    agent.update_kb(x, y, clue): gives the agent the clue value at (x, y) (or the string "mine" if the agent selected a mine). This is  enough info to update the knowledge base.
    agent.get_score(): returns a float equal to the number of mines safely identified over the total number of mines
    """
    for _ in range(board.size - total_mines):
        #query next square to select to choose as a square to open up
        #this means we don't believe that square is a mine
        (x, y) = agent.query_next()

        #if the square is a mine, we update our list of mine knowledge
        if board[x][y] == 1:
            #print("HIT A MINE AT: x = {}, y = {}".format(x, y))
            agent.update_kb(x, y, "mine")
        #if we are correct, and it is not a mine
        #we will update the knowledge base to say how many mines are contained in this square
        agent.update_kb(x, y, get_clue(board, x, y)) 

    return agent.get_score()

def get_clue(board, x, y):
    clue = 0
    for i in range(x - 1, x + 2):
        if (i < 0) or (i >= board.shape[0]):
            continue
        for j in range(y - 1, y + 2):
            if (j < 0) or (j >= board.shape[1]):
                continue
            if (i == x) and (j == y):
                continue
            clue += board[i][j]
    return clue