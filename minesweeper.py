import numpy as np
import basic_agent

DEBUG = 1

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
    if (d < 0) or (n < 1) or (n > d ** 2):
        return -1
    # 0 corresponds to empty space
    board = np.zeros(d ** 2)
    for i in range(int(n)):
        # 1 corresponds to a mine
        board[i] = 1
    np.random.shuffle(board)
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
    for _ in range(board.size - agent.mines_total):
        (x, y) = agent.query_next()
        if DEBUG:
            print("QUERY SELECTION: x = {}, y = {}, val = {}".format(x, y, board[x][y]))
        if board[x][y] == 1:
            break
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
    score = 0
    for index, val in np.ndenumerate(board):
        if val == 1:
            (x, y) = index
            if agent.flagged[x][y] == 1:
                score += 1
    return score


"""
START TESTING
"""

test_d = 10
test_n = 10
reps = 100
scores = [0] * reps
for i in range(reps):
    test_board = generate_board(test_d, test_n)
    test_agent = basic_agent.BasicAgent(test_d, test_n)
    scores[i] = play_minesweeper(test_board, test_agent)
print(scores)