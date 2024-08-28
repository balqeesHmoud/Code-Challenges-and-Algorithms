import unittest
from challenge02 import first_repeated_word  
class TestFirstRepeatedWord(unittest.TestCase):
    
    def test_repeated_word(self):
        result = first_repeated_word("ASAC is a department at LTUC. ASAC teaches programming in LTUC.")
        self.assertEqual(result, 'ASAC')
    
    def test_no_repetition(self):
        result = first_repeated_word("I am learning programming at ASAC.")
        self.assertEqual(result, 'No Repetition')
    
    def test_repeated_word_with_punctuation(self):
        result = first_repeated_word("Hello, hello world! Hello?")
        self.assertEqual(result, 'hello')
    
    def test_empty_string(self):
        result = first_repeated_word("")
        self.assertEqual(result, 'No Repetition')
    
    def test_single_word(self):
        result = first_repeated_word("word")
        self.assertEqual(result, 'No Repetition')
    
    def test_case_sensitivity(self):
        result = first_repeated_word("Word word WORD")
        self.assertEqual(result, 'word')

if __name__ == '__main__':
    unittest.main()
