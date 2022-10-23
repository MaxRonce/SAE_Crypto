import unittest
from src.text_input import *

#test function for the function strip_puntuation(text: str) -> tuple[str, dict[int, Any]]:

class Test_text_input(unittest.TestCase):

    def test_strip_punctuation(self):
        texte = "Hello World!"
        texte_strip, dict = strip_puntuation(texte)
        self.assertEqual(texte_strip, "HELLOWORLD")
        self.assertEqual(dict, {5: " ", 11: "!"})

    def test_insert_punctuation(self):
        texte = "HELLOWORLD"
        dict = {5: " ", 11: "!"}
        texte_insert = insert_punctuation(texte, dict)
        self.assertEqual(texte_insert, "HELLO WORLD!")

    def test_text_format(self):
        texte = "Hello World!"
        texte_format = text_format(texte)
        self.assertEqual(texte_format, "HELLO WORLD!")