from text_input import *
from is_french import *
import file
import numpy as np
from numba import jit
import time
import sys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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

def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a%b)


def split_text(text):

    if len(text)%2 == 1:
        text += "Z"
    text_list = []
    for i in range(0, len(text), 2):
        text_list.append(text[i:i+2])
    return text_list


def convert_to_number(list_text: str) -> list:
    res = []
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
def hill_uncipher(list_text: list, matrix: list) -> str:

    valid_det = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    # if determinant(matrix) % 26 not in valid_det:
    #     return None
    if pgcd(determinant(matrix), 26) != 1:
        return None
    else:

        deter = determinant(matrix)
        det_inv = modinv(deter, 26)
        matrice_inv = inverse(matrix)
        matrix = [[det_inv * matrice_inv[0][0] % 26, det_inv * matrice_inv[0][1] % 26],[det_inv * matrice_inv[1][0] % 26, det_inv * matrice_inv[1][1] % 26]]

        plaintext = []
        for i in list_text:
            a = ALPHABET.index(i[0])
            b = ALPHABET.index(i[1])
            plaintext += block_by_matrix_multiplication([a, b], matrix)
        plaintext = "".join(plaintext)
    return plaintext



def main(text:str):
    # parent_path = file.get_parent_path()
    # text = file.open_file(parent_path + "/data/Texte3.txt")

    text_no_punct, punct = strip_puntuation(text)
    percent_dict_minimum = calculate_euclidean_difference(text_no_punct)

    list_text = split_text(text_no_punct)
    num_list = convert_to_number(list_text)

    matrix = [[2,3],[1,5]]

    start = time.time()
    plaintext=""
    d_mini = calculate_euclidean_difference(text_no_punct)

    message_decrypte = None
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(26):
                    matrice = [[i, j], [k, l]]

                    if hill_uncipher(list_text, matrice) is not None:
                        d_curr = calculate_euclidean_difference(hill_uncipher(list_text, matrice))
                        if d_curr < d_mini:
                            plaintext = hill_uncipher(list_text, matrice)
                            d_mini = d_curr

    return insert_punctuation(plaintext, punct)

if __name__ == "__main__":
    main()
