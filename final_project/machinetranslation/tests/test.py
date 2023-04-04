import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test eng to french equal.
        self.assertNotEqual(english_to_french("None"), '')  #test eng to french not equal.

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test french to eng equal.
        self.assertNotEqual(french_to_english("None"), '')  # test french to eng not equal.

unittest.main()
