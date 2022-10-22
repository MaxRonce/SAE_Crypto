import math
from text_input import *

letter_occurence_dict = {"A" : 7.11, "B" : 1.14, "C" : 3.18, "D" : 3.67,
"E" : 12.10, "F" : 1.11, "G" : 1.23, "H" : 1.11, "I" : 6.59, "J" : 0.34, "K" : 0.29,
"L" : 4.96, "M" : 2.62, "N" : 6.39, "O" : 5.02, "P" : 2.49, "Q" : 0.65, "R" : 6.07,
"S" : 6.51, "T" : 5.92, "U" : 4.49, "V" : 1.11, "W" : 0.17, "X" : 0.32, "Y" : 0.46, "Z" : 0.15}
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

test_text2 = "Les grandes personnes m’ont conseillé de laisser de côté les dessins de serpents boas ouverts ou fermés, et de m’intéresser plutôt à la géographie, à l’histoire, au calcul et à la grammaire. " \
"C’est ainsi que j’ai abandonné, à l’âge de six ans, une magnifiquecarrière de peintre. J’avais été découragé par l’insuccès de mondessin numéro 1 et de mon dessin numéro 2. Les grandes personnes ne" \
" comprennent jamais rien toutes seules, et c’est fatigant, pour les enfants, " \
"de toujours et toujours leur donner desexplications.J’ai donc dû choisir un autre métier et j’ai appris à piloterdes avions. J’ai volé un peu partout dans le monde. Et la géographie, c’est exact," \
" m’a beaucoup servi. Je savais reconnaître,du premier coup d’œil, la Chine de l’Arizona. C’est très utile, sil’on est égaré pendant la nuit.J’ai ainsi eu, au cours de ma vie, des tas de contacts" \
" avecdes tas de gens sérieux. J’ai beaucoup vécu chez les grandes personnes. Je les ai vues de très près. Ça n’a pas trop amélioré monopinion.Quand j’en rencontrais une qui me paraissait un peu " \
"lucide, je faisais l’expérience sur elle de mon dessin numéro 1 quej’ai toujours conservé. Je voulais savoir si elle était vraimentcompréhensive. Mais toujours elle me répondait : « C’est unchapeau. " \
"» Alors je ne lui parlais ni de serpents boas, ni de forêts vierges, ni d’étoiles. Je me mettais à sa portée. Je lui parlais de bridge, de golf, de politique et de cravates." \
" Et la grande personne était bien contente de connaître un homme aussi raisonnable."
"Mais le renard revint à son idée Ma vie est monotone. Je chasse les poules, les hommes me chassent. Toutes les poules se ressemblent, et tous les hommes se ressemblent. Je m’ennuie donc un peu. Mais, si tu" \
"m’apprivoises, ma vie sera comme ensoleillée. Je connaîtrai un bruit de pas qui sera différent de tous les autres. Les autres pas me font rentrer sous terre. Le tien m’appellera hors du terrier,"\
"comme une musique. Et puis regarde ! Tu vois, là-bas, les champs de blé ? Je ne mange pas de pain. Le blé pour moi est inutile. Les champs de blé ne me rappellent rien. " \
"Et ça, c’est triste ! Mais tu as des cheveux couleur d’or. Alors ce sera merveilleux quand tu m’auras apprivoisé ! Le blé, qui est doré, me" \
"fera souvenir de toi. Et j’aimerai le bruit du vent dans le blé…Le renard se tut et regarda longtemps le petit prince : S’il te plaît… apprivoise-moi ! dit-il.Je veux bien, répondit le petit prince, mais je n’ai pas" \
"beaucoup de temps. J’ai des amis à découvrir et beaucoup de choses à connaître. – On ne connaît que les choses que l’on apprivoise, dit le renard. Les hommes n’ont plus le temps de rien connaître. Ils" \
"achètent des choses toutes faites chez les marchands. Mais comme il n’existe point de marchands d’amis, les hommes n’ont plus d’amis. Si tu veux un ami, apprivoise-moi ! – Que faut-il faire ? dit le petit prince." \
"– Il faut être très patient, répondit le renard. Tu t’assoiras d’abord un peu loin de moi, comme ça, dans l’herbe. Je te regarderai du coin de l’œil et tu ne diras rien. Le langage est source de malentendus. Mais, chaque jour, tu pourras t’asseoir" \
"un peu plus près…  Le lendemain revint le petit prince. – Il eût mieux valu revenir à la même heure, dit le renard. Si tu viens, par exemple, à quatre heures de l’après-midi, dès" \
" trois heures je commencerai d’être heureux. Plus l’heure avancera, plus je me sentirai heureux. À quatre heures, déjà, je m’agiterai et m’inquiéterai ; je découvrirai le prix du bonheur !" \
"Mais si tu viens n’importe quand, je ne saurai jamais à quelle heure m’habiller le cœur… Il faut des rites. – Qu’est-ce qu’un rite ? dit le petit prince. – C’est aussi quelque chose de trop oublié, dit le renard." \
" C’est ce qui fait qu’un jour est différent des autres jours, une heure, des autres heures. Il y a un rite, par exemple, chez mes chasseurs. Ils dansent le jeudi avec les filles du village. Alors le"

test_key = "LIVRE"

def key_schedule(message: str, key: str):
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