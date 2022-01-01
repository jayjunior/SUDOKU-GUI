
import sudokuGui

# TODO:
# implement generate_random_sudoku
# implement solve_sudoku


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


def is_final(sudoku):
    pass


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


sudoku = [
    [2, 5, 6, 4, 8, 9, 1, 7, 3],
    [3, 7, 4, 6, 1, 5, 9, 8, 2],
    [9, 8, 1, 7, 2, 3, 4, 5, 6],
    [5, 9, 3, 2, 7, 4, 8, 6, 1],
    [7, 1, 2, 8, 0, 6, 5, 4, 9],
    [4, 6, 8, 5, 9, 1, 3, 2, 7],
    [6, 3, 5, 1, 4, 7, 2, 9, 8],
    [1, 2, 7, 9, 5, 8, 6, 3, 4],
    [8, 4, 9, 3, 6, 2, 7, 1, 5]
]


