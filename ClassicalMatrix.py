from Helper import Matrix

#Calculate a matrix row by column approach O(n3)
def classic(a: Matrix, b: Matrix) -> Matrix:
    x = len(a[0])
    y = len(a)
    sumMatrix = [[] for _ in range(len(a))]
    
    #multiply rowa * colb (row * col multplication)
    for row in range(y):
        for col in range(x):
            sum = 0
            currentRow = a[row]
            for colLevel in range(y):
                sum += currentRow[colLevel] * b[colLevel][col]
            sumMatrix[row].append(sum)

    return sumMatrix
    
