from random import choice

from .core import Board, Faction, GameObject, Planet, SolarSystem
from .config import *


class Zidaan(Faction):
    def __init__(self, player, solar_system: SolarSystem, initial_position=ZIDAAN_INITIAL_POSITION):
        if initial_position < 0:
            initial_position = choice(range(solar_system.size))
        planet_args = {
            'initial_position': initial_position,
            'rate': ZIDAAN_ORBITAL_RATE,
            'solar_system': solar_system
        }
        board_args = {
            'resources': ZIDAAN_RESOURCE_ALLOCATION
        }
        super().__init__(player, planet_args, board_args)
        solar_system.add_planet(self.planet)


class Hianth(Faction):
    def __init__(self, player, solar_system: SolarSystem, initial_position=HIANTH_INITIAL_POSITION):
        if initial_position < 0:
            initial_position = choice(range(solar_system.size))
        planet_args = {
            'initial_position': initial_position,
            'rate': HIANTH_ORBITAL_RATE,
            'solar_system': solar_system
        }
        board_args = {
            'resources': HIANTH_RESOURCE_ALLOCATION
        }
        super().__init__(player, planet_args, board_args)
        solar_system.add_planet(self.planet)


class Gorgon(Faction):
    def __init__(self, player, solar_system: SolarSystem, initial_position=GORGON_INITIAL_POSITION):
        if initial_position < 0:
            initial_position = choice(range(solar_system.size))
        planet_args = {
            'initial_position': initial_position,
            'rate': GORGON_ORBITAL_RATE,
            'solar_system': solar_system
        }
        board_args = {
            'resources': GORGON_RESOURCE_ALLOCATION
        }
        super().__init__(player, planet_args, board_args)
        solar_system.add_planet(self.planet)


class Frent(Faction):
    def __init__(self, player, solar_system: SolarSystem, initial_position=FRENT_INITIAL_POSITION):
        if initial_position < 0:
            initial_position = choice(range(solar_system.size))
        planet_args = {
            'initial_position': initial_position,
            'rate': FRENT_ORBITAL_RATE,
            'solar_system': solar_system
        }
        board_args = {
            'resources': FRENT_RESOURCE_ALLOCATION
        }
        super().__init__(player, planet_args, board_args)
        solar_system.add_planet(self.planet)


class Lithix(Faction):
    def __init__(self, player, solar_system: SolarSystem, initial_position=LITHIX_INITIAL_POSITION):
        if initial_position < 0:
            initial_position = choice(range(solar_system.size))
        planet_args = {
            'initial_position': initial_position,
            'rate': LITHIX_ORBITAL_RATE,
            'solar_system': solar_system
        }
        board_args = {
            'resources': LITHIX_RESOURCE_ALLOCATION
        }
        super().__init__(player, planet_args, board_args)
        solar_system.add_planet(self.planet)


FACTION_LIST = [Zidaan, Hianth, Gorgon, Frent, Lithix]
