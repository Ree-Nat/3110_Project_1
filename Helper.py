import csv
import os.path
import time
import random
from typing import List, Tuple

Matrix = List[List[int]]

#directory of all the data
dir = 'data'
fieldnames = ['n', 'time(ms)']

# Matrix Generators
def createMatrix(n: int, low: int = -10, high: int = 10) -> Matrix:
    """Return a random n x n matrix with entries between low and high."""
    return [[random.randint(low, high) for _ in range(n)] for _ in range(n)]

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


# Matrix Helpers
def add_matrix(A: Matrix, B: Matrix) -> Matrix:
    """Elementwise add two matrices."""
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matrix(A: Matrix, B: Matrix) -> Matrix:
    """Elementwise subtract two matrices (A - B)."""
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def split_matrix(A: Matrix) -> Tuple[Matrix, Matrix, Matrix, Matrix]:
    """Split a square matrix into four quadrants."""
    n = len(A)
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    return A11, A12, A21, A22

def combine_quadrants(C11: Matrix, C12: Matrix, C21: Matrix, C22: Matrix) -> Matrix:
    """Combine four quadrants into one square matrix."""
    top = [c11 + c12 for c11, c12 in zip(C11, C12)]
    bottom = [c21 + c22 for c21, c22 in zip(C21, C22)]
    return top + bottom

def printAB(a: Matrix, b: Matrix):
    """Print two matrices side by side."""
    print(f"A * B | n = {len(a)}")
    for i in range(len(a)):
        print(f"{a[i]}\t{b[i]}")
    print("\n")


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
    appendTime(name, {'n':len(a), 'time(ms)':final_time})

    #print output to terminal
    if isPrinted:
        print(f"{name}: ")
        for row in answer:
            print(row)
        print("\n")

#appends a row with {type: name, n:n, time(ms):time} to a file 
#name is the name of the file
def appendTime(name, row): 
    #make the dir if it DNE
    if (not os.path.exists(dir)):
         os.mkdir(dir)
    
    if (not os.path.exists(os.path.join('data', name+'.csv'))):
         with open(os.path.join('data', name+'.csv'), 'w') as file:
             writer = csv.DictWriter(file, fieldnames=fieldnames)
             writer.writeheader()

    #append
    with open(os.path.join('data', name+'.csv'), 'a', newline='') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
            writer.writerow(row)

#prints matrix a and b and their size
#def printAB(a, b):
#    print(f"A * B | n = {len(a)}")
#    for i in range(len(a)):
#        print(f"{a[i]}\t{b[i]}")
#    print("\n")

#Return a random matrix of size n x n
#import random
#def createMatrix(n):
#    matrix = [[] for x in range(n)]
#    for row in range(n):
#        for col in range(n):
#            random.seed()
#            x = random.randint(0,10)
#            currentRow = matrix[row]
#            currentRow.append(x)
#    return matrix
