import unittest
from collections import namedtuple
from day_18 import execute_sound_card_code, run_concurrently

class TestSoundCard(unittest.TestCase):
    """Test sound card emulation."""

    def test_execute_sound_card_code(self):
        Test = namedtuple('Test', ['code', 'expected'])
        tests = [Test(expected=4, code="""set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""")]

        for test in tests:
            result = execute_sound_card_code(test.code)
            self.assertEqual(result, test.expected)

    def test_run_concurrently(self):
        Test = namedtuple('Test', ['code', 'expected'])
        tests = [Test(expected=3, code="""snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d""")]

        for test in tests:
            result = run_concurrently(test.code)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
