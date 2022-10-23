import math
from text_input import *

letter_occurence_dict = {"A" : 7.11, "B" : 1.14, "C" : 3.18, "D" : 3.67,
"E" : 12.10, "F" : 1.11, "G" : 1.23, "H" : 1.11, "I" : 6.59, "J" : 0.34, "K" : 0.29,
"L" : 4.96, "M" : 2.62, "N" : 6.39, "O" : 5.02, "P" : 2.49, "Q" : 0.65, "R" : 6.07,
"S" : 6.51, "T" : 5.92, "U" : 4.49, "V" : 1.11, "W" : 0.17, "X" : 0.32, "Y" : 0.46, "Z" : 0.15}
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def key_schedule(message: str, key: str)->list:
    # I will add the key to the text (as list of number)
    """
    Generate key for vigenere cipher
    :param message: example : "Hello World"
    :param key: ex : "ABC"
    :return: ex : [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    """
    key = list(key)
    key_full = []
    for i in range(len(message)):
        key_full.append(ord(key[i % len(key)]) - ord("A"))  # ord("A") = 65

    return key_full


def crytage_vigenere(message: str, key:str) -> str:
    cipher_text = []
    message = list(message)

    for i in range(len(message)):
        x = (ord(message[i]) + key[i]) % 26
        x += 65
        cipher_text.append(chr(x))
    return ("".join(cipher_text))

def decrytage_vigenere(message: str, key:str) -> str:
    origin_text = []
    message = list(message)

    for i in range(len(message)):
        x = (ord(message[i]) - key[i]) % 26
        x += 65
        origin_text.append(chr(x))
    return ("".join(origin_text))


def find_average_value_mod(liste : list)->list:
    half_len_list = int(len(liste) // 2)
    average_coincidence_index_mod_i = [[] for i in range(half_len_list)]

    for i in range(1,half_len_list+1):
        k = 0
        for j in range(len(liste)):
            if (j+1)%i == 0:
                average_coincidence_index_mod_i[i-1].append(liste[j])
        average_coincidence_index_mod_i[i-1] = sum(average_coincidence_index_mod_i[i-1])/len(average_coincidence_index_mod_i[i-1])

    return average_coincidence_index_mod_i


def find_key_length(cipher_text: str) -> int:
    """
    :param cipher_text:
    :return:
    calculate coincidence index for each key length
    return key length with the highest coincidence index
    """
    coincidence_index = []
    for i in range(1, 20):
        coincidence_index.append(find_coincidence_index(cipher_text[::i]))

    average_coincidence_index_mod_i = find_average_value_mod(coincidence_index)
    return average_coincidence_index_mod_i.index(max(average_coincidence_index_mod_i)) + 1



def find_coincidence_index(text):
    """
    :param text:
    :return:
    calculate coincidence index for a text
    """
    count_char = []
    coincidence_index = 0
    for i in alph:
        count_char.append(text.count(i))
    for i in count_char:
        coincidence_index += i * (i - 1)
    coincidence_index /= len(text) * (len(text) - 1)
    return coincidence_index

def group_text(text: str, key_length: int) -> list:
    """
    :param text:
    :param key_length:
    :return:
    group text by key length
    """
    text_group = [[] for i in range(key_length)]
    for i in range(key_length):
        text_group[i] = text[i::key_length]
    return text_group

def find_key_frequency_caesar(text):
    encrypt_key = 0
    lowest_difference = math.inf
    number_of_letters =sum(count_occurence(text).values())
    for key in range(1,26):
        temp_deciphered_text = caesar_decrypt(text,key)

        temp_occurence = {alph[i]:(count_occurence(temp_deciphered_text)[alph[i]]/number_of_letters)*100 for i in range(26)}

        temp_difference = math.sqrt(sum([(letter_occurence_dict[alph[i]] - temp_occurence[alph[i]])**2 for i in range(26)]))


        if temp_difference < lowest_difference:
            lowest_difference = temp_difference
            encrypt_key = key


    return encrypt_key

def find_key_frequency_vigenere(text, key_length):
    text_group = group_text(text, key_length)
    key = ""
    for i in range(key_length):
        key += alph[find_key_frequency_caesar(text_group[i])-13]
    return key
def caesar_decrypt(toEncrypt, key : int)->str:
    """
    :param toEncrypt:
    :param key:
    :return:
    decrypt a text with caesar cipher capital letters only
    """
    result = ""
    for i in range(len(toEncrypt)):
        char = toEncrypt[i]
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        else:
            result += char
    return result
def count_occurence(text)->dict:
    return {i : text.count(i) for i in alph}
def difference(text):
    #retourne la difference entre la frequence d'apparition des lettres dans le texte et la frequence d'apparition des lettres dans la langue
    count_occurence_dict = dict(count_occurence(text))
    return sum([abs(count_occurence_dict[i] * 100 / len(text) - letter_occurence_dict[i]) for i in alph])/26
1
def main():
    test_text2= "Hello World"
    test_key = "ABC"
    text, dict = strip_puntuation(test_text2)
    cipher_text = crytage_vigenere(text, key_schedule(text, test_key))


    key_len = find_key_length(cipher_text)
    print(f"La longueur de la clé est : {key_len}")
    text_group = group_text(cipher_text, find_key_length(cipher_text))

    key = find_key_frequency_vigenere(cipher_text, find_key_length(cipher_text))

    print(f"La clé est : {key}")

    print("Le texte decrypté est : ",insert_punctuation(decrytage_vigenere(cipher_text, key_schedule(cipher_text, key)),dict))


if __name__ in "__main__":
    main()