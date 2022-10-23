
from text_input import strip_puntuation, insert_punctuation, text_format
from is_french import *
import random
from MakerWordPattern import *
import SAE_Crypto.data.WordPattern as wp


def split_text(text)-> list[str]:
    '''return a list of 20 random words from the text'''
    text = text_format(text)
    text = strip_puntuation(text, mode='substi')[0]
    text = text.split()

    list_words = []
    for i in range(20):
        list_words.append(random.choice(text))
    return list_words


def get_pattern_list (word_list:list[str]) -> None:
    listpattern = []
    for word in word_list:
        if get_word_pattern(word) not in listpattern:
            listpattern.append(get_word_pattern(word))
    return listpattern


def compare_pattern (pattern_list:list[str]) -> dict[str, list[str]]:
    patterns = {}
    for pattern in pattern_list:
        for word in wp.allPatterns:
            if pattern == word:
                patterns[word] = wp.allPatterns[word]
    return patterns



def main():
    tmp = split_text("Os dom sb kbrog : wf bok bykg-ewzbof ywm lwoxo r'wf zglmgf, hwol wf mbfug, hwol wf ygv-mkgm, hwol wf egmossgf dol bw ugwm rw pgwk. Rwmkgfe eibfmb rw Sbfndbff, Zbkzbkb wf dbrkoubs r'Bkbugf, Lmoei-Kbfrbss wf bok r' Borb.")
    print(get_pattern_list(tmp))
    #print(text_format("hello world"))
    #print(strip_puntuation("hello world"))
    print(compare_pattern(get_pattern_list(tmp)))


if __name__ == '__main__':
    main()
