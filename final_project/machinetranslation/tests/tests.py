import unittest
from translator import french_to_english,english_to_french

class TestTranslator(unittest.TestCase):

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english(None), None)
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french(None), None)
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

if __name__ == "__main__":
    unittest.main()