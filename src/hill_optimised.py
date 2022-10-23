from text_input import *
from is_french import *
import file
import numpy as np
from numba import jit
import time


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#otpimisation of determinant function
@jit(nopython=True)
def determinant(matrix)->int:
    """
    It takes a 2x2 matrix as input and returns the determinant of the matrix
    :param matrix: The matrix to be used
    :return: A float
    """
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    det = a * d - b * c
    return det


@jit(nopython=True)
def inverse(matrix):
    """
    It takes a 2x2 matrix as input and returns the inverse of the matrix
    :param matrix: The matrix to be used
    :return: A 2x2 matrix
    """
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    return [[d, -b], [-c, a]]


@jit(nopython=True)
def modinv(a, m):
    """
    It takes two integers as input and returns the modular inverse of a mod m
    :param a: The integer to be used
    :param m: The modulus
    :return: A float
    """
    for x in range(1, m):
        if (a*x) % m == 1:
            return x
@jit(nopython=True)
def pgcd(a, b):
    """
    "If b is 0, return a, otherwise return the pgcd of b and a modulo b."

    The function is recursive, meaning that it calls itself

    :param a: the first number
    :param b: the base
    :return: The greatest common divisor of a and b.
    """
    if b == 0:
        return a
    else:
        return pgcd(b, a%b)

@jit(nopython=True)
def split_text(text):
    """
    It takes a string of text and returns a list of strings, each of which is two characters long

    :param text: the text to be split
    :return: A list of the text split into pairs of letters.
    """

    if len(text)%2 == 1:
        text += "Z"
    text_list = []
    for i in range(0, len(text), 2):
        text_list.append(text[i:i+2])
    return text_list

def convert_to_number(list_text: str) -> list:
    """
    It takes a list of strings, and returns a list of lists of numbers

    :param list_text: a list of strings, each string is a pair of letters
    :type list_text: str
    :return: A list of lists, where each list is a pair of numbers.
    """
    res = []
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in list_text:
        a = ALPHABET.index(i[0])
        b = ALPHABET.index(i[1])
        res.append([a, b])
    return res


def block_by_matrix_multiplication(block:list, matrix:list):
    res = []
    res.append(ALPHABET[(matrix[0][0] * block[0] + matrix[0][1] * block[1]) % 26])
    res.append(ALPHABET[(matrix[1][0] * block[0] + matrix[1][1] * block[1]) % 26])
    return res

@jit(nopython=True)
def create_matrix_list():
    liste = np.array([[[i, j], [k, l]] for i in range(0, 26) for j in range(0, 26) for k in range(0, 26) for l in range(0, 26)])
    return liste

def hill_uncipher(list_text: list, matrix: list) -> str:

    deter = determinant(matrix)
    det_inv = modinv(deter, 26)
    matrice_inv = inverse(matrix)
    matrix = [[det_inv * matrice_inv[0][0] % 26, det_inv * matrice_inv[0][1] % 26],[det_inv * matrice_inv[1][0] % 26, det_inv * matrice_inv[1][1] % 26]]

    plaintext = []
    for i in list_text:
        a = ALPHABET.index(i[0])
        b = ALPHABET.index(i[1])
        plaintext += block_by_matrix_multiplication([a, b], matrix)

    #same with lambda
    plaintext = "".join(plaintext)
    return plaintext

def main(text:str):



    text_no_punct, punct = strip_puntuation(text)
    percent_dict_minimum = calculate_euclidean_difference(text_no_punct)

    list_text = split_text(text_no_punct)
    num_list = convert_to_number(list_text)
    start = time.time()
    plaintext=""
    d_mini = calculate_euclidean_difference(text_no_punct)
    start = time.time()
    all_matrix = create_matrix_list()

    print(f"Time to create matrix list: {time.time() - start}")
    print(f"Number of matrix: {len(all_matrix)}")

    #remove all matrix with det != 1
    matrix_list = [i for i in all_matrix if pgcd(determinant(i), 26) == 1]


    start = time.time()
    txt_list = [hill_uncipher(list_text, i) for i in matrix_list]
    d_list = [calculate_euclidean_difference(i) for i in txt_list]
    #get the minimum and the index of the minimum
    d_mini = min(d_list)
    index = d_list.index(d_mini)
    plaintext = txt_list[index]
    print(f"Time to decrypt the text: {time.time() - start}")
    return insert_punctuation(plaintext, punct)

if __name__ == "__main__":
    parent_path = file.get_parent_path()
    text = file.open_file(parent_path + "/data/Texte3.txt")
    print(main(text))

