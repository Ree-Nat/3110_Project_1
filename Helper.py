import csv;
import os.path;
import ClassicalMatrix;

#data = [5, '0100']
dir = 'data';

#hardcoded a matrix
a = [[2,0,-1,6],
     [3,7,8,0],
     [-5,1,6,-2],
     [8,0,1,7]]

#hardcoded b matrix
b = [[0,1,6,3],
     [-2,8,7,1],
     [2,0,-1,0],
     [9,1,6,-2]]

#other hardcoded matrixes
c = [[1,2], [1,2]]
d = [[3,4], [5,6]]

#appends a row with [n, time] to a file 
def appendTime(name, row): 
    #make the dir if it DNE
    if (not os.path.exists(dir)):
         os.mkdir(dir)

    #append
    with open(os.path.join('data', name+'.csv'), 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow(row)

#records the runtime of the classic algorithm.
#returns the time it takes to finish the algorithm
import time
def record_Runtime(a, b):
    start_time = time.monotonic()
    ClassicalMatrix.classic(a,b)
    end_time = time.monotonic()
    final_time = end_time - start_time
    return final_time

#Return a random matrix of size n x n
import random
def createMatrix(n):
    matrix = [[] for x in range(n)]
    for row in range(n):
        for col in range(n):
            random.seed()
            x = random.randint(0,10)
            currentRow = matrix[row]
            currentRow.append(x)
    return matrix

