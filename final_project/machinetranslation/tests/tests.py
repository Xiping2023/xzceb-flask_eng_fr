''' implements a unit test for translator'''
import unittest
import translator

class Testing(unittest.TestCase):
    ''' perform unit test on translator methods'''

    def test_boolean(self):
        ''' test for null input for translation method and
            translation of the given word
        '''
        english_input = 'Hello'
        self.assertIsNotNone(english_input, 'test value is not null.')
        translated_french = translator.english_to_french(english_input)
        self.assertEqual(translated_french, 'Bonjour', 'They are equal.')

        french_input = 'Bonjour'
        self.assertIsNotNone(french_input, 'test value is not null.')
        translated_english = translator.french_to_english(french_input)
        self.assertEqual(translated_english, 'Hello', 'They are equal.')

if __name__ == '__main__':
    unittest.main()
