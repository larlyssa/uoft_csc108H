import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
    if value >= min_value and value <= max_value:
        return True
    else:
        return False

def game_board_full(game_board):
"""
Returns true if the board game is full. Otherwise, returns false.
"""
    for space in game_board:
        if space == EMPTY:
            return False     
    return True

def get_board_size(game_board):
"""
Checks that the game board is a perfect square, then returns the length of the columns/rows.
"""
    board_str_len = len(game_board)
    if board_str_len ** 0.5 == round(board_str_len ** 0.5):
        return int(board_str_len ** 0.5)
    else:
        return "Error: board not a perfect square."
    
def make_empty_board(length):
"""
Creates an empty board of the desired length, filled only with empty '-' characters.
"""
    empty_board = ""
    for instance in range(length):
        empty_board += EMPTY
    return empty_board

def get_position(row, column, board_size):
"""
Returns the position in a string for a (row, column) coordinate, given the board size.
"""
    str_index = (row - 1) * board_size + column - 1
    return str_index


def make_move(symbol, row, column, game_board):
"""
Makes a move, adding the symbol to the appropriate (row, column) on the game board. Precondition that the move is made in an empty square.
"""
    move_pos = get_position(row, column, get_board_size(game_board))
    new_board = game_board[:int(move_pos)] + symbol + game_board[int(move_pos + 1):]
    return new_board

def extract_line (game_board, direction, direction_location):
"""
Returns the characters that makes up the specified row.
"""
    board_size = get_board_size(game_board)
    line = ""
    if direction == 'down':
        for symbol in range(1, int(board_size) + 1):
            symbol_pos = get_position(symbol, direction_location, board_size)
            line += game_board[symbol_pos]
    elif direction == 'across':
        for symbol in range(1, int(board_size) + 1):
            symbol_pos = get_position(direction_location, symbol, board_size)
            line += game_board[symbol_pos]
    
    elif direction == 'down_diagonal':
        for symbol in range(1, int(board_size) + 1):
            symbol_pos = get_position(symbol, symbol, board_size)
            line += game_board[symbol_pos]
    elif direction == 'up_diagonal':
        for symbol in range(1, int(board_size) + 1):
            symbol_pos = get_position(board_size - symbol + 1, symbol, board_size)
            line += game_board[symbol_pos]
    return line
