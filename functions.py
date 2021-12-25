import numpy as np


def check_neighbours(board):
    dimensions = board.shape
    #print(dimensions)
    alive_cell = 'X'
    dead_cell = '.'
    rows, columns = dimensions[0], dimensions[1]
    temp_array = board.copy()
    for i in range(0, rows):
        for j in range(0, columns):
            cell = board[i][j]
            nmb_of_neigh = 0
            try:
                if board[i+1][j-1] == 'X': # checking all the surrounding cells
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i+1][j] == 'X':
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i+1][j+1] == 'X':
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i][j-1] == 'X':
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i][j+1] == 'X':
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i-1][j-1] == 'X':
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i-1][j] == 'X':
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i-1][j+1] == 'X':
                    nmb_of_neigh += 1
            except IndexError:
                pass
            
            
            if cell == alive_cell:
                if nmb_of_neigh <= 1 or nmb_of_neigh >= 4:
                    temp_array[i][j] = dead_cell
                elif nmb_of_neigh >= 2 and nmb_of_neigh <= 3:
                    temp_array[i][j] = alive_cell
            elif cell == dead_cell:
                if nmb_of_neigh == 3:
                    temp_array[i][j] = alive_cell
            
    board = temp_array.copy()
    return board
#IndexError 
#print(tab)

