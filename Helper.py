import csv
import os.path
import time

#directory of all the data
dir = 'data'

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

#records the runtime of the classic algorithm
#name = name of file, matrix_func = the matrix function
#a and b are the matrix getting multiplied
#isPrinted when true prints the output to the terminal
def record_Runtime(name, matrix_func, a, b, isPrinted):

    #record the time
    start_time = time.perf_counter()
    answer = matrix_func(a,b)
    end_time = time.perf_counter()
    final_time = (end_time - start_time)*1000

    #log the time
    appendTime([name, len(a), f"{final_time:.5f} ms"])

    #print output to terminal
    if isPrinted:
        print(f"{name}: ")
        for row in answer:
            print(row)
        print("\n")

#appends a row with [n, time] to a file 
#name is the name of the file
def appendTime(row): 
    #make the dir if it DNE
    if (not os.path.exists(dir)):
         os.mkdir(dir)

    #append
    with open(os.path.join('data', 'data.csv'), 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(row)

#prints matrix a and b and their size
def printAB(a, b):
    print(f"A * B | n = {len(a)}")
    for i in range(len(a)):
        print(f"{a[i]}\t{b[i]}")
    print("\n")

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
