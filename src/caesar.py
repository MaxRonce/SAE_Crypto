
from text_input import strip_puntuation, insert_punctuation, text_format
from is_french import is_french

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
    decrypted_text_list = []
    for key in range(25):
        decrypted_text_list.append(caesar_decrypt(text, key+1))
    return decrypted_text_list

if __name__ == "__main__":


    text = "Oh kdoo g'hqwuhh gx fkdwhdx hwdlw vl judqg txh od pdlvrq ghv Gxuvohb dxudlw sx b whqlu wrxwhhqwlhuh hw oh sodirqg vl kdxw tx'rq duulydlw sdv d o'dshufhyrlu. Ghv wrufkhv hqiodpphhv hwdlhqwilahhv dxa pxuv gh slhuuh, frpph d Julqjrwwv, hw xq vrpswxhxa hvfdolhu gh pdueuh shuphwwdlwgh prqwhu gdqv ohv hwdjhv."
    text1 = strip_puntuation(text)[0]
    print(text1)
    
    tmp = is_french(caesar_decrypt_all(text1))[1]
    print(insert_punctuation(tmp, strip_puntuation(text)[1]))
