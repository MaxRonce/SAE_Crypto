import os
import json
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
            return json.load(file)

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


if __name__ == "__main__":
    parent_path = get_parent_path()
    file_path = os.path.join(parent_path, "out", "test.txt")
    file_content = "Hello World!"
    write_file(file_path, file_content)

    print("hello")

    for i in range(1, 6):
        text = open_file(parent_path + "/data/Texte" + str(i) + ".txt")
        clean_text(text, i)

    liste_of_text = ["Hello", "World", "How", "Are", "You"]
    all_text_to_csv(liste_of_text, "test")

    print(load_csv("test"))



