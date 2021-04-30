import minesweeper
import basic_agent
import advanced_agent
#import advanced_agent
import numpy as np
import matplotlib.pyplot as plt




dim = 10
n_mines = 30
test_board = minesweeper.generate_board(dim, n_mines)
test_basic_agent = basic_agent.BasicAgent(dim, n_mines)
test_advanced_agent = advanced_agent.AdvancedAgent(dim, n_mines)

score = minesweeper.play_minesweeper(test_board, n_mines, test_advanced_agent)

#print(10 * test_board + test_basic_agent.is_mine)
#print(score)

basic_enabled = 0

if (basic_enabled):
    dim = 10
    n_tests = 100
    scores = np.zeros(9)
    # From 10% mines to 90% mines in 10% steps
    for i in range(9):
        p_mine = ((i + 1) / 10)
        n_mines = int(p_mine * (dim ** 2)) # start low
        print("Running tests for {} mines in {} cells.".format(n_mines, dim ** 2))
        # Simulation loop
        for j in range(n_tests):
            board = minesweeper.generate_board(dim, n_mines)
            agent = basic_agent.BasicAgent(dim, n_mines)
            scores[i] += minesweeper.play_minesweeper(board, n_mines, agent)
        scores[i] /= n_tests
    # Terminal output
    for i in range(len(scores)):
        n_mines = int(((i + 1) / 10) * (dim ** 2))
        print("Basic agent score for {} mines in {}x{} board: {}".format(n_mines, dim, dim, scores[i]))
    # Graphical output
    x = np.arange(0.1, 1, 0.1)
    y = scores
    plt.plot(x,y)
    plt.xlabel("Probability of mine in a cell")
    plt.ylabel("Mines safely identified / total mines")
    plt.title("Basic agent performance: {}x{} board, {} total tests".format(dim, dim, n_tests * 9))
    plt.show()

advanced_enabled = 1

if (advanced_enabled):
    dim = 10
    n_tests = 100
    scores = np.zeros(9)
    # From 10% mines to 90% mines in 10% steps
    for i in range(9):
        p_mine = ((i + 1) / 10)
        n_mines = int(p_mine * (dim ** 2)) # start low
        print("Running tests for {} mines in {} cells.".format(n_mines, dim ** 2))
        # Simulation loop
        for j in range(n_tests):
            board = minesweeper.generate_board(dim, n_mines)

            # COMMENT THIS BACK IN WHEN YOU GET ADVANCED AGENT TO COMPILE

            #agent = advanced_agent.AdvancedAgent(dim, n_mines)
            scores[i] += minesweeper.play_minesweeper(board, n_mines, test_advanced_agent)
        scores[i] /= n_tests

    # Terminal output
    for i in range(len(scores)):
        n_mines = int(((i + 1) / 10) * (dim ** 2))
        print("VIRGIN agent score for {} mines in {}x{} board: {}".format(n_mines, dim, dim, scores[i]))
    # Graphical output
    x = np.arange(0.1, 1, 0.1)
    y = scores
    plt.plot(x,y)
    plt.xlabel("Probability of mine in a cell")
    plt.ylabel("Mines safely identified / total mines")
    plt.title("VIRGIN agent performance: {}x{} board, {} total tests".format(dim, dim, n_tests * 9))
    plt.show()
