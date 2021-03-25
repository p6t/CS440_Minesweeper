import minesweeper
import basic_agent
import numpy as np


"""

dim = 10
n_mines = 30
test_board = minesweeper.generate_board(dim, n_mines)
test_agent = basic_agent.BasicAgent(dim, n_mines)

score = minesweeper.play_minesweeper(test_board, n_mines, test_agent)

print(10 * test_board + test_agent.is_mine)
print(score)

"""

dim = 10
scores = np.zeros(5)
n_tests = 10
for n_mines in range(1, 51, 10):
    index = int((n_mines - 1) / 10)
    for _ in range(n_tests):
        board = minesweeper.generate_board(dim, n_mines)
        agent = basic_agent.BasicAgent(dim, n_mines)
        scores[index] += minesweeper.play_minesweeper(board, n_mines, agent)
    scores[index] /= n_tests
for i in range(len(scores)):
    print("Score for {} mines in {}x{} board: {}".format((i * 10) + 1, dim, dim, scores[i]))
