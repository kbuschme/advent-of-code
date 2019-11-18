import unittest
from collections import namedtuple
from day_15 import parse_cave_string, fight, find_minimum_elf_attack_power

class TestBeverageBandits(unittest.TestCase):
    """Test Beverage Bandits."""

    def test_fight(self):
        Test = namedtuple('Test', ['cave', 'rounds', 'hitpoints'])
        tests = [
            Test(rounds=47,
                 hitpoints=590,
                 cave=("#######\n"
                       "#.G...#\n"
                       "#...EG#\n"
                       "#.#.#G#\n"
                       "#..G#E#\n"
                       "#.....#\n"
                       "#######")),
            Test(rounds=37,
                 hitpoints=982,
                 cave=("#######\n"
                       "#G..#E#\n"
                       "#E#E.E#\n"
                       "#G.##.#\n"
                       "#...#E#\n"
                       "#...E.#\n"
                       "#######")),
            Test(rounds=46,
                 hitpoints=859,
                 cave=("#######\n"
                       "#E..EG#\n"
                       "#.#G.E#\n"
                       "#E.##E#\n"
                       "#G..#.#\n"
                       "#..E#.#\n"
                       "#######")),
            Test(rounds=35,
                 hitpoints=793,
                 cave=("#######\n"
                       "#E.G#.#\n"
                       "#.#G..#\n"
                       "#G.#.G#\n"
                       "#G..#.#\n"
                       "#...E.#\n"
                       "#######")),
            Test(rounds=54,
                 hitpoints=536,
                 cave=("#######\n"
                       "#.E...#\n"
                       "#.#..G#\n"
                       "#.###.#\n"
                       "#E#G#G#\n"
                       "#...#G#\n"
                       "#######")),
            Test(rounds=20,
                 hitpoints=937,
                 cave=("#########\n"
                       "#G......#\n"
                       "#.E.#...#\n"
                       "#..##..G#\n"
                       "#...##..#\n"
                       "#...#...#\n"
                       "#.G...G.#\n"
                       "#.....G.#\n"
                       "#########"))
        ]
        for test in tests:
            cave, units = parse_cave_string(test.cave)
            result_rounds, result_hitpoints, _ = fight(cave, units)
            self.assertEqual(result_rounds, test.rounds)
            self.assertEqual(result_hitpoints, test.hitpoints)

    def test_find_minimum_elf_attack_power(self):
        Test = namedtuple(
            'Test', ['cave', 'rounds', 'elf_attack_power', 'hitpoints'])
        tests = [
            Test(rounds=29,
                 hitpoints=172,
                 elf_attack_power=15,
                 cave=("#######\n"
                       "#.G...#\n"
                       "#...EG#\n"
                       "#.#.#G#\n"
                       "#..G#E#\n"
                       "#.....#\n"
                       "#######")),
            Test(rounds=33,
                 hitpoints=948,
                 elf_attack_power=4,
                 cave=("#######\n"
                       "#E..EG#\n"
                       "#.#G.E#\n"
                       "#E.##E#\n"
                       "#G..#.#\n"
                       "#..E#.#\n"
                       "#######")),
            Test(rounds=37,
                 hitpoints=94,
                 elf_attack_power=15,
                 cave=("#######\n"
                       "#E.G#.#\n"
                       "#.#G..#\n"
                       "#G.#.G#\n"
                       "#G..#.#\n"
                       "#...E.#\n"
                       "#######")),
            Test(rounds=39,
                 hitpoints=166,
                 elf_attack_power=12,
                 cave=("#######\n"
                       "#.E...#\n"
                       "#.#..G#\n"
                       "#.###.#\n"
                       "#E#G#G#\n"
                       "#...#G#\n"
                       "#######")),
            Test(rounds=30,
                 hitpoints=38,
                 elf_attack_power=34,
                 cave=("#########\n"
                       "#G......#\n"
                       "#.E.#...#\n"
                       "#..##..G#\n"
                       "#...##..#\n"
                       "#...#...#\n"
                       "#.G...G.#\n"
                       "#.....G.#\n"
                       "#########"))
        ]
        for test in tests:
            cave, units = parse_cave_string(test.cave)
            (result_rounds,
             result_hitpoints,
             result_attack_power) = find_minimum_elf_attack_power(cave, units)
            self.assertEqual(result_rounds, test.rounds)
            self.assertEqual(result_hitpoints, test.hitpoints)
            self.assertEqual(result_attack_power, test.elf_attack_power)

if __name__ == '__main__':
    unittest.main()
