# CMPT 200 Lab 2 Maze Solver
# 
# Author: Winston Kouch
#
#
# Date: September 30, 2014
#
# Description: Asks user for file with maze data. Stores maze in list of lists
#              Runs backtracking recursive function to find path to goal.
#              Saves the output to file, mazeSol.txt. If no file given, it will
#              default to using maze.txt. It then checks if the file exists.
#              if it does, it will proceed with solving the maze. If it
#              doesn't exist it will print an error message and stop.
#
# Syntax: getMaze() - Asks user for file with maze data
#
#

# import my Maze class
from Maze import *
                        
# To load the maze, this function is used to ask user for maze filename
# After it is entered, it will load the maze or 
def getMaze():
    # Ask user to input maze file name
    filename = input("Please enter the maze file name: ")
    
    # if user enters nothing during input, it will default to maze.txt and try to open it.
    if (filename == ""):
        filename = "maze.txt"
    
    # try to open the file
    try:
        inputFile = open(filename, 'r')
        
    except FileNotFoundError:
        # If it doesnt exist, prints error message and stops
        print ("Error, The file", filename, "does not exist.")
        return None
    
    # Read the map data into theMaze
    theMaze = inputFile.readlines()
    
    # close the file
    inputFile.close()
    
    # Set up the map size, start point, end point
           
    # Grab from first line of map data
    mapSize = theMaze[0].split()
           
    # Split the 2 numbers into rows, cols
    mapSize[0] = 2*int(mapSize[0])+1
    mapSize[1] = 2*int(mapSize[1])+1
    
    # Grab start and end point from line 2 and 3 of file       
    startPoint = theMaze[1].split()
    endPoint = theMaze[2].split()    
    
    # Set up a display window for graphics.py
    win = GraphWin ("Maze Path", 10 * (mapSize[1]), 10 * (mapSize[0]))      
    
    # Generate the board in a list of lists
    generatedMaze = Maze(mapSize[0],mapSize[1])
    
    # Map the maze into my list of lists
    generatedMaze.mappingMaze(theMaze, mapSize)
    
    # Place the start and end points onto the board
    generatedMaze.setPositions(startPoint, endPoint, mapSize)
            
    # Display translated Maze
    generatedMaze.display(generatedMaze, 10, win)   
    
    # Solve the maze
    generatedMaze.solveMaze()
    
    # Display the solution in graphics
    generatedMaze.displaysol(generatedMaze, 10, win)

# Run getMaze
getMaze()