import numpy as np
import matplotlib.pyplot as plt
import basic_agent

DEBUG = 0

"""
Agent requirements:

Required fields:
safely_flagged (int): The number of mines identified without running into them.

Required functions:
query_next() (returns (x, y)): Function to decide which square the agent wants to go to next.
update_kb(x, y, clue): Function to update the kb with a clue at x, y. Note that clue=-999 if the user just hit a mine.

"""

"""
Generate new board

Parameters:
d (int > 0): The board is a square of size d * d
n (int between 0 and d ** 2): There are n mines on the board

Return:
board (numpy array): a d * d array representing a minesweeper board. Check board[x][y] to check the contents of the board cell. A value of 1 corresponds to a mine. A value of 0 corresponds to a safe square.

Errors:
-1 (int): invalid parameters, see constraints above
"""   
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
    if DEBUG:
        print("START BOARD STARTING CONFIG")
        print(board)
        print("end board starting config")
    return board

"""
Play a game of minesweeper

Parameters:
board (numpy array): An array created by generate_board()
agent: An instance of a class with logic to play the game.

Return:
score (int): The number of mines flagged successfully before the agent dies.
"""
def play_minesweeper(board, agent):
    #for the amount of mines
    for _ in range(board.size - agent.total_mines):
        #query next square to select to choose as a square to open up
        #this means we don't believe that square is a mine
        (x, y) = agent.query_next()
        if DEBUG:
            print("QUERY SELECTION: x = {}, y = {}, val = {}".format(x, y, board[x][y]))
        #if the square is a mine, we update our list of mine knowledge
        if board[x][y] == 1:
            #print("HIT A MINE AT: x = {}, y = {}".format(x, y))
            agent.update_kb(x, y, -999)
        #if we are correct, and it is not a mine
        #we will update the knowledge base to say how many mines are contained in this square
        agent.update_kb(x, y, get_clue(board, x, y)) 
    return calculate_score(board, agent)

"""
Get a clue from a given position on the board

Parameters:
board (numpy array): An array created by generate_board().
x (int): The x-coordinate to get a clue for.
y (int): The y-coordinate to get a clue for.

Return:
clue (int): The number of adjacent mines to the square.
"""
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

"""
Calculate the score from a game

Parameters:
board (numpy array): An array created by generate_board()
agent: An instance of a class with logic to play the game.

Return:
score (int): The number of mines flagged successfully before the agent dies.
"""
def calculate_score(board, agent):
    """
    score = 0
    for index, val in np.ndenumerate(board):
        if val == 1:
            (x, y) = index
            if agent.mine_or_safe[x][y] == 1:
                score += 1
    return score
    """
    return agent.safely_marked


"""
START TESTING
"""

dimension = 10
n_mines = 30
num_tests = 1
scores = [0] * num_tests
for i in range(num_tests):
    board1 = generate_board(dimension, n_mines)
    agent1 = basic_agent.BasicAgent(dimension, n_mines)
    score = play_minesweeper(board1, agent1)
    scores[i] = score
print(scores)
actual_score = 0


"""
testboard = np.zeros((4, 4))
testboard[0][0] = 1
testboard[2][3] = 1
print(testboard)

testagent = basic_agent.BasicAgent(4, 2)
score = play_minesweeper(testboard, testagent)
print(score)
"""