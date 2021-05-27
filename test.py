from tictactoe import optimal_min

X = "X"
O = "O"
EMPTY = None
board = [
        [X,O,O],
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,O,X]
        ]

print(optimal_min(board))