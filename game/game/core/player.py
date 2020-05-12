from .object import CoreObject
from .planet import Planet

class Player(CoreObject):
    def __init__(self,
                 name='Player',
                 faction=None,
                 planet=None):
        super().__init__()
        self.resources = {
            'carbon': 0,
            'hydrogen': 0,
            'iron': 0,
            'gorgonium': 0,
            'lithium': 0,
            'continuum': 0,
        }
        self.name = name
        self.faction = faction
        self.planet = planet
