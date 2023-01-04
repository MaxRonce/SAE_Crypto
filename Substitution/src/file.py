import os
import json
import numpy as np
import csv
from text_input import *
#abstract path of the parent folder

def get_parent_path() -> str:
    """
    It returns the path of the parent folder
    :return: A string
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#Open the given file and read it, stock it in a variable

def open_file(file_path: str, return_type = "Text") -> str:
    """
    It takes a string as input and returns the content of the file at the given path
    :param file_path: The path of the file to be opened
    :return: A string
    """
    if return_type == "Text":
        with open(file_path, "r") as file:
            return file.read()
    if return_type == "Json":
        with open(file_path, "r") as file:
            dict = json.load(file)
            #convert all dict keys to int
            return {int(k):v for k,v in dict.items()}


#function that take a string as input and write it in a file, if then file doesn't exist, it creates it into SAE_Crypto/out folder

def write_file(file_path: str, file_content, type = "Text") -> None:
    """
    It takes a string as input and write it in a file, if then file doesn't exist, it creates it into SAE_Crypto/out folder
    :param file_path: The path of the file to be written
    :param file_content: The content of the file to be written
    :return: None
    """
    if type == "Text":
        with open(file_path, "w") as file:
            file.write(file_content)
    if type == "Json":
        with open(file_path, "w") as file:
            json.dump(file_content, file)

#function that take a string as input, strip punctuation, write the clean texte in a file, if then file doesn't exist, it creates it into SAE_Crypto/data folder
#and return the clean text in a file in SAE_Crypto/Data folder, use text_input

def clean_text(text: str, txt_number : int):
    """
    It takes a string as input, strip punctuation, write the clean texte in a file, if then file doesn't exist, it creates it into SAE_Crypto/data folder
    and return the clean text in a file in SAE_Crypto/Data folder, use text_input
    :param text: The text to be cleaned
    :return: A string
    """
    text, punct = strip_puntuation(text)
    parent_path = get_parent_path()

    #write it into data/Clean_text folder
    write_file(parent_path + "/data/Clean_text/Clean_text_" + str(txt_number) + ".txt", text)

    #write the punctuation dictionary into data/Punctuation folder
    write_file(parent_path + "/data/Punctuation/Punctuation_" + str(txt_number) + ".json", punct, "Json")
    return None


def text_to_number(text: str, A_value : int) -> list:
    """
    It takes a string as input and returns a numpy array of integers
    :param text: The text to be converted
    :return: A numpy array of integers
    """
    if A_value == 0:
        return np.array([ord(char)-65 for char in text])
    else:
        return np.array([ord(char)-(64) for char in text])

def number_to_text(number: list, A_value : int) -> str:
    """
    It takes a list of integers as input and returns a string
    :param number: The list of integers to be converted
    :return: A string
    """
    if A_value == 0:
        return "".join([chr(i+65) for i in number])
    if A_value == 1:
        return "".join([chr(i+64) for i in number])

def to_csv(file_path: str, data: str) -> None:
    """
    It takes a string and a list as input and write the list in a csv file
    :param file_path: The path of the file to be written
    :param data: The data to be written
    :return: None
    """
    #use numpy to write the data in a csv file
    np.savetxt(file_path, data, delimiter=",", fmt="%s")

def from_csv(file_path: str, type = "int"):
    """
    It takes a string as input and returns a numpy array
    :param file_path: The path of the file to be read
    :return: A numpy array
    """
    if type == "int":
        return np.loadtxt(file_path, delimiter=",", dtype=int)
    if type == "str":
        return np.loadtxt(file_path, delimiter=",", dtype=str)





if __name__ == "__main__":
    parent_path = get_parent_path()

    # for i in range(1, 6):
    #     text = open_file(parent_path + "/data/Texte" + str(i) + ".txt")
    #     clean_text(text, i)
    #
    # for i in range(1, 6):
    #     text = open_file(parent_path + "/data/Clean_text/Clean_text_" + str(i) + ".txt")
    #     to_csv(parent_path + "/data/Text_Number/Number_" + str(i) + ".csv", text_to_number(text, 1))
    #     print(text)
    print(from_csv(parent_path + "/data/Text_Number/Number_4.csv"))




