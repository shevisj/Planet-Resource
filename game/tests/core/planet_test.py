from game.core.planet import Planet
from game.core.solar_system import SolarSystem
from unittest import TestCase

class PlanetTest(TestCase):
    def setUp(self):
        self.planet = Planet('Mars', rate=5, solar_system=SolarSystem(size=12))

    def test_increment_orbit_adds_rate_to_position(self):
        self.planet.increment_orbit()
        self.assertEqual(self.planet.position, 5)
