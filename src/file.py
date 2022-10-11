import os
#abstract path of the parent folder

def get_parent_path() -> str:
    """
    It returns the path of the parent folder
    :return: A string
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#Open the given file and read it, stock it in a variable

def open_file(file_path: str) -> str:
    """
    It takes a string as input and returns the content of the file at the given path
    :param file_path: The path of the file to be opened
    :return: A string
    """
    with open(file_path, "r") as file:
        file_content = file.read()
    return file_content

#function that take a string as input and write it in a file, if then file doesn't exist, it creates it into SAE_Crypto/out folder

def write_file(file_path: str, file_content: str) -> None:
    """
    It takes a string as input and write it in a file, if then file doesn't exist, it creates it into SAE_Crypto/out folder
    :param file_path: The path of the file to be written
    :param file_content: The content of the file to be written
    :return: None
    """
    with open(file_path, "w") as file:
        file.write(file_content)


if __name__ == "__main__":
    parent_path = get_parent_path()
    file_path = os.path.join(parent_path, "out", "test.txt")
    file_content = "Hello World!"
    write_file(file_path, file_content)