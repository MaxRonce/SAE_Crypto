import unittest
from src.is_french import count_letters, calculate_percentage, calculate_euclidean_difference, is_french

class Test_french(unittest.TestCase):

    #test function for the function count_letters(text: str) -> dict:
    def test_count_letters(self):
        text = "HELLOWORLD"
        letter_count_dict = count_letters(text)
        self.assertEqual(letter_count_dict, {'A': 0, 'B': 0, 'C': 0, 'D': 1, 'E': 1, 'F': 0, 'G': 0, 'H': 1, 'I': 0, 'J': 0, 'K': 0, 'L': 3, 'M': 0, 'N': 0, 'O': 2, 'P': 0, 'Q': 0, 'R': 1, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 1, 'X': 0, 'Y': 0, 'Z': 0})

    #test function for the function calculate_percentage(text: str) -> dict:
    def test_calculate_percentage(self):
        text = "HELLOWORLD"
        letter_percentage_dict = calculate_percentage(text)
        self.assertEqual(letter_percentage_dict,{'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 10.0, 'E': 10.0, 'F': 0.0, 'G': 0.0, 'H': 10.0, 'I': 0.0, 'J': 0.0, 'K': 0.0, 'L': 30.0, 'M': 0.0, 'N': 0.0, 'O': 20.0, 'P': 0.0, 'Q': 0.0, 'R': 10.0, 'S': 0.0, 'T': 0.0, 'U': 0.0, 'V': 0.0, 'W': 10.0, 'X': 0.0, 'Y': 0.0, 'Z': 0.0})

    #test function for the function calculate_euclidean_difference(text: str) -> float:
    def test_calculate_euclidean_difference(self):
        text = "HELLOWORLD"
        euclidean_difference = calculate_euclidean_difference(text)
        self.assertEqual(euclidean_difference, 36.73)

    #test function for the function is_french(text: str) -> :
    def test_is_french(self):
        text_list = ["BONJOUR", "HELLO WORLD", "BONJOUR MONDE"]
        self.assertEqual(is_french(text_list)[1], "BONJOUR MONDE")
        self.assertEqual(is_french(text_list)[0], 3)


