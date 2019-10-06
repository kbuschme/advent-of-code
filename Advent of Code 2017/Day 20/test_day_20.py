import unittest
from collections import namedtuple
from day_20 import find_closest_particle, count_remaining_particles

class TestCalculateParticlePosition(unittest.TestCase):
    """Test calculate particle position."""

    def test_find_closest_particle(self):
        Test = namedtuple('Test', ['particles', 'expected'])
        tests = [Test(particles=["p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>",
                                 "p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>"],
                      expected=0)]

        for test in tests:
            result = find_closest_particle(test.particles)
            self.assertEqual(result, test.expected)

    def test_find_remaining_particles(self):
        Test = namedtuple('Test', ['particles', 'expected'])
        tests = [Test(particles=["p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>",
                                 "p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>",
                                 "p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>",
                                 "p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"],
                      expected=1)]

        for test in tests:
            result = count_remaining_particles(test.particles)
            self.assertEqual(result, test.expected)

if __name__ == '__main__':
    unittest.main()
