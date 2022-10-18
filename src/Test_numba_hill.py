import numpy as np
from numba import jit
from numba.typed import List
import time
import file
import multiprocessing


def split_text(liste, N:int):
    """
    It takes a string as input and split it into a list of blocks of 2, if the len is not a multiple of N, if adds
    a 0 at the end until it's a multiple of N
    :param text: The text to be split
    :return: A list of blocks of 2
    """
    text_as_list = []
    liste = liste.tolist()
    #add a 0 at the end of the text if the len is not a multiple of N
    while len(liste) % N != 0:
        liste.append(0)
    #split the text into blocks of N using lambda map
    text_as_list = np.array(list(map(lambda x: liste[x:x+N], range(0, len(liste), N))))
    return text_as_list



#generatel all the possible matrices 2x2 in Z/26Z

@jit(nopython=True)
def create_matrix_list(start=1, end=26):
    liste = np.array([[[i, j], [k, l]] for i in range(1, 26) for j in range(1, 26) for k in range(1, 26) for l in range(1, 26)])
    return liste

#multiply 2 matrix function, vectorize it with numba

def multiply_matrix(matrix1, matrix2):
    #matrix1 [1,1] matrix2[[1,2],[3,4]] is2x2 matrices
    return np.dot(matrix1, matrix2)

def multiply_list_by_matrix(liste, matrix):
    #liste = [[1,2],[3,4],[5,6]]....
    #matrix = [[1,2],[3,4]]
    #result = [[7,10],[15,22],[23,34]]
    return np.array(list(map(lambda x: multiply_matrix(x, matrix), liste)))

def multiply_list_by_matrix_list(liste, matrix_list):
    result = list(map(lambda x: multiply_list_by_matrix(liste, x), matrix_list))
    #modulate the result by 26 on each number
    return np.array(list(map(lambda x: np.mod(x, 26), result)))


def pgcd(a, b):
    if a == 0:
        return b
    return pgcd(b % a, a)

def unsplit_list(liste):
    return [item for sublist in liste for item in sublist]

def main():
    parent_path = file.get_parent_path()
    #create a list of all the possible matrices 2x2 in Z/26Z
    start = time.time()
    matrix_list = create_matrix_list()
    print(f"Number of matrix generated : {len(matrix_list)}")
    print("Time to create the matrix list: ", time.time() - start)
    print("---------------------------------------")


    #strip the matrix list to keep only the invertible matrices
    start = time.time()
    matrix_list = np.array(list(filter(lambda x: pgcd(np.linalg.det(x), 26) == 1, matrix_list)))
    print(f"Number of invertible matrix generated : {len(matrix_list)}")
    print("Time to create the invertible matrix list: ", time.time() - start)

    start = time.time()

    print("---------------------------------------")

    for i in range(1,6):
        print(f"Test {i}")
        text_as_list = file.from_csv(parent_path + f"/data/Text_Number/Number_{i}.csv")
        print(f"Text {i} : {text_as_list}")
        print("Time to load the text as a np array: ",  time.time() - start)
        splitted = split_text(text_as_list, 2)
        print("time to split the text: ", time.time() - start)
        result = []
        for j in range(len(matrix_list)):
            result.append(unsplit_list(multiply_list_by_matrix(splitted, matrix_list[j])))

        print("time to multiply the text by all matrix: ", time.time() - start)
        file.to_csv(parent_path + f"/out/Hill/Number_{i}.csv",result)
        print("time to save the result: ", time.time() - start)
        print("TEXT NUMBER ", i, " DONE")
        print("---------------------------------------")

    print("time to multiply the text by all matrix: ", time.time() - start)

    #multiprocess the multiplication of the text by all the possible matrices

    start = time.time()



    print("time to multiply the text by all the possible matrices with multiprocessing: ", time.time() - start)
if __name__ == "__main__":
    main()