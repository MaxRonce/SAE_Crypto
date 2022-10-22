
import file
import is_french
from caesar import *
from vigenere import *
from affine import *

def main():
    parent_path = file.get_parent_path()
    print("--------------------")
    print("Caesar : ")
    # Try all text with caesar 1st
    remaining_text = [1, 2, 3, 4, 5]
    all_decrypted = []
    for i in range(1, 6):
        text = file.open_file(parent_path + f"/data/Texte{i}.txt")
        all_decrypted.append(caesar_decrypt_all(text))
        print(f"Texte{i} : {all_decrypted[i - 1]}")

    choice = int(input("Quel texte est en français ? (1-5) : "))
    file.write_file(parent_path + f"/out/Texte{choice}_decrypted.txt", all_decrypted[choice - 1])
    remaining_text.remove(choice)
    print(f"Texte non identifiés restants : {remaining_text}")

    #Try all text with affine 2nd
    print("--------------------")
    print("Affine : ")
    all_decrypted = []
    for text_num in remaining_text:
        load_text = file.open_file(parent_path + f"/data/Clean_text/Clean_text_{text_num}.txt")
        plaintext_list = test_all_keys(load_text)
        all_decrypted.append(is_french(plaintext_list)[1])
        print(f"Texte{text_num} : {is_french(plaintext_list)[1]}")

    choice = int(input(f"Quel texte est en français ? ({remaining_text}) : "))
    remaining_text.remove(choice)
    french_text = all_decrypted[choice - 1]

    #insert punctuation
    punctuation = file.open_file(parent_path + f"/data/Punctuation/Punctuation_{choice}.json", return_type="Json")
    unciphered_text = insert_punctuation(french_text, punctuation)
    file.write_file(parent_path + f"/out/Texte{choice}_decrypted.txt", unciphered_text)
    print(f"Texte {choice} déchiffré : {unciphered_text}")
    print(f"Texte non identifiés restants : {remaining_text}")



    #try all text with vigenere 3rd
    print("--------------------")
    print("Vigenere : ")
    all_decrypted = []
    for text_num in remaining_text:
        load_text = file.open_file(parent_path + f"/data/Clean_text/Clean_text_{text_num}.txt")
        key_len = find_key_length(load_text)
        text_group = group_text(load_text, key_len)
        key = find_key_frequency_vigenere(load_text, key_len)
        unciphered_text = decrytage_vigenere(load_text, key_schedule(load_text, key))
        print(f"Texte{text_num} : {unciphered_text}")
        all_decrypted.append((unciphered_text,key,key_len))

    choice = int(input(f"Quel texte est en français ? ({remaining_text}) : "))
    remaining_text.remove(choice)
    french_text = all_decrypted[choice - 2][0]

    # insert punctuation
    punctuation = file.open_file(parent_path + f"/data/Punctuation/Punctuation_{choice}.json", return_type="Json")
    unciphered_text = insert_punctuation(french_text, punctuation)
    file.write_file(parent_path + f"/out/Texte{choice}_decrypted.txt", unciphered_text)
    print(f"Texte {choice} déchiffré : {unciphered_text}, \n clé : {all_decrypted[choice - 2][1]}")
    print(f"Texte non identifiés restants : {remaining_text}")

if __name__ == "__main__":
    main()