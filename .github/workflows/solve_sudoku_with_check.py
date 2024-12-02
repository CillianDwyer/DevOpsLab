def solve_sudoku_with_check(board):
    if not is_valid_board(board):
        return None  # Invalid board
    solution = solve_sudoku(board)
    if solution:
        return solution
    return None  # No solution exists

def is_valid_board(board):
    if len(board) != 9 or not all(len(row) == 9 for row in board):
        return False  # Not a 9x9 grid
    for row in board:
        for cell in row:
            if not (0 <= cell <= 9):
                return False  # Invalid cell value
    return True
