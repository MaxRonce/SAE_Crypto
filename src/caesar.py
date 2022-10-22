
from text_input import strip_puntuation, insert_punctuation, text_format
from is_french import is_french
from file import *

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#TODO fonction qui prend en para un txt -> str sans ponctu ni espace en maj, déchiffre avec un chiffrage cesar avec une clé donnée

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

#TODO fonction qui prend en para un txt -> test toutes les possibilités de clé et renvoie une liste de str contenant tous les txt déchiffrés
def caesar_decrypt_all(text: str) -> list:
    """
    It takes a string (no punctuation and UPPER) as input and returns a list of strings containing all the possible decrypted texts
    :param text: The text to be decrypted
    :return: A list of strings
    """
    stripText = strip_puntuation(text)[0]
    decrypted_text_list = []
    for key in range(25):
        decrypted_text_list.append(caesar_decrypt(stripText, key+1))
    return insert_punctuation(is_french(decrypted_text_list)[1], strip_puntuation(text)[1])

if __name__ == "__main__":

    text4 = "Zc krgfkr u'le ufzxk le rzi drikzrc jli c'fscfex tyrjjzj ul mrjzjkrj. Zc flmizk jfe wizxf dlirc, zc gizk ul crzk wifzu, zc slk le xireu sfc. Zc j'rgrzjrzk. Zc j'rjjzk jli jfe tfjp, zc gizk le aflierc hl'zc gritflilk u'le rzi uzjkirzk. Zc rccldr le tzxrizccf hl'zc wldr aljhl'rl sflk hlfzhl'zc kiflmrk jfe griwld ziizkrek. Zc kfljjr."
    print(caesar_decrypt_all(text4))

