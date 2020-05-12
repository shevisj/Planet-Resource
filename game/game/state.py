# This represents the highest level abstraction of this program.
from .core.object import CoreObject

class GameState(CoreObject):
    def __init__(self):
        super().__init__()
        self.global_parameters = {
            'super_computers_active': 0,
            'ethereal_beacons_lit': 0
        }

