from Helper import Matrix, add_matrix, sub_matrix, split_matrix, combine_quadrants

# Strassen Algorithm
def strassen(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)

    #Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    #Split matrices into quadrants
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)
    
    #Define new values using recursion
    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen(add_matrix(A21, A22), B11)
    M3 = strassen(A11, sub_matrix(B12, B22))
    M4 = strassen(A22, sub_matrix(B21, B11))
    M5 = strassen(add_matrix(A11, A12), B22)
    M6 = strassen(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen(sub_matrix(A12, A22), add_matrix(B21, B22))

    #Combine results into quadrants
    C11 = add_matrix(add_matrix(M1, M4), sub_matrix(M7, M5))
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(add_matrix(M1, M3), sub_matrix(M6, M2))

    #Combine quadrants and return resulting product matrix C
    return combine_quadrants(C11, C12, C21, C22)