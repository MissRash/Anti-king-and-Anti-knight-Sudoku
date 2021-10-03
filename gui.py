import pygame, sys
from pygame.locals import *



# Set the display window size (windowwidth, windowheight, windowsize_multiplier)
# For sudoku puzzles, the window is of square shape. Therefore, height and width have the same value.
windowwidth = 9
windowheight = 9
# windowsize_multiplier defines the factor by which the height and width of the window should be enlarged.
windowsize_multiplier = 60
windowwidth_gui = windowwidth * windowsize_multiplier
windowheight_gui = windowheight * windowsize_multiplier
# squaresize defines the size of each 3x3 sub-grid. Since grid is a square, we can use either height or width to calculate this value.
squaresize = int(windowheight_gui / 3)
# cellsize defines the size of each cell in the 9x9 grid.
cellsize = int(squaresize / 3)
# Pixel representation of the colors used in this GUI window
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
NAVYBLUE = (0, 0, 128)


# Main game loop. Accepts the sudoku solution grid and the file name of the loaded sudoku puzzle as arguments
def main(sol, title):
    global DISPLAYSURF, solution, fonttype, fontsize
    # pygame.init() activates the Pygame library. This function is called before calling any other Pygame function
    pygame.init()
    # Below function creates a Surface (image or display window) of size given in the tuple (windowwidth_gui, windowheight_gui)
    # The mentioned tuple accepts width and height values, (width, height)
    DISPLAYSURF = pygame.display.set_mode((windowwidth_gui, windowheight_gui))
    # Below function sets the caption text that will appear at the top of the display window
    pygame.display.set_caption('Solution for sudoku puzzle: %s' % title.rstrip('.txt'))
    # Setting the display font type and size
    fonttype = pygame.font.SysFont('cambria', 40)
    # Setting the window background with white color
    DISPLAYSURF.fill(WHITE)
    # Calls the function that will draw the minor and major lines of the grid
    drawGrid()
    # Accessing each element of sol
    for i in range(9):
        for j in range(9):
    # for each element of sol, the below function is called which will blit(draw) the elements onto the DISPLAYSURF Surface
    # (i * cellsize) represents width; (j * cellsize) represents height
            fillcells(sol[i][j], i * cellsize, j * cellsize)

    while True:
    # Since there is no user interaction in this window setup, we have only one event which can happen i.e.,
    # when the user QUITS the program by clicking on the CLOSE button located at the top-right corner of the window
        for event in pygame.event.get():
            if event.type == QUIT:
                # pygame.quit() deactivates the Pygame library.
                pygame.quit()
                # sys.exit() terminates the program
                sys.exit()
    # Until the QUIT event is initiated, the below function displays the solution window
        pygame.display.update()


# Function to draw major and minor lines of the grid
def drawGrid():
    # Draw minor lines - boundary of each cell
    # In the below for loop, each line is at a distance of cellsize from each other
    for x in range(0, windowwidth_gui, cellsize):
    # Parameters of the below function:
    # DISPLAYSURF- Surface on which the line is drawn (Remember that we have already filled the window with white background)
    # GRAY - Line color
    # (x, 0) represents starting position of the line; (x, windowheight_gui) represents the end position of the line
        pygame.draw.line(DISPLAYSURF, GRAY, (x, 0), (x, windowheight_gui)) # draw vertical lines
    for y in range(0, windowheight_gui, cellsize):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, GRAY, (0, y), (windowwidth_gui, y))

    # Draw major Lines - squares (3x3 sub-grid)
    for x in range(0, windowwidth_gui+1, squaresize):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x, 0), (x, windowheight_gui), 5)
    for y in range(0, windowheight_gui+1, squaresize):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0, y), (windowwidth_gui, y), 5)

    return None


# Function to blit(draw) sudoku solution numbers onto the display window
# cellvalue takes each element of sol, sol[x][y] as argument
def fillcells(cellvalue, x, y):
# '%d' % cellvalue : the text to be rendered
# True: This is the antialias argument. If set to True, the displayed text will have smoother egdes.
# Antialiased images are rendered to create 24-bit RGB images.
# NAVYBLUE: Color of the rendered text
    cellSurf = fonttype.render('%d' % cellvalue, True, NAVYBLUE)
# Below function will return a rectangle that starts at (0,0) with width and height the same size as the image, cellSurf.
    cellRect = cellSurf.get_rect()
# Since our intention is to draw the text, cellSurf, onto the display window, DISPLAYSURF, we have to align the position of the text with respect to the display grid
# By using cellRect.topleft, we can position cellSurf at a width of (y+18) pixels and height of (x+5) pixels
# In each row of an array, x-coordinate remains constant. But, while blitting image in Pygame, width varies with each element of a row.
# Therefore, (y+18) i.e., y-coordinate of array is used for width and x-coordinate for height.
    # y+18 represents width and x+5 represents height
    cellRect.topleft = (y+18, x+5)
# Below function blits(draws) the image rendered by cellSurf in the position provided by cellRect.
    DISPLAYSURF.blit(cellSurf, cellRect)
