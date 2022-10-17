import unittest
from src.caesar import *

TEST_TEXT = "HELLOWORLD"


class TestCaesar(unittest.TestCase):

    def test_caesar_decrypt(self):
        key = 1
        self.assertEqual(caesar_decrypt(TEST_TEXT, key), "IFMMPXPSME")

    def test_caesar_decrypt_all(self):
        self.assertEqual(caesar_decrypt_all(TEST_TEXT), ['IFMMPXPSME', 'JGNNQYQTNF', 'KHOORZRUOG', 'LIPPSASVPH', 'MJQQTBTWQI', 'NKRRUCUXRJ', 'OLSSVDVYSK', 'PMTTWEWZTL', 'QNUUXFXAUM', 'ROVVYGYBVN', 'SPWWZHZCWO', 'TQXXAIADXP', 'URYYBJBEYQ', 'VSZZCKCFZR', 'WTAADLDGAS', 'XUBBEMEHBT', 'YVCCFNFICU', 'ZWDDGOGJDV', 'AXEEHPHKEW', 'BYFFIQILFX', 'CZGGJRJMGY', 'DAHHKSKNHZ', 'EBIILTLOIA', 'FCJJMUMPJB', 'GDKKNVNQKC'])
