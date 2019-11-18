import unittest
from collections import namedtuple
from day_24 import parse_system_description, immune_response
from day_24 import boost_immune_system

class TestImmuneSystem(unittest.TestCase):
    """Test Immune System"""

    def test_parse_system_description(self):
        Test = namedtuple('Test', ['system_description', 'expected'])
        tests = [
            Test(system_description="""Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4""",
            expected=[
                {'team': 'Immune System',
                 'units': 17,
                 'hit_points': 5390,
                 'weaknesses': ['radiation', 'bludgeoning'],
                 'immunities': [],
                 'attack': 4507,
                 'attack_type': 'fire',
                 'initiative': 2},
                {'team': 'Immune System',
                 'units': 989,
                 'hit_points': 1274,
                 'immunities': ['fire'],
                 'weaknesses': ['bludgeoning', 'slashing'],
                 'attack': 25,
                 'attack_type': 'slashing',
                 'initiative': 3},
                {'team': 'Infection',
                 'units': 801,
                 'hit_points': 4706,
                 'immunities': [],
                 'weaknesses': ['radiation'],
                 'attack': 116,
                 'attack_type': 'bludgeoning',
                 'initiative': 1},
                {'team': 'Infection',
                 'units': 4485,
                 'hit_points': 2961,
                 'immunities': ['radiation'],
                 'weaknesses': ['fire', 'cold'],
                 'attack': 12,
                 'attack_type': 'slashing',
                 'initiative': 4}
            ])
        ]
        for test in tests:
            result = parse_system_description(test.system_description)
            self.assertEqual(result, test.expected)

    def test_immune_response(self):
        Test = namedtuple('Test', ['groups', 'expected'])
        tests = [
            Test(groups=[
                {'team': 'Immune System',
                 'units': 17,
                 'hit_points': 5390,
                 'weaknesses': ['radiation', 'bludgeoning'],
                 'immunities': [],
                 'attack': 4507,
                 'attack_type': 'fire',
                 'initiative': 2},
                {'team': 'Immune System',
                 'units': 989,
                 'hit_points': 1274,
                 'immunities': ['fire'],
                 'weaknesses': ['bludgeoning', 'slashing'],
                 'attack': 25,
                 'attack_type': 'slashing',
                 'initiative': 3},
                {'team': 'Infection',
                 'units': 801,
                 'hit_points': 4706,
                 'immunities': [],
                 'weaknesses': ['radiation'],
                 'attack': 116,
                 'attack_type': 'bludgeoning',
                 'initiative': 1},
                {'team': 'Infection',
                 'units': 4485,
                 'hit_points': 2961,
                 'immunities': ['radiation'],
                 'weaknesses': ['fire', 'cold'],
                 'attack': 12,
                 'attack_type': 'slashing',
                 'initiative': 4}
            ],
            expected=('Infection', 5216))]

        for test in tests:
            result = immune_response(test.groups)
            self.assertEqual(result, test.expected)

    def test_boost_immune_system(self):
        Test = namedtuple('Test', ['groups', 'boost', 'expected'])
        tests = [
            Test(groups=[
                {'team': 'Immune System',
                 'units': 17,
                 'hit_points': 5390,
                 'weaknesses': ['radiation', 'bludgeoning'],
                 'immunities': [],
                 'attack': 4507,
                 'attack_type': 'fire',
                 'initiative': 2},
                {'team': 'Immune System',
                 'units': 989,
                 'hit_points': 1274,
                 'immunities': ['fire'],
                 'weaknesses': ['bludgeoning', 'slashing'],
                 'attack': 25,
                 'attack_type': 'slashing',
                 'initiative': 3},
                {'team': 'Infection',
                 'units': 801,
                 'hit_points': 4706,
                 'immunities': [],
                 'weaknesses': ['radiation'],
                 'attack': 116,
                 'attack_type': 'bludgeoning',
                 'initiative': 1},
                {'team': 'Infection',
                 'units': 4485,
                 'hit_points': 2961,
                 'immunities': ['radiation'],
                 'weaknesses': ['fire', 'cold'],
                 'attack': 12,
                 'attack_type': 'slashing',
                 'initiative': 4}
            ],
            boost=1570,
            expected=[
                {'team': 'Immune System',
                 'units': 17,
                 'hit_points': 5390,
                 'weaknesses': ['radiation', 'bludgeoning'],
                 'immunities': [],
                 'attack': 6077,
                 'attack_type': 'fire',
                 'initiative': 2},
                {'team': 'Immune System',
                 'units': 989,
                 'hit_points': 1274,
                 'immunities': ['fire'],
                 'weaknesses': ['bludgeoning', 'slashing'],
                 'attack': 1595,
                 'attack_type': 'slashing',
                 'initiative': 3},
                {'team': 'Infection',
                 'units': 801,
                 'hit_points': 4706,
                 'immunities': [],
                 'weaknesses': ['radiation'],
                 'attack': 116,
                 'attack_type': 'bludgeoning',
                 'initiative': 1},
                {'team': 'Infection',
                 'units': 4485,
                 'hit_points': 2961,
                 'immunities': ['radiation'],
                 'weaknesses': ['fire', 'cold'],
                 'attack': 12,
                 'attack_type': 'slashing',
                 'initiative': 4}])
        ]
        for test in tests:
            result = boost_immune_system(test.groups, boost=test.boost)
            self.assertEqual(result, test.expected)

    def test_immune_response_with_boost(self):
        Test = namedtuple('Test', ['groups', 'boost', 'expected'])
        tests = [
            Test(groups=[
                {'team': 'Immune System',
                 'units': 17,
                 'hit_points': 5390,
                 'weaknesses': ['radiation', 'bludgeoning'],
                 'immunities': [],
                 'attack': 4507,
                 'attack_type': 'fire',
                 'initiative': 2},
                {'team': 'Immune System',
                 'units': 989,
                 'hit_points': 1274,
                 'immunities': ['fire'],
                 'weaknesses': ['bludgeoning', 'slashing'],
                 'attack': 25,
                 'attack_type': 'slashing',
                 'initiative': 3},
                {'team': 'Infection',
                 'units': 801,
                 'hit_points': 4706,
                 'immunities': [],
                 'weaknesses': ['radiation'],
                 'attack': 116,
                 'attack_type': 'bludgeoning',
                 'initiative': 1},
                {'team': 'Infection',
                 'units': 4485,
                 'hit_points': 2961,
                 'immunities': ['radiation'],
                 'weaknesses': ['fire', 'cold'],
                 'attack': 12,
                 'attack_type': 'slashing',
                 'initiative': 4}
            ],
            boost=1570,
            expected=('Immune System', 51))]

        for test in tests:
            result = immune_response(boost_immune_system(
                test.groups, test.boost))
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
