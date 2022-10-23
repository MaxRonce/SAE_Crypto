ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import itertools
#substitution cipher for a given text and key(dictionnary)

def encrypt_substitution(text: str, key: dict) -> str:
    """
    It takes a string and a dictionnary as input and returns the encrypted string
    :param text: The text to be encrypted
    :param key: The dictionnary that contains the key
    :return: The encrypted string
    """
    text = list(text)
    for i in range(len(text)):
        if text[i] in ALPHABET:
            text[i] = key[text[i]]
    return "".join(text)


#test all possible keys for a given text

def test_all_keys(text: str) -> list:
    """
    It takes a string as input and returns a list of all possible keys
    :param text: The text to be tested
    :return: A list of all possible keys
    """
    key_list = []
    for key in itertools.permutations(ALPHABET):
        print(key)
        key_dict = dict(zip(ALPHABET, key))
        key_list.append(key_dict)
    return key_list

test_all_keys("ABC")



