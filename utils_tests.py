## Taken/credit from ChatGPT

import unittest
from utils import Utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.utils_instance = Utils()

    def test_reversed_with_integers(self):
        self.assertEqual(self.utils_instance.reversed_number(12345), 54321)
        self.assertEqual(self.utils_instance.reversed_number(-6789), -9876)

    def test_reversed_with_strings(self):
        with self.assertRaises(ValueError):
            self.utils_instance.reversed_number("12345")
        with self.assertRaises(ValueError):
            self.utils_instance.reversed_number("hello")

    def test_reversed_with_floats(self):
        with self.assertRaises(ValueError):
            self.utils_instance.reversed_number(123.45)
        with self.assertRaises(ValueError):
            self.utils_instance.reversed_number(-6.789)

    def test_formatter_with_integers(self):
        binary, octal = self.utils_instance.formatter(42)
        self.assertEqual(binary, "101010")
        self.assertEqual(octal, "52")

    def test_formatter_with_strings(self):
        with self.assertRaises(ValueError):
            self.utils_instance.formatter("42")
        with self.assertRaises(ValueError):
            self.utils_instance.formatter("hello")

    def test_formatter_with_floats(self):
        with self.assertRaises(ValueError):
            self.utils_instance.formatter(3.14)
        with self.assertRaises(ValueError):
            self.utils_instance.formatter(-0.5)

if __name__ == "__main__":
    unittest.main()
