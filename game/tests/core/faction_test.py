from game.core import Faction
from unittest import TestCase

class PlanetTest(TestCase):
    def setUp(self):
        self.faction = Faction('Zidaan', )

    def tearDown(self):
        self.solar_system.remove_planet(self.planet.uuid)

    def test_increment_orbit_adds_rate_to_position(self):
        self.planet.increment_orbit()
        self.assertEqual(self.planet.position, 5)
