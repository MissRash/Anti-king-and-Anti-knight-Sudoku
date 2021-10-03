def constraints_check(sudoku, value, coordinates, antiking, antiknight):
    for row in range(9):
        # Checking the entire column, coordinates[1], for same number as value
        if sudoku[row][coordinates[1]] == value:
            return False

        for col in range(9):
            # Checking the entire row, coordinates[0], for same number as value
            if sudoku[coordinates[0]][col] == value:
                return False

    row_square = (coordinates[0] // 3) * 3
    col_square = (coordinates[1] // 3) * 3

    for i in range(3):
        for j in range(3):
            # Checking the entire 3 x 3 grid for same number as value
            if sudoku[row_square + i][col_square + j] == value:
                return False

            # Checking all eight anti-knight moves of the cell (coordinates[0], coordinates[1]) for same number as value
            if antiknight == 'T':
                # Checking four anti-knight moves of the cell in rows (coordinates[0]-1) and (coordinates[0]+1)
                for row in (coordinates[0] - 1, coordinates[0] + 1):
                    for col in (coordinates[1] - 2, coordinates[1] + 2):
                        # Row and column values should not exceed the array size
                        if 9 > row >= 0 and 9 > col >= 0:
                            # The cell to be checked should not be in the same 3 x 3 grid as the cell (coordinates[0], coordinates[1])
                            if (row // 3) * 3 == row_square and (col // 3) * 3 == col_square:
                                continue
                            if sudoku[row][col] == value:
                                return False

                # Checking remaining four anti-knight moves in columns (coordinates[1]-1) and (coordinates[1]+1)
                for row in (coordinates[0] - 2, coordinates[0] + 2):
                    for col in (coordinates[1] - 1, coordinates[1] + 1):
                        if 9 > row >= 0 and 9 > col >= 0:
                            if (row // 3) * 3 == row_square and (col // 3) * 3 == col_square:
                                continue
                            if sudoku[row][col] == value:
                                return False

            # Checking four diagonal anti-king moves of cell (coordinates[0], coordinates[1]) for same number as value
            # Not necessary to check vertical and horizontal anti-king moves as they are already checked in lines 4, 9
            if antiking == 'T':
                for row in (coordinates[0] - 1, coordinates[0] + 1):
                    for col in (coordinates[1] - 1, coordinates[1] + 1):
                        if 9 > row >= 0 and 9 > col >= 0:
                            if (row // 3) * 3 == row_square and (col // 3) * 3 == col_square:
                                continue
                            if sudoku[row][col] == value:
                                return False

    return True


# Function to find zeroes in the unsolved sudoku puzzle
def find_zero(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                # Returns position of 0 to fill_number(sudoku, antiking, antiknight)
                return row, col

    return None


# Function to assign values to positions with 0's through backtracking algorithm
def fill_number(sudoku, antiking, antiknight):
    position = find_zero(sudoku)
    # If all 0's in the puzzle are replaced with a number between 1-9, True is returned to solve_puzzle(sudoku, antiking, antiknight)
    if position is None:
        return True
    else:
        row, col = position

    # Using recursion and backtracking to solve the sudoku puzzle
    for x in range(1, 10):
        # Calling constraints_check(sudoku, x, (row, col), antiking, antiknight) to verify if x can be placed in the position (row, col)
        if constraints_check(sudoku, x, (row, col), antiking, antiknight):
            # Assign x to sudoku[row][col] if above function returns True
            sudoku[row][col] = x

            # The below function recursively calls itself until all the 0's in the puzzle have been replaced
            if fill_number(sudoku, antiking, antiknight):
                return True

        # Backtracking to previous valid state of 0 to try out the next digit for x
        sudoku[row][col] = 0

    return False


# This function initiates the sudoku problem-solving algorithm and eventually returns the solved sudoku grid to run.py
def solve_puzzle(sudoku, antiking, antiknight):
    fill_number(sudoku, antiking, antiknight)
    return sudoku

