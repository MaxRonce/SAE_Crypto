from typing import Tuple, Dict, Any

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

def strip_puntuation(text: str, mode:str = 'default') -> tuple[str, dict[int, Any]]:
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
    removed_punctuation = string.punctuation
    if mode == 'default':
        removed_punctuation += " "
    for i in range(len(text)):
        if text[i] in removed_punctuation:
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


