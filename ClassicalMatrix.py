#Calculate a matrix row by column approach O(n3)
def classic(a, b):

    x = len(a[0])
    y =  len(a)
    sumMatrix = [[] for x in range(len(a))]
    #multiply rowa * colb (row * col multplication)
    for row in range(y):
        for col in range(x):
            sum = 0
            currentRow = a[row]
            for colLevel in range(y):
                sum += currentRow[colLevel] * b[colLevel][col]
            sumMatrix[row].append(sum)

    return sumMatrix
    
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

#records the runtime of the classic algorithm.
#returns the time it takes to finish the algorithm
import time
def record_Runtime(a, b):
    start_time = time.monotonic()
    classic(a,b)
    end_time = time.monotonic()
    final_time = end_time - start_time
    return final_time

#creates a text file that records runtimes from a nxn size from l size to r size
def create_graph(file, l, r):
    return None


a = [[2,0,-1,6],
     [3,7,8,0],
     [-5,1,6,-2],
     [8,0,1,7]]

b = [[0,1,6,3],
     [-2,8,7,1],
     [2,0,-1,0],
     [9,1,6,-2]]

c = [[1,2], [1,2]]
d = [[3,4], [5,6]]


print(record_Runtime(a,b))
print(record_Runtime(c,d))
    