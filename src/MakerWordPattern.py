from text_input import strip_puntuation, insert_punctuation, text_format
from is_french import *
import pprint


TEXT = 'AZEFSFV'

def get_word_pattern(word):
    word = word.upper()
    next_num = 0
    letter_nums = {}
    word_pattern = []

    for letter in word:
        if letter not in letter_nums:
            letter_nums[letter] = str(next_num)
            next_num += 1
        word_pattern.append(letter_nums[letter])
    return ".".join(word_pattern)

def main ():
    allPaterns = {}

    fo = open('data/french.txt')
    wordList = fo.read().split('\n')
    fo.close()

    for word in wordList:
        pattern = get_word_pattern(word)
        if pattern not in allPaterns:
            allPaterns[pattern] = [word]
        else:
            allPaterns[pattern].append(word)

    fo = open('data/WordPattern.py','w')
    fo.write('allPatterns = ' + pprint.pformat(allPaterns))
    fo.close()


if __name__ == '__main__':
    main()