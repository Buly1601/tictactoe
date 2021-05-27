"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board. --CHECHED--
    """
    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    
    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board. --CHECKED--
    """
    if terminal(board):
        return None

    pos_actions = set()

    for x,row in enumerate(board):
        for y,cell in enumerate(row):
            if cell == EMPTY:
                pos_actions.add((x,y))
    
    return pos_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board. --CHECKED--
    """
    res_board = copy.deepcopy(board)

    x = action[0]
    y = action[1]

    res_board[x][y] = player(board)
    
    return res_board


def winner(board):
    """
    Returns the winner of the game, if there is one. --CHECKED--
    """
    # check rows
    row_winner = check_row(board)
    if row_winner:
        return row_winner
    
    # check columns 
    transpose = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

    column_winner = check_row(transpose)
    if column_winner:
        return column_winner

    # check diagnoal possible winner
    middle = board[1][1]
    if middle == EMPTY: return 

    if board[0][0] == middle and board[2][2] == middle:
        return middle
    elif board[0][2] == middle and board[2][0] == middle:
        return middle

    return None

def check_row(board):
    """
    Returns the winner in row for a board. --CHECKED-- 
    """
    for row in board:
        row_set = set(row)
        if len(row_set) == 1:
            if row[0] == X:
                return X 
            elif row[0] == O:
                return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise. --CHECKED-- 
    """
    winer = winner(board)
    if winer:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY: return False

    return True    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise. --CHECKED--
    """
    winer = winner(board)
     
    if winer == X: 
        return 1
    elif winer == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None

    turn = player(board)

    if turn == X:
        cost,coords = optimal_max(board)
        return coords
    else:
        cost,coords = optimal_min(board)
        return coords


def optimal_max(board):
    #v = #v = max(v, min_value(result(board, action)))
    if terminal(board):
        return utility(board),None
    
    aux_v = -math.inf
    return_coords = tuple()

    for action in actions(board):
        next_board = result(board, action)
        min_prediction,c = optimal_min(next_board)

        if min_prediction > aux_v:
            aux_v = min_prediction
            return_coords = action
        
        if aux_v == 1:
            break

    return aux_v,return_coords

def optimal_min (board):
    #v = # v = max(v, min_value(result(board, action)))
    if terminal(board):
        return utility(board), None
    
    aux_v = math.inf
    return_coords = tuple()

    for action in actions(board):
        next_board = result(board, action)
        max_prediction,c = optimal_max(next_board)

        if max_prediction < aux_v:
            aux_v = max_prediction
            return_coords = action

        if aux_v == -1:
            break

    return aux_v,return_coords