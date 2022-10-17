import numpy as np
from numba import jit
import time

#numba accelerated code

#generatel all the possible matrices 2x2 in Z/26Z

@jit(nopython=True)
def create_matrix_list(start=1, end=26):
    liste = np.array([[[i, j], [k, l]] for i in range(1, 26) for j in range(1, 26) for k in range(1, 26) for l in range(1, 26)])
    return liste

#multiply 2 matrix function, vectorize it with numba

@jit(nopython=True)
def multiply_matrix(matrix1, matrix2):
    #matrix1 and matrix2 are 2x2 matrices
    #the result is a 2x2 matrix
    result = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

@jit(nopython=True)
def multiply_list_matrix(liste, matrix):
    #liste is a list of list
    #matrix is a list of list
    #the result is a list of list
    #same but with a lambda map

    result = list(map(lambda x: multiply_matrix(matrix, np.transpose(x)), liste))
    result = list(map(lambda x: list(map(lambda y: y % 26, x)), result))
    return result

#create a vector of size N, divided in block of 2
@jit(nopython=True)
def big_vector(N):
    #generate a vector of N blocks of 2 with a for loop
    vector = np.array([[i, j] for i in range(N) for j in range(N)])
    return vector
#list(map(lambda x: multiply_matrix(vector, x), matrix_list)) as function

def main():
    #create a list of all the possible matrices 2x2 in Z/26Z with numba and meseaure the time
    start = time.time()
    matrix_list = create_matrix_list()
    print(len(matrix_list))
    end = time.time()
    print("Time to create the matrix list: ", end - start)
    print("Number of matrices: ", len(matrix_list))
    vector = np.array([[1, 2], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4], [3, 4]])


    #multiply the vector with all the matrices in the list and measure the time
    start = time.time()
    result = list(map(lambda x: multiply_matrix(vector, x), matrix_list))
    end = time.time()
    print("Time to multiply the vector with all the matrices: ", end - start)

    #generate a big vector

    start = time.time()
    vector = big_vector(1000)
    print(len(vector))
    end = time.time()
    print("Time to create the big vector: ", end - start)


    #multiply the vector with all the matrices in the list and measure the time
    start = time.time()
    result = np.array(map(lambda x: multiply_matrix(vector, x), matrix_list))
    end = time.time()
    print("Time to multiply the big vector with all the matrices: ", end - start)


if __name__ == "__main__":
    main()