import unittest
from collections import namedtuple
from day_4 import number_of_valid_passphrases_without_duplicates
from day_4 import number_of_valid_passphrases_without_anagrams

class TestNumberOfValidPassphrases(unittest.TestCase):
    """Test number of valid passphrases."""

    def test_number_of_valid_passphrases_without_duplicates(self):
        Test = namedtuple('Test', ['phrases', 'expected'])
        tests = [Test(phrases=['aa bb'], expected=1),
                 Test(phrases=['aa bb cc dd ee',
                               'aa bb cc dd aa',
                               'aa bb cc dd aaa'],
                      expected=2)]

        for test in tests:
            result = number_of_valid_passphrases_without_duplicates(
              test.phrases)
            self.assertEqual(result, test.expected)

    def test_number_of_valid_passphrases_without_anagrams(self):
        Test = namedtuple('Test', ['phrases', 'expected'])
        tests = [Test(phrases=['aa bb'], expected=1),
                 Test(phrases=["abcde fghij",
                               "abcde xyz ecdab",
                               "a ab abc abd abf abj",
                               "iiii oiii ooii oooi oooo",
                               "oiii ioii iioi iiio"],
                      expected=3)]

        for test in tests:
            result = number_of_valid_passphrases_without_anagrams(
                test.phrases)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
