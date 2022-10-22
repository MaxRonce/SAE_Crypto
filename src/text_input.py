from typing import Tuple, Dict, Any
import numpy as np
import unidecode
import string


def text_format(text_input : str) -> str:
    """
    It takes a string as input, converts it to uppercase, and then removes any accents

    :param text_input: The text you want to format
    :return: A string
    """
    text_input = text_input.upper()
    try:
        text_input = unidecode.unidecode(text_input)
    except NameError:
        pass
    return str(text_input)

def strip_puntuation(text: str):
    """
    It takes a string, formats it, turns it into a list, makes a copy of the list, and then creates a dictionary of the
    punctuation and spaces in the original list. Then it removes the punctuation and spaces from the copy and returns the
    copy as a string

    :param text: the text to be stripped of punctuation
    :type text: str
    :return: A tuple with the first element being the string without punctuation and the second element being a dictionary
    with the punctuation and spaces as keys and the punctuation and spaces as values.
    """
    text = text_format(text)
    text = list(text)
    text_copy = text
    dic_text = {}

    for i in range(len(text)):
        if text[i] in string.punctuation+" ":
            dic_text[i] = text[i]
    for i in dic_text.values():
        text_copy.remove(i)

    return "".join(text_copy), dic_text

def insert_punctuation(text: str, dic: dict) -> str:
    """
    It takes a string and a dictionary as input, and returns a string with punctuation inserted at the positions specified
    in the dictionary

    :param text: the text to be punctuated
    :type text: str
    :param dic: a dictionary of punctuation marks and their positions in the text
    :type dic: dict
    :return: A string with punctuation inserted at the correct locations. Uppercase
    """
    text = list(text)
    for i in dic.keys():
        text.insert(i, dic[i])
    return "".join(text)

#convert a text into a numpy array of number, A = 1st letter of the alphabet, B = 2nd letter of the alphabet, etc.

def text_to_number(text: str) -> np.ndarray:
    """
    It takes CLEAN text as input and returns a numpy array of numbers

    :param text: The text to be converted
    :return: A numpy array of numbers
    """
    text = text_format(text)
    text = list(text)
    for i in range(len(text)):
        text[i] = ord(text[i]) - 64
    text = np.array(text)
    return text
#convert a numpy array of number into a text
def number_to_text(text) -> str:
    """
    It takes a numpy array of numbers as input and returns a string
    :param text: The numpy array of numbers to be converted
    :return: A string
    """
    text = list(text)
    for i in range(len(text)):
        text[i] = chr(text[i] + 64)
    text = "".join(text)
    return text

# flatten an array of arrays into a single array
def flatten_array(array: np.ndarray) -> np.ndarray:
    """
    It takes a numpy array of arrays as input and returns a single numpy array

    :param array: The numpy array of arrays to be flattened
    :return: A single numpy array
    """
    array = array.flatten()
    return array

#split a text into an array of n-sized arrays, if the text is not a multiple of n, the last array will be padded with 0

def split_text(text: str, n: int) -> np.ndarray:
    """
    It takes a string and an integer as input and returns a numpy array of arrays

    :param text: The text to be split
    :param n: The length of the arrays
    :return: A numpy array of arrays
    """
    text = text_to_number(text)
    if text.size % n != 0:
        text = np.append(text, np.zeros(n - text.size % n))
    text = np.array_split(text, len(text) / n)
    text = np.array(list(map(lambda x: x.astype(int), text)))
    text = np.array(text)
    return text


