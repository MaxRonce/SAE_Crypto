from caesar import caesar_decrypt_all
import file
import is_french
import langid

def main():
    parent_path = file.get_parent_path()
    #Try all text with caesar 1st
    remaining_text = [1,2,3,4,5]
    all_decrypted = []
    for i in range(1,6):
        text = file.open_file(parent_path + f"/data/Texte{i}.txt")
        all_decrypted.append(caesar_decrypt_all(text))
        print(f"Texte{i} : {all_decrypted[i-1]}")

    choice = int(input("Quel texte est en français ? (1-5) : "))
    file.write_file(parent_path + f"/out/Texte{choice}_decrypted.txt", all_decrypted[choice-1])
    remaining_text.remove(choice)
    print(f"Texte non identifiés restants : {remaining_text}")

    #Try all text with affine 2nd
















if __name__ == "__main__":
    main()