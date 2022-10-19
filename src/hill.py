import numpy as np

#split the text into blocks of size n
def split_text(text: list, n: int) -> list:
    """
    It takes a list and an integer as input and returns a list of list
    :param text: The text to be split
    :param n: The size of the blocks
    :return: A list of list
    """
    return [text[i:i + n] for i in range(0, len(text), n)]

#hill cipher encryption using split text

def encrypt_hill(text: list, key: list) -> str:
    """
    It takes a string and a list as input and returns the encrypted string
    :param text: The text to be encrypted
    :param key: The list that contains the key
    :return: The encrypted string
    """
    encrypted_text = []
    print(text)
    for block in text:
        encrypted_text.append(np.dot(block,key).tolist())
    return encrypted_text

def decrypt_hill(text: list, key: list) -> str:
    """
    It takes a string and a list as input and returns the decrypted string
    :param text: The text to be decrypted
    :param key: The list that contains the key
    :return: The decrypted string
    """
    decrypted_text = []
    for block in text:
        decrypted_text.append(np.dot(block,key).tolist())
    return decrypted_text

def main():

    key = [[1, 2], [3, 4]]
    text = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    text = split_text(text, 2)
    print(text)

    encrypted_text = encrypt_hill(text, key)
    print(encrypted_text)

    for elem in encrypted_text:
        for i in range(len(elem)):
            elem[i] = int(elem[i]) %26
    print(encrypted_text)


    key_inv = np.linalg.inv(key)
    decrypted_text = decrypt_hill(encrypted_text, key)
    for elem in decrypted_text:
        for i in range(len(elem)):
            elem[i] = int(elem[i]) %26
    print(decrypted_text)

if __name__ == "__main__":
    main()