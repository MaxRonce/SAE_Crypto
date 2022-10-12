ALPHABET= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_occurence_dict = {"A" : 7.11, "B" : 1.14, "C" : 3.18, "D" : 3.67,
"E" : 12.10, "F" : 1.11, "G" : 1.23, "H" : 1.11, "I" : 6.59, "J" : 0.34, "K" : 0.29,
"L" : 4.96, "M" : 2.62, "N" : 6.39, "O" : 5.02, "P" : 2.49, "Q" : 0.65, "R" : 6.07,
"S" : 6.51, "T" : 5.92, "U" : 4.49, "V" : 1.11, "W" : 0.17, "X" : 0.32, "Y" : 0.46, "Z" : 0.15}

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
    letter_count_dict = count_letters(text)
    letter_percentage_dict = {}
    for letter in ALPHABET:
        letter_percentage_dict[letter] = round((letter_count_dict[letter] / len(text)) * 100, 2)
    return letter_percentage_dict

#calculate the euclidean difference between the percentage of each letter in the given text and the percentage of each letter in the
#french language

def calculate_euclidean_difference(text: str) -> float:
    """
    It takes a string (no punctuation and UPPER) as input and returns the euclidean difference between the percentage of each letter in the given
    text and the percentage of each letter in the french language
    :param text: The text to be counted
    :return: A float
    """
    letter_percentage_dict = calculate_percentage(text)
    euclidean_difference = 0
    for letter in ALPHABET:
        euclidean_difference += (letter_percentage_dict[letter] - letter_occurence_dict[letter]) ** 2
    return round(euclidean_difference ** 0.5, 2)

#TODO function is_french that takes a list of strings and returns the string that is the most likely to be french and it's index in the list,
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
    return euclidean_difference_list.index(min(euclidean_difference_list)), text_list[euclidean_difference_list.index(min(euclidean_difference_list))]


