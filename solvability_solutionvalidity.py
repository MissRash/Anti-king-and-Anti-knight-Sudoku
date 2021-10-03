# Function to verify solvability of loaded puzzle and correctness of solution grid
# First parameter is the array containing the sudoku puzzle
# Second parameter tells the function if the puzzle is solved or unsolved
# Third and fourth parameters indicate if anti-king or anti-knight move constraints are applicable or not.

def solvability(sudoku, grid_type, antiking, antiknight):

    for row in range(9):
        for col in range(9):

            # STEP 1: CHECK FOR 0'S IN THE GRID
            # Since the unsolved sudoku puzzle contains 0, we proceed with next iteration of the loop when a cell contains 0
            if grid_type == 'unsolved':
                if sudoku[row][col] == 0:
                    continue
            # The solution grid should not contain any 0's. If (row, col) has 0, the solution is invalid
            if grid_type == 'solved':
                if sudoku[row][col] == 0:
                    return False

            # STEP 2: CHECK THE NINE 3 X 3 SQUARES
            # Each of the nine 3 x 3 squares are indexed using below two assignments
            row_square = (row // 3) * 3
            col_square = (col // 3) * 3
            # For every (row, col), we check if same number is present more than once in its square
            for x in range(3):
                for y in range(3):
                    # Below condition makes sure that the cell (row, col) is not checked with itself
                    if row_square + x == row and col_square + y == col:
                        continue

                    if grid_type == 'unsolved':
                        # Since the unsolved sudoku puzzle contains 0, we proceed with next iteration of the for loop when a cell contains 0
                        if sudoku[row_square + x][col_square + y] == 0:
                            continue
                        if sudoku[row_square + x][col_square + y] == sudoku[row][col]:
                            return False

                    if grid_type == 'solved':
                        # The solution array should not contain any 0's. If an element of the square has the value, 0, the solution is invalid
                        if sudoku[row_square + x][col_square + y] == 0:
                            return False
                        # A square should not contain any number more than one. If it does, the grid is either unsolvable or invalid, depending on the value of grid_type
                        elif sudoku[row_square + x][col_square + y] == sudoku[row][col]:
                            return False

            # STEP 3: CHECK ROW
            for i in range(1, 9):
                # Since the unsolved sudoku puzzle contains 0, we proceed with next iteration of the for loop when a cell in the same row as (row, col) contains 0
                if grid_type == 'unsolved':
                    if sudoku[row][(col + i) % 9] == 0:
                        continue
                    elif sudoku[row][(col + i) % 9] == sudoku[row][col]:
                        return False
                # The solution grid should either not contain any 0's or not have repetitive numbers in the given row.
                if grid_type == 'solved':
                    if sudoku[row][(col + i) % 9] == 0 or sudoku[row][(col + i) % 9] == sudoku[row][col]:
                        return False

            # STEP 4: CHECK COLUMN
            for i in range(1, 9):
                # Since the unsolved sudoku puzzle contains 0, we proceed with next iteration of the for loop when a cell in the same column as (row, col) contains 0
                if grid_type == 'unsolved':
                    if sudoku[(row + i) % 9][col] == 0:
                        continue
                    elif sudoku[(row + i) % 9][col] == sudoku[row][col]:
                        return False
                # The solution grid should either not contain any 0's or not have repetitive numbers in the given column
                if grid_type == 'solved':
                    if sudoku[(row + i) % 9][col] == sudoku[row][col] or sudoku[(row + i) % 9][col] == 0:
                        return False

            # STEP 5: IF ANTI-KNIGHT MOVES CONSTRAINT IS APPLICABLE, CHECK ALL EIGHT POSSIBLE KNIGHT MOVES WITH RESPECT TO THE GIVEN CELL (ROW, COL)
            if antiknight == 'T':
                    # Check cells present in four knight moves applicable respectively to a row above and a row below the cell, (row, col)
                    for k in (row - 1, row + 1):
                        for l in (col - 2, col + 2):
                            # Making sure that values of k and l are in the index range of the 9 x 9 array
                            if 9 > k >= 0 and 9 > l >= 0:
                                # If k and l are in same square as (row, col), we proceed with next iteration of the for loop since in STEP 2 we have already checked the square containing cell, (row, col)
                                if ((k // 3) * 3) == row_square and ((l // 3) * 3) == col_square:
                                    continue
                                # Since the unsolved sudoku puzzle contains 0, we proceed with next iteration of the for loop when a cell in the knight move contains 0
                                if grid_type == 'unsolved':
                                    if sudoku[k][l] == 0:
                                        continue
                                    # A cell in the knight move position of the cell, (row, col), should not contain the same number as the cell, (row, col). If it does, the grid is unsolvable.
                                    elif sudoku[k][l] == sudoku[row][col]:
                                        return False
                                # The solution grid should not contain any 0's. If any cell in one of the knight moves of cell, (row, col), contains 0, the solution is invalid
                                # A cell in the knight move position of the cell, (row, col), should not contain the same number as the cell, (row, col). If it does, the solution is invalid.
                                if grid_type == 'solved':
                                    if sudoku[k][l] == 0 or sudoku[k][l] == sudoku[row][col]:
                                        return False

                    # Check the cells located in four knight moves applicable respectively to a column to the left and to a column to the right of the cell, (row, col)
                    for k in (row - 2, row + 2):
                        for l in (col - 1, col + 1):
                            # Making sure that values of k and l are in the index range of the array
                            if 9 > k >= 0 and 9 > l >= 0:
                                # If k and l are in same square as (row, col), we proceed with next iteration of the for loop since in STEP 2 we have already checked the square containing cell, (row, col)
                                if ((k // 3) * 3) == row_square and ((l // 3) * 3) == col_square:
                                    continue
                                # Since the unsolved sudoku puzzle contains 0, we proceed with next iteration of the for loop when a cell in the knight move contains 0
                                if grid_type == 'unsolved':
                                    if sudoku[k][l] == 0:
                                        continue
                                    # A cell in the knight move position of the cell, (row, col), should not contain the same number as the cell, (row, col). If it does, the grid is unsolvable
                                    elif sudoku[k][l] == sudoku[row][col]:
                                        return False
                                # The solution grid should not contain any 0's. If any cell in one of the knight moves of cell, (row, col), contains 0, the solution is invalid
                                # A cell in the knight move position of the cell, (row, col), should not contain the same number as the cell, (row, col). If it does, the solution is invalid
                                if grid_type == 'solved':
                                    if sudoku[k][l] == 0 or sudoku[k][l] == sudoku[row][col]:
                                        return False

            # STEP 6: IF ANTI-KING MOVES CONSTRAINT IS APPLICABLE, CHECK ALL FOUR POSSIBLE KING MOVES IN CELLS LOCATED DIAGONALLY TO THE GIVEN CELL, (ROW, COL)
            # We need not check neighboring cells at LEFT, RIGHT, TOP AND BOTTOM positions since they are already checked in STEPS 3 AND 4.
            if antiking == 'T':
                for k in (row - 1, row + 1):
                    for l in (col - 1, col + 1):
                        # Making sure that values of k and l are in the index range of the array
                        if 9 > k >= 0 and 9 > l >= 0:
                            # If k and l are in same square as (row, col), we proceed with next iteration of the for loop since in STEP 2 we have already checked the square containing cell, (row, col)
                            if ((k // 3) * 3) == row_square and ((l // 3) * 3) == col_square:
                                continue
                            # Since the unsolved sudoku puzzle contains 0, we proceed with next iteration of the for loop when a cell diagonally connected to (row, col) contains 0
                            if grid_type == 'unsolved':
                                if sudoku[k][l] == 0:
                                    continue
                                # A cell diagonally connected to the cell, (row, col), should not contain the same number as the cell, (row, col). If it does, the grid is unsolvable
                                elif sudoku[k][l] == sudoku[row][col]:
                                    return False
                            # The solution grid should not contain any 0's. If any cell diagonally connected to (row, col) contains 0, the solution is invalid
                            # A cell diagonally connected to the cell, (row, col), should not contain the same number as the cell, (row, col). If it does, the solution is invalid
                            if grid_type == 'solved':
                                if sudoku[k][l] == 0 or sudoku[k][l] == sudoku[row][col]:
                                    return False

    return True
