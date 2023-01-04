

import unidecode
import string
import re
import numpy as np
import matplotlib.pyplot as plt
import codecs
import pickle

def text_format(text_input : str) -> str:
    """
    It takes a string as input, converts it to uppercase, and then removes any accents

    :param text_input: The text you want to format
    :return: A string
    """
    text_input = text_input.upper()
    try:
        text_input = unidecode.unidecode(text_input)
    except NameError:
        pass
    return str(text_input)

def strip_puntuation(text: str):
    """
    It takes a string, formats it, turns it into a list, makes a copy of the list, and then creates a dictionary of the
    punctuation and spaces in the original list. Then it removes the punctuation and spaces from the copy and returns the
    copy as a string

    :param text: the text to be stripped of punctuation
    :type text: str
    :return: A tuple with the first element being the string without punctuation and the second element being a dictionary
    with the punctuation and spaces as keys and the punctuation and spaces as values.
    """
    text = text_format(text)
    text = list(text)
    text_copy = text
    dic_text = {}

    for i in range(len(text)):
        if text[i] in string.punctuation+" ":
            dic_text[i] = text[i]
    for i in dic_text.values():
        text_copy.remove(i)

    return "".join(text_copy), dic_text

def insert_punctuation(text: str, dic: dict) -> str:
    """
    It takes a string and a dictionary as input, and returns a string with punctuation inserted at the positions specified
    in the dictionary

    :param text: the text to be punctuated
    :type text: str
    :param dic: a dictionary of punctuation marks and their positions in the text
    :type dic: dict
    :return: A string with punctuation inserted at the correct locations. Uppercase
    """
    text = list(text)
    for i in dic.keys():
        text.insert(i, dic[i])
    return "".join(text)

#convert a text into a numpy array of number, A = 1st letter of the alphabet, B = 2nd letter of the alphabet, etc.

def text_to_number(text: str) -> np.ndarray:
    """
    It takes CLEAN text as input and returns a numpy array of numbers

    :param text: The text to be converted
    :return: A numpy array of numbers
    """
    text = text_format(text)
    text = list(text)
    for i in range(len(text)):
        text[i] = ord(text[i]) - 64
    text = np.array(text)
    return text
#convert a numpy array of number into a text
def number_to_text(text) -> str:
    """
    It takes a numpy array of numbers as input and returns a string
    :param text: The numpy array of numbers to be converted
    :return: A string
    """
    text = list(text)
    for i in range(len(text)):
        text[i] = chr(text[i] + 64)
    text = "".join(text)
    return text

# flatten an array of arrays into a single array
def flatten_array(array: np.ndarray) -> np.ndarray:
    """
    It takes a numpy array of arrays as input and returns a single numpy array

    :param array: The numpy array of arrays to be flattened
    :return: A single numpy array
    """
    array = array.flatten()
    return array


def char_to_id(c):
    return 0 if c == " " else ord(c) - 64


def id_to_char(i):
    return " " if i == 0 else chr(i + 64)


def apply_code(s, code):
    res = ""
    for c in s:
        i = char_to_id(c)
        res += id_to_char(code[i])
    return res


def invert_code(code):
    res = [-1] * 27
    for i in range(27):
        j = code.index(i)
        res[i] = j
    return res


def transform_to_caps(s):
    # Substitution "oe"
    s = re.sub(chr(338), "OE", s)
    s = re.sub(chr(339), "OE", s)

    # Replace accents, turn ponctuation signs into space
    # In the end, everything should be space (ascii 32) or capitals A-Z (ascii 65-90)
    to_A = [192, 224, 226]
    to_C = [199, 231]
    to_E = [200, 201, 202, 232, 233, 234, 235]
    to_I = [238, 239]
    to_O = [244]
    to_U = [249, 251, 252]
    to_SPACE = list(range(33, 65)) + [171, 187, 8217, 8230]

    s_sub = ""
    for c in s:
        c2 = c
        if (ord(c2) in range(97, 123)):
            c2 = chr(ord(c2) - 32)
        if ord(c2) in to_SPACE:
            c2 = " "
        if ord(c2) in to_A:
            c2 = "A"
        if ord(c2) in to_C:
            c2 = "C"
        if ord(c2) in to_E:
            c2 = "E"
        if ord(c2) in to_I:
            c2 = "I"
        if ord(c2) in to_O:
            c2 = "O"
        if ord(c2) in to_U:
            c2 = "U"
        s_sub += c2

    # Remove multiple spaces
    res = re.sub('\s+', ' ', s_sub)

    return res


