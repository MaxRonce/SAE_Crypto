import numpy as np
ALPHABET= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_occurence_dict =  {
    'A': 8.4, 'B': 1.06, 'C': 3.03, 'D': 4.18,
    'E': 17.26, 'F': 1.12, 'G': 1.27, 'H': 0.92,
    'I': 7.34, 'J': 0.31, 'K': 0.05, 'L': 6.01,
    'M': 2.96, 'N': 7.13, 'O': 5.26, 'P': 3.01,
    'Q': 0.99, 'R': 6.55, 'S': 8.08, 'T': 7.07,
    'U': 5.74, 'V': 1.32, 'W': 0.04, 'X': 0.45,
    'Y': 0.3, 'Z': 0.12
}
#count occurence of each letter in the given text

def count_letters(text: str) -> dict:
    """
    It takes a string (no punctuation and UPPER) as input and returns a dictionary with the letters of the alphabet as keys and the number of times
    they appear in the string as values
    :param text: The text to be counted
    :return: A dictionary with the letters of the alphabet as keys and the number of times they appear in the string as
    values
    """
    text = list(text)
    letter_count_dict = {}
    for letter in ALPHABET:
        letter_count_dict[letter] = text.count(letter)
    return letter_count_dict

#calculate the percentage of each letter in the given text

def calculate_percentage(text: str) -> dict:
    """
    It takes a string (no punctuation and UPPER) as input and returns a dictionary with the letters of the alphabet as keys and the percentage of
    times they appear in the string as values
    :param text: The text to be counted
    :return: A dictionary with the letters of the alphabet as keys and the percentage of times they appear in the string as
    values
    """
    freq = {}
    for lettre in ALPHABET:
        freq[lettre] = 0.0
    for lettre in text:
        freq[lettre] += 1
    for lettre in ALPHABET:
        freq[lettre] /= len(text)
    return freq


#calculate the euclidean difference between the percentage of each letter in the given text and the percentage of each letter in the
#french language

def calculate_euclidean_difference(text: str) -> float:
    """
    It takes a string (no punctuation and UPPER) as input and returns the euclidean difference between the percentage of each letter in the given
    text and the percentage of each letter in the french language
    :param text: The text to be counted
    :return: A float
    """
    euclidean_difference = 0.0
    freq = calculate_percentage(text)
    for lettre in ALPHABET:
        euclidean_difference += (freq[lettre] - letter_occurence_dict[lettre])**2
    return np.sqrt(euclidean_difference)

#using the euclidean difference function above as a metric and the strip_punctuation function from text_input.py

def is_french(text_list: list) -> tuple:
    """
    It takes a list of strings as input and returns the string that is the most likely to be french and it's index in the list
    :param text_list: The list of strings to be checked
    :return: A tuple with the index of the string that is the most likely to be french and the string itself
    """
    euclidean_difference_list = []
    for text in text_list:
        euclidean_difference_list.append(calculate_euclidean_difference(text))
    return euclidean_difference_list.index(min(euclidean_difference_list))+1, text_list[euclidean_difference_list.index(min(euclidean_difference_list))]
