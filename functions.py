import numpy as np
from multiprocessing import Process
from tkinter import *
from PIL import ImageTk
from PIL import Image


def file_glider(file, root):
    file.set('glider.txt')
    root.destroy()


def file_pulsar(file, root):
    file.set('pulsar.txt')
    root.destroy()


def file_gun(file, root):
    file.set('gosper-glider-gun.txt')
    root.destroy()


def check_neighbours(board):
    dimensions = board.shape
    # print(dimensions)
    alive_cell = 1
    dead_cell = 0
    rows, columns = dimensions[0], dimensions[1]
    temp_array = board.copy()
    for i in range(0, rows):
        for j in range(0, columns):
            cell = board[i][j]
            nmb_of_neigh = 0
            try:
                if board[i+1][j-1] == alive_cell:  # checking all the surrounding cells
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i+1][j] == alive_cell:
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i+1][j+1] == alive_cell:
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i][j-1] == alive_cell:
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i][j+1] == alive_cell:
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i-1][j-1] == alive_cell:
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i-1][j] == alive_cell:
                    nmb_of_neigh += 1
            except IndexError:
                pass
            try:
                if board[i-1][j+1] == alive_cell:
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


def game_window():
    root = Tk()

    img_glider = ImageTk.PhotoImage(Image.open('glider.png'))
    img_glider_gun = ImageTk.PhotoImage(Image.open('glider_gun.png'))
    img_pulsar = ImageTk.PhotoImage(Image.open('pulsar.png'))
    glider_image = Label(root, image=img_glider)
    glider_gun_image = Label(root, image=img_glider_gun)
    pulsar_image = Label(root, image=img_pulsar)

    file = StringVar()
    header = Label(root, text='Which pattern do you want to see evolve?').grid(
        row=0, column=1, columnspan=2)

    # Making buttons
    button_glider = Button(root, text='Glider',
                           command=lambda: file_glider(file, root))
    button_glider_gun = Button(
        root, text='Gosper_glider_gun', command=lambda: file_gun(file, root))
    button_pulsar = Button(root, text='Pulsar',
                           command=lambda: file_pulsar(file, root))

    # Griding buttons
    button_glider.grid(row=1, column=0)
    button_glider_gun.grid(row=2, column=0)
    button_pulsar.grid(row=3, column=0)

    glider_image.grid(row=1, column=1)
    glider_gun_image.grid(row=2, column=1)
    pulsar_image.grid(row=3, column=1)

    # make some images to show the patterns and put them under the buttons! Just above this comment

    root.mainloop()

    return file.get()