def load_corpus(filename):
    # Load the text and make it one string
    encoding = "utf-8"
    whole_text = ""
    with codecs.open(filename, "r", encoding) as lines:
        for l in lines:
            # :-2 to remove endline and then concatenate
            whole_text = whole_text + l[:-2] + " "

    return whole_text


def count_correct_words(s, dictionnary_words):
    cnt = 0
    word_list = s.split(" ")
    for w in word_list:
        if w in dictionnary_words:
            cnt += 1
    return cnt, len(word_list)


def score_correct_words(s, dictionnary_words):
    res = 0
    tot = 0
    word_list = s.split(" ")
    for w in word_list:
        if w in dictionnary_words:
            res += len(w)
        tot += len(w)
    return res / tot


def find_wrong_words(s, dictionnary_words):
    word_list = s.split(" ")
    for w in word_list:
        if w not in dictionnary_words:
            print(w)


def frequency_order(s):
    res = np.zeros(26)
    for i in range(26):
        res[i] = s.count(chr(65 + i))
    return list(1 + np.argsort(res)[::-1])


def count_bigrams(corpus, outfile, imagefile=None):
    # Count of ASCII characters to check everything is ok
    count = np.zeros(512)
    for c in corpus:
        count[ord(c)] += 1

    for i in range(512):
        if count[i] > 0:
            print(str(i) + " " + chr(i) + " " + str(count[i]))

    # Now we are ready to count the bigrams
    bigrams = np.zeros((27, 27), dtype='int32')
    i = 0
    for c in corpus:
        j = 0 if c == " " else ord(c) - 64
        bigrams[i, j] += 1
        i = j

    bigrams.tofile(outfile)

    if imagefile != None:
        # Plot of the matrix, normalized per line
        p2D = bigrams.astype('float') / np.tile(sum(bigrams.T), (27, 1)).T
        p2D[np.isnan(p2D)] = 0

        alpha = 0.33
        p2Da = p2D ** alpha
        plt.figure(figsize=(8, 8))
        plt.imshow(p2Da, interpolation='nearest', cmap='inferno')
        plt.axis('off')

        for ip, i in enumerate([32] + list(range(65, 91))):
            plt.text(-1, ip, chr(i), horizontalalignment='center',
                     verticalalignment='center')
            plt.text(ip, -1, chr(i), horizontalalignment='center',
                     verticalalignment='center')
        plt.savefig(imagefile)

        return p2Da


def create_dictionnary():
    filepath = "../data/liste.de.mots.francais.frgut.txt"

    whole_dico = ""
    with codecs.open(filepath, "r", "utf-8") as lines:
        for l in lines:
            whole_dico += l[:-1] + " "

    dico = transform_to_caps(whole_dico)
    # We add simple letters and qu'
    words = ['QU'] + ['A', 'C', 'D', 'L', 'Y', 'M', 'N', 'S', 'T'] + dico.split(" ")

    pickle.dump(words, open("../data/dictionnary.data", "wb"))


emolist = [
    '\U0001F600',
    '\U0001F601',
    '\U0001F602',
    '\U0001F603',
    '\U0001F604',
    '\U0001F605',
    '\U0001F606',
    '\U0001F607',
    '\U0001F608',
    '\U0001F609',
    '\U0001F610',
    '\U0001F611',
    '\U0001F612',
    '\U0001F613',
    '\U0001F614',
    '\U0001F615',
    '\U0001F616',
    '\U0001F617',
    '\U0001F618',
    '\U0001F619',
    '\U0001F620',
    '\U0001F621',
    '\U0001F622',
    '\U0001F623',
    '\U0001F624',
    '\U0001F625']

