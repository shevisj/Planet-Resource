# This represents the highest level abstraction of this program.
from .core import GameObject, Planet, SolarSystem
from .config import SOLAR_SYSTEM_SIZE
from .factions import FACTION_LIST
from .player import Player

class GameState(GameObject):
    def __init__(self, n_players=5):
        self.global_parameters = {
            'super_computers_active': 0,
            'ethereal_beacons_lit': 0
        }
        self.solar_system = SolarSystem(size=SOLAR_SYSTEM_SIZE)
        self.players = {}
        self.factions = {}
        for i in range(n_players):
            player = Player(name=f'Player {i+1}')
            faction = FACTION_LIST[i](player, self.solar_system)
            self.players[str(faction)] = player
            self.factions[str(player)] = faction
        super().__init__()

