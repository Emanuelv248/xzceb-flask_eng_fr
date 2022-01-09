import unittest
from translator import french_To_English
from translator import english_To_French


class Testtranslator(unittest.TestCase): 
    def test_french_To_English(self): 
        self.assertEqual(french_To_English("Bonjour"), "Hello")
        

class Testtranslator(unittest.TestCase): 
    def test_english_To_French(self): 
        self.assertEqual(english_To_French("Hello"),"Bonjour")
        

unittest.main()