# CMPT 200 Lab 2 Maze Solver
# 
# Author: Winston Kouch
#
#
# Date: September 30, 2014

#include graphics.py for graphical drawing of maze and solution
from graphics import *

START = 0 # The start
OPEN = 1 # Walkable pathway
ROCK = 2 # Wall
EXIT = 3 # The exit

MARK = 4 # Mark down paths on the way to exit

#Label paths not on solution path leading to dead ends as BAD
BAD = 5

# Description: the class Maze holds a grid of cells of size r x c.
# Syntax: the class Maze is initialized using: Maze (r,c).
class Maze:
    
    # Description: Upon class creation, generates ROCKS (value = 2)
    #              in each cell of r x c in board.
    # Parameters: r, c - row and column
    def __init__(self, r, c):
        self.board = [[2 for x in range(c)] for x in range(r)]
    
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
        if (r >= 0 and c >= 0 and r < boardSize[0] and c < boardSize[1]):
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
        # Wait for mouse click
        win.getMouse()
        
    # Similar to display function above, except it looks for integer 4 and 5 in
    # the list of lists to find red which is marked paths leading to a dead end
    # Integer 4 is MARKED which is the green path leading from start to exit.
    def displaysol(self, board, size, win):
        boardSize = self.getSize()
        for i in range(boardSize[0]):
            for j in range(boardSize[1]):        
                cell = Rectangle(Point(size*j,size*i), Point(10+size*j, 10+size*i))
                # marked bad path red color tiles
                #if (self.board[i][j] == 5):
                    #cell.setFill("red")
                    #cell.draw(win)
                # solution path marked as green tiles
                if (self.board[i][j] == 4):
                    cell.setFill("green")
                    cell.draw(win)                                         
        # Wait for Mouse Click
        win.getMouse()
        # Close Graphics Window
        win.close()
            
    # Function to prepare to solve the loaded maze
    def solveMaze(self): 
        # Get Start point in my maze representation and store as start
        boardSize = self.getSize()
        for i in range(boardSize[0]):
            for j in range(boardSize[1]):
                if(self.board[i][j] == START):
                    #row, col
                    start = (i, j)
                    
        # Get End point in my maze representation and store as end
        boardSize = self.getSize()
        for i in range(boardSize[0]):
            for j in range(boardSize[1]):
                if(self.board[i][j] == EXIT):
                    #row, col
                    end = (i, j)
                    
        # store the start value as y and x
        y, x = start
        
        # run the algorithm to find path to goal
        self.checkPath(y, x)
        
        # store the end value as y and x
        y, x = end
        
        # if a path was found from start to goal, tell the user that
        # if the exit tile does not exist, means path found, so do nothing.
        if (self.board[y][x] == MARK):
            # do nothing
            pass
        # Else, tell user there was no path found.
        else:
            # if algorithm runs and no path to exit, print no path found
            print ('No path from start to finish were found!')
        
    # Recursive Backtracking Pathfinding
    def checkPath(self, y, x):
        # Change the START tile to an OPEN tile so it will start properly
        if(self.board[y][x] == START):
            self.board[y][x] = OPEN
            
        # Then, check if coordinates on the board
            self.onMap(y,x) # onMap will return true if on map
            
        # If tile checked is EXIT, solution has been found and sol path marked!
        if(self.board[y][x] == EXIT):
            self.board[y][x] = MARK
            # Tell user that there is a path to goal
            print ('A path has been found from start to finish!')
            print ('Solution stored in mazeSol.txt')
            
            # Output solution to mazeSol.txt by calling outputSolution function
            self.outputSolution()
            return True
        
        # If tile is not open/walkable, cannot proceed this way
        if(self.board[y][x] != OPEN):
            return False
        
        # If it passed all if's so far, mark x,y as part of solution path
        # Because I am marking my path, it prevents my algorithm from
        # continuous cycling
        self.board[y][x] = MARK
            
        # Check Directions
    
        # Check North Tile(y-1), gets True if criteria is met
        if(self.checkPath(y-1,x) == True):
            return True
        # Check East Tile(x+1), gets True if criteria is met
        if(self.checkPath(y,x+1) == True):
            return True
        # Check South Tile(y+1), gets True if criteria is met
        if(self.checkPath(y+1,x) == True):
            return True
        # Check West Tile(x-1), getsTrue if criteria is met
        if(self.checkPath(y,x-1) == True):
            return True
        # If the path isn't leading to the EXIT,
        # mark the path that leads to dead end path
        # this is not needed but is nice to know which paths lead to dead ends
        self.board[y][x] = BAD
        
    # sets Start Position and End Position that is given in the maze data file
    def setPositions(self, startPoint, endPoint, mapSize):
        # Unpack tuples
        startRow = int(startPoint[0])
        startCol = int(startPoint[1])
        endRow = int(endPoint[0])
        endCol = int(endPoint[1])
        # Since we drop from top left corner and proceed east and south
        # for +x and +y coordinates, we must subtract the given start and end
        # from the data which starts from 0,0 at the bottom left
        # Set Start Point
        self.board[mapSize[0] - (startRow + 1)][startCol] = START
        # Set End Point
        self.board[-endRow*2][(endCol*2)-1] = EXIT
            
    # map the maze using retrieved maze data from the maze file
    def mappingMaze(self, theMaze, mapSize):
        global stripped_list, solution_list
        # rowCounter keeps track of what row it is on
        rowCounter = 0
        
        # store the rols, cols as integers instead
        rows = int(mapSize[0])
        cols = int(mapSize[1])
        
        # Strip the \n characters from each line
        stripped_list = [item.strip() for item in theMaze[3:]]
        
        # For each row, check each letter that is represented as column
        # if it is a rock, it is a wall type which returns walkable tile as false
        # if it is a space, it is a walkable tile on the maze board
        for line in stripped_list:
            for i in range(cols):
                if(stripped_list[rowCounter][i] == "|" or "+" or "-"):
                    self.board[rowCounter][i] = ROCK
                if(stripped_list[rowCounter][i] == " "):
                    self.board[rowCounter][i] = OPEN
            # Increase the row count in operation after each row is checked
            rowCounter += 1
            
        # creates a new list that stores the solution for later
        solution_list = [] + stripped_list    
            
    def outputSolution(self):
        
        # For each row, check each letter that is represented as column
        # if it is a rock, it is a wall type which returns walkable tile as false
        # if it is a space, it is a walkable tile on the maze board
        
        # start from row one
        rowCounter = 1
        
        # retrieve map size
        boardSize = self.getSize()
        
        # change the the string contents in solution list to contain * for
        # the path to solution instead of white space
        for line in solution_list:
            # for each tile in my maze, (grabbing every 2 tiles)
            # if the tile is in my list of lists and is MARKED as part of
            # solution path, change the string to include the * instead of
            # white space.
            for i in range(boardSize[1]):
                if(self.onMap(rowCounter,i)):
                    if(self.board[rowCounter][i] == MARK):
                        if (rowCounter and i % 2):
                            solution_list[rowCounter] = solution_list[rowCounter][0:i] + "*" + solution_list[rowCounter][i+1:]
                            
            # Increase the row count in operation after each row is checked, since I doubled the map size for my representation
            # I am grabbing from every 2 rows, 2 cols
            rowCounter += 2
            
        # Initialize the string for the combined solution
        combinedSol = ""
        
        # Join each line
        for line in solution_list:
            combinedSol = combinedSol + line + "\n"    
        
        # Output file to mazeSol.txt
        outputFile = open('mazeSol.txt', 'w')
        
        # write to file the string, combinedWord
        outputFile.write(combinedSol)
        
        # close output file
        outputFile.close()