import random
from typing import List

Matrix = List[List[int]]

# -------------------
# Matrix Generator
# -------------------
def matrixGenerator(n: int) -> Matrix:
    return [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]

# -------------------
# Helper functions
# -------------------
def add_matrix(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def split_matrix(A: Matrix):
    n = len(A)
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    return A11, A12, A21, A22

def combine_quadrants(C11: Matrix, C12: Matrix, C21: Matrix, C22: Matrix) -> Matrix:
    top = [c11 + c12 for c11, c12 in zip(C11, C12)]
    bottom = [c21 + c22 for c21, c22 in zip(C21, C22)]
    return top + bottom

# -------------------
# Naive Divide & Conquer
# -------------------
def dac_multiply(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)
    
    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # Split into quadrants
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)
    
    # 8 recursive multiplications
    M1 = dac_multiply(A11, B11)
    M2 = dac_multiply(A12, B21)
    M3 = dac_multiply(A11, B12)
    M4 = dac_multiply(A12, B22)
    M5 = dac_multiply(A21, B11)
    M6 = dac_multiply(A22, B21)
    M7 = dac_multiply(A21, B12)
    M8 = dac_multiply(A22, B22)
    
    # Combine results
    C11 = add_matrix(M1, M2)
    C12 = add_matrix(M3, M4)
    C21 = add_matrix(M5, M6)
    C22 = add_matrix(M7, M8)
    
    return combine_quadrants(C11, C12, C21, C22)

# -------------------
# Demo
# -------------------
if __name__ == "__main__":
    n = 4  # must be a power of 2
    A = matrixGenerator(n)
    B = matrixGenerator(n)
    
    print("Matrix A:")
    for row in A: print(row)
    
    print("\nMatrix B:")
    for row in B: print(row)
    
    C = dac_multiply(A, B)
    print("\nA * B (Naive D&C):")
    for row in C: print(row)
