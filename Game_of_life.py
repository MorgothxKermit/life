import numpy as np
import time
from functions import check_neighbours

with open('glider.txt', 'r') as file:
    A = file.read()


C = []

A = A.split()
for i in range(0, len(A)-1):
    B = [j for j in A[i]]
    C.append(B)
    
C = np.array(C)

new_C = C.copy() # I encountered a certain problem with the function, as if C was global, a quick fix done


for i in range(0, C.shape[0]):
    print('\n')
    for j in range(0, C.shape[1]):
        print(C[i][j], end='')

#print('\n', new_C)
while True:
    new_C = check_neighbours(new_C)
    print('\n'*10)
    for i in range(0, C.shape[0]):
        print('\n')
        for j in range(0, C.shape[1]):
            print(new_C[i][j], end='')
    time.sleep(0.5)

