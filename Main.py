from Helper import record_Runtime, a, b, createMatrix, printAB
import ClassicalMatrix
import NaiveMatrix
import StrassenMatrix

p = 9 #n = 2**p = problem size; change this value to change the problem size for data collection
printTimes = 0 #the number of times we want a printed output to the terminal in large scale data collection
#do not make printTimes too big, the size of the matrix will be 2**printTimes big

def main():

    #Test Code to run your programs; 
    #edit method if neccesary to call your method
    #testCode()
    #remember to delete or unstage the data dir and files before commiting to github

    #data collection code

    print("Starting...")
    
    for i in range(p+1):
        c = createMatrix(2**i)
        d = createMatrix(2**i)

        if (i<printTimes): #only prints up to printTimes into the console
            matrixMultiplication(c, d, True)
        else:
            matrixMultiplication(c, d, False)

        i =+ 1

    print("Finished!")
    

#run each program with matrixes a and b
#prints the outputs when isPrinted is set to true
def matrixMultiplication(a, b, isPrinted):
    #print the matrixes we are multiplying 
    if isPrinted:
        printAB(a, b)

    #name of file, function, function parameters
    record_Runtime("Naive", NaiveMatrix.dac_multiply, a, b, isPrinted)
    record_Runtime("Classic", ClassicalMatrix.classic, a, b, isPrinted)
    record_Runtime("Strassen", StrassenMatrix.strassen, a, b, isPrinted)
    
#test the code with 2 hard coded matrix and 2 randomly generated ones
def testCode():

    #use all 3 methods to multiply hardcoded matrix a and b
    matrixMultiplication(a, b, True)

    c = createMatrix(8)
    d = createMatrix(8)

    #use all 3 methods to multiply randomly generated matrix a and b of size 8 each
    matrixMultiplication(c, d, True)

if __name__ == "__main__":
    main()