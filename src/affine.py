import math
from src.is_french import *

#function do decrypt affine cipher, a and b are the keys

def decrypt_affine(ciphertext, a, b):
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                plaintext += chr((a * (ord(c) - ord('A') - b)) % 26 + ord('A'))
            else:
                plaintext += chr((a * (ord(c) - ord('a') - b)) % 26 + ord('a'))
        else:
            plaintext += c
    return plaintext

#function that test all possible keys and return a list of all possible plaintexts

def test_all_keys(ciphertext):
    plaintext_list = []
    for a in range(1, 26):
        if math.gcd(a, 26) == 1:
            for b in range(1, 26):
                plaintext_list.append(decrypt_affine(ciphertext, a, b))
    return plaintext_list

text = "EROCRJABGRJDZHZJOHWZQQANLNOGJGZIZDBOGJONQROHGZROBQQZON" #ciphertext
plaintext_list = test_all_keys(text)

is_fr = is_french(plaintext_list)
print(is_fr)




