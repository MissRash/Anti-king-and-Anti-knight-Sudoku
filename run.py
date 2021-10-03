import time
from gui import *
from solver import *
from solvability_solutionvalidity import *


sudoku = []
# Ask user for file containing sudoku puzzle
file_name = str(input("\nPlease provide puzzle file name: "))
file_name = ''.join((file_name,'.txt'))
# Load the text file containing sudoku puzzle in read format
r = open(file_name, 'r')
while True:
    lines = r.readlines()
    # List to hold the unsolved sudoku puzzle
    for line in lines:
        # Splitting each row of the text file
        z = line.split()
        # Appending each row to the list, sudoku
        sudoku.append(z)
    # Counter, j, followed by for loop, to verify that the loaded array has 81 elements
    j = 0
    for i in range(9):
        # len(sudoku[i]) represents number of columns
        # We do not need to check for rows specifically, since the counter, j, verifies that there are nine columns with 9 elements in each of them
        if len(sudoku[i]) == 9:
            j += 1
    # If all 9 columns have length of 9 elements, exit the while loop
    if j == 9:
        break
    # If total number of elements is not 81, the program executes the following lines, and reiterates the while loop
    else:
        print("Please check loaded puzzle for missing values.")
        file_name = str(input("Please provide puzzle file name: "))
        file_name = ''.join((file_name, '.txt'))
        r = open(file_name, 'r')
        sudoku = []

for i in range(0, 9):
    for j in range(0, 9):
        # Converting the variable type from string to integer
        sudoku[i][j] = int(sudoku[i][j])

print("The loaded sudoku puzzle is: %s" % r.name.rstrip('.txt'))
print()


# Function to display the unsolved sudoku grid
def show_grid(sudoku):
    horizontal_divider = "-" * 31
    print(" ", horizontal_divider)
    for i in range(9):
        for j in range(9):
            if j % 3 == 0:
                print('  | ', end="")

            print("", sudoku[i][j], end="")

            if j == 8:
                print("  | ", end="")

        print()
        if (i + 1) % 3 == 0:
            print(" ", horizontal_divider)

# Calling the above defined function
show_grid(sudoku)

# Ask user if the loaded puzzle has anti-king or anti-knight moves constraints
while True:
    antiking = str(input("\nIs the anti-king move constraint applicable for this puzzle? Enter T or F: "))
    if antiking == 'T' or antiking == 'F':
        break
    else:
        print("Please provide your option by pressing T or F. No other character is accepted.")

while True:
    antiknight = str(input("\nIs the anti-knight move constraint applicable for this puzzle? Enter T or F: "))
    if antiknight == 'T' or antiknight == 'F':
        break
    else:
        print("Please provide your option by pressing T or F. No other character is accepted.")

# Execution of the solution part of the script begins at this point
start = time.time()

# solvability(sudoku, grid_type, antiking, antiknight) function verifies if the loaded puzzle is solvable or not.
# Based on verification from solvability(sudoku, 'unsolved', antiking, antiknight) function, the program execution either proceeds further or terminates.
while solvability(sudoku, 'unsolved', antiking, antiknight) is True:
    print("Initial check complete.")
    print("This sudoku puzzle is solvable.")
    print()
    print("Solving the puzzle.....")
    # Calling the function to initiate the sudoku problem-solving algorithm
    solution_grid = solve_puzzle(sudoku, antiking, antiknight)

    # Calling solvability(sudoku, 'solved', antiking, antiknight) again to verify the correctness of the puzzle solution
    solution_check = solvability(solution_grid, 'solved', antiking, antiknight)
    # If solution_check returns False, the solution grid is invalid.
    if solution_check is False:
        print("\nSolution found for %s puzzle does not meet the applicable constraints." % r.name.rstrip('.txt'))
        break
    # If solution_check returns True, the solution grid is valid. Call function to measure time at this point.
    stop = time.time()
    print()
    print("\nPlease refer the Pygame display window for solution of the puzzle %s." % r.name.rstrip('.txt'))
    print()
    print("Execution time: ", stop-start, "seconds")
    # Calling main(solution_grid, r.name) function from gui.py to display the solved puzzle
    main(solution_grid, r.name)
    break

# solvability(sudoku, antiking, antiknight) function verifies if the loaded puzzle is solvable or not.
# If it is not solvable, the execution jumps to the below lines of the script.
else:
    print("This sudoku puzzle is unsolvable")
