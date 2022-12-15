import file
import is_french
from caesar import *
from vigenere import *
from affine import *
from substitution import *
import hill_optimised as hill


# import hill


def choice_input(remaining_text):
    try:
        choice = int(input(f"Quel texte est le français ? {remaining_text} : "))
        if choice not in remaining_text:
            raise ValueError
    except ValueError:
        print("Choix invalide")
        return choice_input(remaining_text)
    return choice


def main():
    parent_path = file.get_parent_path()
    print("--------------------")
    print("Caesar : ")
    # Try all text with caesar 1st
    remaining_text = [1, 2, 3, 4, 5]
    all_decrypted = []
    for i in range(1, 6):
        print(" ")
        text = file.open_file(parent_path + f"/data/Texte{i}.txt")
        all_decrypted.append(caesar_decrypt_all(text))
        # insert punctuation
        punctuation = file.open_file(parent_path + f"/data/Punctuation/Punctuation_{i}.json", return_type="Json")
        unciphered_text = insert_punctuation(all_decrypted[i - 1], punctuation)
        all_decrypted[i - 1] = unciphered_text
        print(f"Texte{i} : {unciphered_text}")

    choice = choice_input(remaining_text)
    file.write_file(parent_path + f"/out/Texte{choice}_decrypted.txt", all_decrypted[choice - 1])
    remaining_text.remove(choice)
    print(f"Texte non identifiés restants : {remaining_text}")

    # Try all text with affine 2nd
    print("--------------------")
    print("Affine : ")
    all_decrypted = []
    for text_num in remaining_text:
        print(" ")
        load_text = file.open_file(parent_path + f"/data/Clean_text/Clean_text_{text_num}.txt")
        plaintext_list = test_all_keys(load_text)
        all_decrypted.append(is_french(plaintext_list)[1])

        # insert punctuation
        punctuation = file.open_file(parent_path + f"/data/Punctuation/Punctuation_{text_num}.json", return_type="Json")
        unciphered_text = insert_punctuation(is_french(plaintext_list)[1], punctuation)

        print(f"Texte{text_num} : {unciphered_text}")

    choice = choice_input(remaining_text)
    remaining_text.remove(choice)
    french_text = all_decrypted[choice - 1]

    # insert punctuation
    punctuation = file.open_file(parent_path + f"/data/Punctuation/Punctuation_{choice}.json", return_type="Json")
    unciphered_text = insert_punctuation(french_text, punctuation)
    file.write_file(parent_path + f"/out/Texte{choice}_decrypted.txt", unciphered_text)
    print(f"Texte {choice} déchiffré : {unciphered_text}")
    print(f"Texte non identifiés restants : {remaining_text}")

    # try all text with vigenere 3rd
    print("--------------------")
    print("Vigenere : ")
    all_decrypted = []
    for text_num in remaining_text:
        print(" ")
        load_text = file.open_file(parent_path + f"/data/Clean_text/Clean_text_{text_num}.txt")
        key_len = find_key_length(load_text)
        text_group = group_text(load_text, key_len)
        key = find_key_frequency_vigenere(load_text, key_len)
        unciphered_text = decrytage_vigenere(load_text, key_schedule(load_text, key))
        # insert punctuation
        punctuation = file.open_file(parent_path + f"/data/Punctuation/Punctuation_{text_num}.json", return_type="Json")
        unciphered_text = insert_punctuation(unciphered_text, punctuation)
        print(f"Texte{text_num} : {unciphered_text}")
        all_decrypted.append((unciphered_text, key, key_len))

    choice = choice_input(remaining_text)
    remaining_text.remove(choice)
    french_text = all_decrypted[choice - 2][0]

    file.write_file(parent_path + f"/out/Texte{choice}_decrypted.txt", french_text)
    print(f"Texte {choice} déchiffré : {french_text}, \n clé : {all_decrypted[choice - 2][1]}")
    print(f"Texte non identifiés restants : {remaining_text}")

    # try all text with HILL 4th

    print("--------------------")
    print("HILL : ")
    print("WARNING : L'algorithme de Hill est très long à calculer, vous pouvez prendre un café")
    print("Average time : 1min on a 2.5Ghz CPU, 8GB RAM, and 20sec on a 3.5Ghz CPU, 16GB RAM")
    all_decrypted = []
    for text_num in remaining_text:
        print(" ")
        text = file.open_file(parent_path + f"/data/Texte{text_num}.txt")
        unciphered_text = hill.main(text)  # note that the text is already clean and have punctuation
        all_decrypted.append(unciphered_text)
        print(f"Texte{text_num} : {unciphered_text}")

    choice = choice_input(remaining_text)
    remaining_text.remove(choice)
    french_text = all_decrypted[choice - 3]

    file.write_file(parent_path + f"/out/Texte{choice}_decrypted.txt", french_text)
    print(f"Texte {choice} déchiffré : {french_text}")
    print(f"Texte non identifiés restants : {remaining_text}")

    # try all text with Substitution 5th
    print("--------------------")
    print("Substitution :")
    print("WARNING : L'algorithme de Substitution est très long à calculer, vous pouvez maintenant boire votre café")

    unciphered_text = substitution(file.open_file(parent_path + "/data/Texte5.txt"))
    print("Texte 5 : ", unciphered_text)
    file.write_file(parent_path + f"/out/Texte5_decrypted.txt", unciphered_text)
    print("-" * 50)
    print("fin du programme")


if __name__ == "__main__":
    main()
