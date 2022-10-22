
from text_input import strip_puntuation, insert_punctuation, text_format
from is_french import is_french

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_decrypt(text: str, key: int) -> str:
    """
    It takes a string (no punctuation and UPPER) as input and returns the string decrypted with the given key
    :param text: The text to be decrypted
    :param key: The key to be used for decryption
    :return: A string
    """
    text = list(text)
    decrypted_text = []
    for letter in text:
        decrypted_text.append(ALPHABET[(ALPHABET.index(letter) + key) % 26])
    return "".join(decrypted_text)

def caesar_decrypt_all(text: str) -> list:
    """
    It takes a string (no punctuation and UPPER) as input and returns the most likely to be french string and it's index in the list
    :param text: The text to be decrypted
    :return: A list of strings
    """
    stripText = strip_puntuation(text)[0]
    decrypted_text_list = []
    for key in range(25):
        decrypted_text_list.append(caesar_decrypt(stripText, key+1))
    return is_french(decrypted_text_list)[1]


