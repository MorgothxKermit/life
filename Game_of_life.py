import numpy as np
import time
import functions as life

file_name = life.game_window()

with open(file_name, 'r') as file:
    A = file.read()
    print(A)

C = []

A = A.split()
for i in range(0, len(A)-1):
    B = [j for j in A[i]]
    C.append(B)
    
C = np.array(C)

new_C = C.copy() # I encountered a certain problem with the function, as if C was global, a quick fix was done

"""for i in range(0, C.shape[0]):
    print('\n')
    for j in range(0, C.shape[1]):
        print(C[i][j], end='')
"""
#print('\n', new_C)
while True:
    new_C = life.check_neighbours(new_C) # main functionality, changes the board into next turn
    print('\n'*10)
    for i in range(0, C.shape[0]): # prints for now just to see if it works
        print('\n')
        for j in range(0, C.shape[1]):
            print(new_C[i][j], end='')
    time.sleep(0.5)


