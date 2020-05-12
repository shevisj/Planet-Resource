from game.core.planet import Planet
from game.core.solar_system import SolarSystem
from unittest import TestCase

class SolarSystemTest(TestCase):
    def setUp(self):
        self.planet_names = ['a', 'b', 'c', 'd', 'e', 'f']
        self.solar_system = SolarSystem(size=12)
        for i, n in enumerate(self.planet_names):
            self.solar_system.add_planet(Planet(n, rate=i+1))

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
        print(self.solar_system.increment_orbits(100))


