# This represents the highest level abstraction of this program.
from .core import GameObject, Planet, Player, SolarSystem
from .config import SOLAR_SYSTEM_SIZE
from .factions import FACTION_LIST

class GameState(GameObject):
    def __init__(self, n_players=5):
        super().__init__()
        self.global_parameters = {
            'super_computers_active': 0,
            'ethereal_beacons_lit': 0
        }
        self.solar_system = SolarSystem(size=SOLAR_SYSTEM_SIZE)
        self.players = {}
        for i in range(n_players):
            player = Player()
            faction = FACTION_LIST[i](player, self.solar_system)
            player.faction = faction
            self.players[str(faction)] = player

