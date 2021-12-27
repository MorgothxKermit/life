import numpy as np
import functions as life
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# remove the posibility of having a warning, when the plot could be too "big"
plt.rc('figure', max_open_warning=0)
file_name = life.game_window()

with open(file_name, 'r') as file:
    read_from_file = file.read()
    # print(read_from_file)

board = []

read_from_file = read_from_file.split()
for i in range(0, len(read_from_file)-1):
    temp_list = [1 if j == 'X' else 0 for j in read_from_file[i]]
    board.append(temp_list)

board = np.array(board)

# I encountered a certain problem with the function, as if board was global, a quick fix was done
game_board = board.copy()

"""for i in range(0, board.shape[0]):
    print('\n')
    for j in range(0, board.shape[1]):
        print(board[i][j], end='')

print('\n', game_board)
while True:
    # main functionality, changes the board into next turn
    game_board = life.check_neighbours(game_board)
    print('\n'*10)
    # prints for now just to see if it works
    for i in range(0, board.shape[0]):
        print('\n')
        # board.shape to know the dimensions of the array
        for j in range(0, board.shape[1]):
            if game_board[i][j] == 1:
                print('X', end='')
            else:
                print('.', end='')
    time.sleep(0.5)
"""
# the above comment is completely useless, it's just for me if I ever want to go back 
# to printing my result.


def animate(n):
    global game_board
    game_board = life.check_neighbours(game_board)
    img.set_array(game_board)
    return img

game_board = life.check_neighbours(game_board)
fig, ax = plt.subplots()
img = ax.imshow(game_board)
anim = animation.FuncAnimation(
    fig, 
    animate,
    frames=30,
    interval=500,
    blit=False
)
plt.show()
