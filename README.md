# CS440_Minesweeper

Peter Tilton and Mayank Singamreddy

Due 20 Mar 2021

## Work distribution

- Step 1: Environment and agent structure (Peter)
- Step 2: Basic agent algorithm (Peter)
- Step 3: Improved agent (Mayank)
- Step 4: Writeup (Both)
## Bonus points

- EXTRA CREDIT: 15 points for LaTeX
- EXTRA CREDIT: 5 points for clever acronym
- EXTRA CREDIT: 10 points for new plot of density vs. average final score using global information (number of mines on board)
- EXTRA CREDIT: 15 points for new plot density vs. average final score using better decisions than random

## Program specification

Components:

- **Environment**: Represents the board and where the mines are located.
    - Parameter *d*: Board is of shape *d* x *d*.
    - Parameter *n*: Number of mines to put on the board.
    - Creates a board where 0 means no mine and 1 means mine.
- **Agent**: The entity that moves around the maze.
    - A correctly operating agent should not flag a cell as mined when it does not have a mine.
    - The game ends when the agent queries a cell with a mine in it. Final score is the number of mines safely identified.

Procedure:

1. The agent decides which cell to query.
2. The agent queries a location in the environment.
3. The environment reports back whether or not there is a mine there. If not, it reports the number of surrounding cells that are mines.
4. The agent saves this information to a knowledge base.
5. The agent performs inferences to generate new information.

## Basic agent algorithm for comparison

- For the agent, keep track of:
    - *n_identified*: overall number of identified mines.
- For each cell, keep track of:
    - *status*: "mine", "safe", or "hidden".
    - *adj_mines*: number of mines surrounding the cell.
    - *adj_safe*: number of safe squares surrounding the cell.
    - *adj_identified_mines*: number of identified mines surrounding the cell.
    - *adj_hidden*: number of hidden squares around the cell.
- If, for a given cell, *n* - *n_identified* = *adj_hidden*, every adjacent cell is a mine.
- If, for a given cell, (8 - *adj_mines*) - *adj_safe* = *adj_hidden*, every adjacent cell is safe.
- If a cell is identified as safe, reveal it and update your information.
- If a cell is identified as a mine, reveal it and update your information.
- Reapeat above steps until no more hidden cells can be conclusively identified.
- If no hidden cells can be conclusively identified, pick one randomly.

## An improved agent

- We should make an improved agent which uses methods of inference and proof to combine clues.
- Knowledge includes:
    - Whether or not a cell has been revealed.
    - Whether or not a revealed cell is a mine or safe.
    - Clue number revealed for a safe cell.
    - Inferred relationships between cells.

## Questions and writeup

Just read from the assignment doc, I don't wanna write it all here.


