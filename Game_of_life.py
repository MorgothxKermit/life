import numpy as np
import time
import functions as life
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rc('figure', max_open_warning = 0)


file_name = life.game_window()

with open(file_name, 'r') as file:
    read_from_file = file.read()
    #print(read_from_file)

board = []

read_from_file = read_from_file.split()
for i in range(0, len(read_from_file)-1):
    temp_list = ['X'  if j == 'X' else '.' for j in read_from_file[i]]
    board.append(temp_list)
    
board = np.array(board)

game_board = board.copy() # I encountered a certain problem with the function, as if board was global, a quick fix was done

"""for i in range(0, board.shape[0]):
    print('\n')
    for j in range(0, board.shape[1]):
        print(board[i][j], end='')
"""
#print('\n', game_board)
while True:
    game_board = life.check_neighbours(game_board) # main functionality, changes the board into next turn
    print('\n'*10)
    for i in range(0, board.shape[0]): # prints for now just to see if it works
        print('\n')
        for j in range(0, board.shape[1]): # board.shape to know the dimensions of the array
            print(game_board[i][j], end='')
    time.sleep(0.5)

"""while True:
    game_board = life.check_neighbours(game_board)
    fig, ax = plt.subplots()
    img = ax.imshow(game_board)
    ani = animation.FuncAnimation(fig, game_board, frames=10, interval=50, save_count=50)
    plt.show"""