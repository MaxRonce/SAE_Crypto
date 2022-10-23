import math
from is_french import *

#function do decrypt affine cipher, a and b are the keys

def decrypt_affine(ciphertext, a, b):
    """
    It takes a ciphertext and two integers, and returns the plaintext

    :param ciphertext: The text to be decrypted
    :param a: the multiplicative key
    :param b: the shift value
    :return: The plaintext is being returned.
    """
    plaintext = ""
    for c in ciphertext:
        plaintext += chr((a * (ord(c) - ord('A') - b)) % 26 + ord('A'))
    return plaintext

#function that test all possible keys and return a list of all possible plaintexts

def test_all_keys(ciphertext):
    """
    It takes a ciphertext and returns a list of all possible plaintexts

    :param ciphertext: the ciphertext you want to decrypt
    :return: A list of all possible plaintexts.
    """
    plaintext_list = []
    for a in range(1, 26):
        if math.gcd(a, 26) == 1:
            for b in range(1, 26):
                plaintext_list.append(decrypt_affine(ciphertext, a, b))
    return plaintext_list




