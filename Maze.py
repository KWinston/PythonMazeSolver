# CMPT 200 Lab 1 Maze question - part 2,3,4
# 
# Author: Winston Kouch
# Date: September 15, 2014
#
# Description: Stores a list of lists that maps out a 2D grid.
#              Can use makeMaze to generate a maze.
#
# Syntax: board = Maze (r,c) - forms a board of size (r x c)
#         board = makeMaze(23, 23) - makes maze using Maze class
#
# Parameters: r - number of rows to make
#             c - number of columns to make
#

# include the makeMaze file
from makeMaze import *

# Set the four cell properties as integer values
# these values are used as globals so all functions can access these values
global win, START, OPEN, ROCK, EXIT
START = 0
OPEN = 1
ROCK = 2
EXIT = 3

# Description: the class Maze holds a grid of cells of size r x c.
# Syntax: the class Maze is initialized using: Maze (r,c).
class Maze:
    
    # Description: Upon class creation, generates ROCKS (value = 2)
    #              in each cell of r x c in board.
    # Parameters: r, c - row and column
    def __init__(self, r, c):
        self.board = [[2 for x in range(c)] for x in range(r)]
    
    # Description: This function retrieves the cell integer of a given cell.
    #              When checking, it is r or c - 1 because the first cells are
    #              stored in 0's. ie. (0,0) = row 1, col 1.
    # Parameters: r, c - row and column
    def get(self, r, c):
        
        # Each if statement checks the board for each cell type (integer 0 to 3)
        # it returns the integer for whichever it finds.
        if (self.board[r-1][c-1] == 0):
            return START
        
        if (self.board[r-1][c-1] == 1):
            return OPEN        
        
        if (self.board[r-1][c-1] == 2):
            return ROCK
        
        if (self.board[r-1][c-1] == 3):
            return EXIT
        
    # Description: This function sets the cell contents of a given cell.
    #              When checking, it is r or c - 1 because the first cells are
    #              stored in 0's.
    # Parameters: r, c, value - row, column and value is the cell content
    def set(self, r, c, value):
        
        # Each if statement determines the value that is being passed. It then
        # sets the cell content to the value being passed (an integer) at
        # position (r,c) as if the board started from row 1, col 1.
        if (value == START):
            self.board[r-1][c-1] = value
                
        if (value == OPEN):
            self.board[r-1][c-1] = value
                
        if (value == ROCK):
            self.board[r-1][c-1] = value
                
        if (value == EXIT):
            self.board[r-1][c-1] = value
            
    # Description: Determines if the cell to be checked is on the map
    #              ie. part of the created board.
    # Parameters: r, c - row and column
    def onMap(self, r, c):
        # boardSize uses the method getSize and stores it as a tuple
        boardSize = self.getSize()
        
        # If either r or c is not part of the list of lists, it will return
        # false. If it is, it will return True.
        # r and c use <= when checking boardSize because when checking
        # get and set, ie. r = 3, and c = 3 will be checked as board[2][2]
        if (r > 0 and c > 0 and r <= boardSize[0] and c <= boardSize[1]):
            return True
        return False

    # Description: Gets the size of the board. self.board is the # of rows
    #              and self.board[0] tells us the # of columns.
    def getSize(self):
        return (len(self.board), len(self.board[0]))
        
    # Description: Displays the contents of the maze using graphics.py.
    #              White cell is OPEN, Black cell is ROCK, Blue is EXIT
    #              Yellow is START.
    # Parameters: board - the varaible with the list of lists for the board data
    #             size - the # of pixels for each tile to be displayed
    #             win - the graphical window for graphics.py to draw on
    def display(self, board, size, win):
        # calls getSize to get the number of rows and columns of board
        boardSize = self.getSize()
        
        # for each position in board[r][c], draw the tile to screen according to
        # cell content 0-3
        for i in range(boardSize[0]):
                for j in range(boardSize[1]):
                    # cell: contains the rectangle data for graphics to draw
                    cell = Rectangle(Point(size*j,size*i), Point(10+size*j, 10+size*i))
                    if (self.board[i][j] == 0):
                        # set the rectangle color to draw
                        cell.setFill("yellow")
                        # draw the cell contents to graphics window
                        cell.draw(win)  
                    if (self.board[i][j] == 1):
                        cell.setFill("white")
                        cell.draw(win)                                               
                    if (self.board[i][j] == 2):
                        cell.setFill("black")
                        cell.draw(win)  
                    if (self.board[i][j] == 3):
                        cell.setFill("blue")
                        cell.draw(win)