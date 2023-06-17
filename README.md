# Tictactoe
This is a CS50 intro to AI course project.

## Explanation
The goal of this project is to create an artificial intelligence that could play tic-tac-toe against a human.

### Board
The program reads the board as a 2-dimensional list full of Nones in the beginning, once the game goes on, the Nones change into "X" or "O".

### Intelligence
The way the program thinks is by maximizing the a state of a board that the program predicts with the current state of the board. Whenever the human player plays, the program takes all of the possibilities, once the program reaches a winner or full board, then the cost of the board will determine the desicion.

