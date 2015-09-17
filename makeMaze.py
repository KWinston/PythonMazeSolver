from graphics import *
from Maze import *
import random

# MakeMaze generates a maze using the Maze object created as part of Lab 1 and
# then displays it
# Author: B. Brookwell

PROBABILITY = 0.60
# Generates and displays a left hand searchable maze
#
# Syntax: makeMaze (rows, columns)
# Parameter
#      rows -- number of rows (Should be a multiple of 4 less one)
#      columns -- number of columns (Should be a multiple of 4 less one)

def makeMaze(rows, columns):
    # Create the display window
    win = GraphWin ("Maze Test", 10 * (columns + 1), 10 * (rows + 1))
    
    # Set up the full maze
    board = Maze (rows, columns)
    
    # Calculate the board center and put it in as the starting point
    r0 = rows // 2
    c0 = columns // 2
    board.set (r0, c0, START)
    queue = []
    queue.append(Point(r0, c0))
    
    while len(queue) > 0:  # As long as there are things to process in the queue
        element = queue.pop(0)  # Get the next location
        r = element.getX()
        c = element.getY()
        
        r1 = r + 2   # Move down two and see if we can cut a corridor
        if board.onMap (r1, c) and board.get(r1, c) == ROCK and random.random() < PROBABILITY:
            board.set(r+1, c, OPEN)
            board.set(r1, c, OPEN)
            queue.append(Point(r1, c))
        r1 = r - 2   # Move up two and see if we can cut a corridor
        if board.onMap (r1, c) and board.get(r1, c) == ROCK and random.random() < PROBABILITY:
            board.set(r-1, c, OPEN)
            board.set(r1, c, OPEN)
            queue.append(Point(r1, c))
        c1 = c + 2   # Move right two and see if we can cut a corridor
        if board.onMap (r, c1) and board.get(r, c1) == ROCK and random.random() < PROBABILITY:
            board.set(r, c+1, OPEN)
            board.set(r, c1, OPEN)
            queue.append(Point(r, c1))        
        c1 = c - 2   # Move left two and see if we can cut a corridor
        if board.onMap (r, c1) and board.get(r, c1) == ROCK and random.random() < PROBABILITY:
            board.set(r, c-1, OPEN)
            board.set(r, c1, OPEN)
            queue.append(Point(r, c1))
            
    # Starting at one of the four sides, place the exit
    side = random.randint(0,3)
    if side == 0:   # Top edge
        steps = columns // 2
        cStart = 1 + 2 * random.randint(0, (steps // 2))
        rStart = 0
        board.set (0, cStart, EXIT)
        dRow = 1
        dCol = 0
    elif side == 1:  # Bottom edge
        steps = columns // 2
        cStart = 1 + 2 * random.randint(0, (steps // 2))
        size = board.getSize()
        rStart, c1 = size
        rStart-=1
        board.set (rStart, cStart, EXIT)
        dRow = -1
        dCol = 0 
    elif side == 2:  # Left edge
        steps = rows // 2
        rStart = 1 + 2 * random.randint(0, (steps // 2))
        cStart = 0
        board.set (rStart, 0, EXIT)
        dRow = 0
        dCol = 1
    else:            # Right Edge
        steps = rows // 2
        rStart = 1 + 2 * random.randint(0, (steps // 2))
        size = board.getSize()
        r1, cStart = size
        cStart-=1
        board.set (rStart, cStart, EXIT)
        dRow = 0
        dCol = -1 
        
    # Cut a corridor inward from the exit until you contact the maze
    rStart += dRow
    cStart += dCol
    while board.get(rStart, cStart) == ROCK:
        board.set (rStart, cStart, OPEN)
        rStart += dRow
        cStart += dCol
        
    # Display the maze and wait for the person to click
    board.display (board, 10, win)
    
    win.getMouse()
    win.close()
    