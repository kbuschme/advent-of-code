from collections import Counter
"""
Advent of Code 2017

https://adventofcode.com/2017/day/4

--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use
a passphrase instead of simply a password. A passphrase consists of a series
of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

  * aa bb cc dd ee is valid.
  * aa bb cc dd aa is not valid - the word aa appears more than once.
  * aa bb cc dd aaa is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input.
How many passphrases are valid?

Your puzzle answer was 337.


--- Part Two ---

For added security, yet another system policy has been put in place. Now,
a valid passphrase must contain no two words that are anagrams of each
other - that is, a passphrase is invalid if any word's letters can be
rearranged to form any other word in the passphrase.

For example:

  * abcde fghij is a valid passphrase.
  * abcde xyz ecdab is not valid - the letters from the third word can be
    rearranged to form the first word.
  * a ab abc abd abf abj is a valid passphrase, because all letters need
    to be used when forming another word.
  * iiii oiii ooii oooi oooo is valid.
  * oiii ioii iioi iiio is not valid - any of these words can be rearranged
    to form any other word.

Under this new system policy, how many passphrases are valid?

Your puzzle answer was 231.
"""

def number_of_valid_passphrases_without_duplicates(phrases):
    return sum([1 if len(phrase.split()) == len(set(phrase.split())) else 0
                for phrase in phrases])

def number_of_valid_passphrases_without_anagrams(phrases):
    anagram_phrases = [[Counter(word) for word in phrase.split()]
                        for phrase in phrases]

    unique = [[False for i, each in enumerate(anagrams)
                     if each in anagrams[:i]+anagrams[i+1:]]
              for anagrams in anagram_phrases]

    return sum([1 if all(each) else 0 for each in unique])

def main():
    filename = 'day_4_passphrases.txt'
    with open(filename, 'r') as passphrase_file:
        passphrases = passphrase_file.readlines()

    print("Passphrases:", len(passphrases))
    print("Number of valid passphrases (without duplicate words):",
          number_of_valid_passphrases_without_duplicates(passphrases))
    print("Number of valid passphrases (without anagrams):",
          number_of_valid_passphrases_without_anagrams(passphrases))

if __name__ == '__main__':
    main()
