from game.core import Planet, SolarSystem
from unittest import TestCase

class SolarSystemTest(TestCase):
    def setUp(self):
        self.planet_names = ['a', 'b', 'c', 'd', 'e', 'f']
        self.solar_system = SolarSystem()
        for i, n in enumerate(self.planet_names):
            self.solar_system.create_planet(n, rate=i+1)
        print(self.solar_system.planets)

    def tearDown(self):
        for i, n in enumerate(self.planet_names):
            self.solar_system.remove_planet(n)

    def test_increment_orbits_adds_rate_to_positions(self):
        self.solar_system.increment_orbits()
        expected = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
        }
        self.assertDictEqual(expected, self.solar_system.orbital_state())


