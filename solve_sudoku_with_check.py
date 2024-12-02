from solve_sudoku import solve_sudoku  # Import solve_sudoku

def solve_sudoku(board):
    if not is_valid_board(board):
        return None  # Invalid board
    solution = solve_sudoku(board)  # Call the solve_sudoku function
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
