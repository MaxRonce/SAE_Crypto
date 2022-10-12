import unittest
from src.file import *

class Test_file(unittest.TestCase):

        def test_open_file(self):
            parent_path = get_parent_path()
            file_path = os.path.join(parent_path, "out", "test.txt")
            file_content = open_file(file_path)
            self.assertEqual(file_content, "Hello World!")

        def test_write_file(self):
            parent_path = get_parent_path()
            file_path = os.path.join(parent_path, "out", "test.txt")
            file_content = "Hello World!"
            write_file(file_path, file_content)
            file_content = open_file(file_path)
            self.assertEqual(file_content, "Hello World!")
