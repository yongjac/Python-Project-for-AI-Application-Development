"""This module tests translator.py"""

import unittest

from machinetranslation import translator

class TestEnglishToFrench(unittest.TestCase):
    """This class test english to french translation"""
    def test1(self):
        """This function test english to french translation"""
        self.assertEqual(translator.english_to_french(None), '')
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        self.assertEqual(translator.english_to_french(''), '')

class TestEnglishToGerman(unittest.TestCase):
    """This class test english to german translation"""
    def test1(self):
        """This function test english to german translation"""
        self.assertEqual(translator.english_to_german(None), '')
        self.assertEqual(translator.english_to_german('Hello'), 'Hallo')
        self.assertEqual(translator.english_to_german(''), '')

if __name__ == '__main__':
    unittest.main()
