# This represents the highest level abstraction of this program.
from .object import CoreObject

class Game(CoreObject):
    def __init__(self):
        super().__init__()
        self.global_parameters = {
            'super_computers_active': 0,
            'ethereal_beacons_lit': 0
        }
