
"""
    solve the given sudoku
"""


def solve_sudoku(sudoku):
    empty_cells = get_next_empty_cell(sudoku)
    if(empty_cells == None):
        return []
    for possibility in range(1, 10):
        apply(possibility, sudoku, empty_cells[0], empty_cells[1])
        if is_valid(possibility, sudoku, empty_cells[0], empty_cells[1]):
            next = solve_sudoku(sudoku)
            if next != None:
                next.insert(0,[empty_cells[0],empty_cells[1],possibility])
                revert(sudoku, empty_cells[0], empty_cells[1])
                return next
        revert(sudoku, empty_cells[0], empty_cells[1])

    return None


def get_next_empty_cell(sudoku):
    empty_cell = []
    for row in range(0, 9):
        for col in range(0, 9):
            if sudoku[row][col] == 0:
                empty_cell = [row, col]
                return empty_cell
    return None


def apply(possibility, sudoku, row, col):
    sudoku[row][col] = possibility


def revert(sudoku, row, col):
    sudoku[row][col] = 0


def is_valid(possibility, sudoku, row, col):
    # check on row
    for cols in range(0, 9):
        if sudoku[row][cols] == possibility and cols != col:
            return False

    # check on col
    for rows in range(0, 9):
        if sudoku[rows][col] == possibility and rows != row:
            return False

    starting_row = (row//3)*3
    starting_col = (col//3)*3

    for rows in range(starting_row, starting_row+3):
        for cols in range(starting_col, starting_col+3):
            if sudoku[rows][cols] == possibility and rows != row and col != col:
                return False
    return True




