import minesweeper
import basic_agent

dim = 10
n_mines = 30
test_board = minesweeper.generate_board(dim, n_mines)
test_agent = basic_agent.BasicAgent(dim, n_mines)

minesweeper.play_minesweeper(test_board, n_mines, test_agent)

