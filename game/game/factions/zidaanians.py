from ..core import Board, CoreObject, Planet
from ..config import ZIDAAN_ORBITAL_RATE, ZIDAAN_BOARD

class Zidaanians(CoreObject):
    def __init__(self, initial_position=0, solar_system=None):
        super.__init__()
        self.board = Board(state=ZIDAAN_BOARD)
        self.planet = Planet('Zidaan', 
                             initial_position=initial_position,
                             rate=ZIDAAN_ORBITAL_RATE,
                             solar_system=solar_system)
        