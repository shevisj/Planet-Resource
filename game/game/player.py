from .core import GameObject
from .resources import Continuum, Food, Gorgonium, Iron, Lithium

class Player(GameObject):
    def __init__(self,
                 name='Player',
                 faction=None,
                 planet=None,
                 board=None,
                 units=[],
                 victory_points=0,
                 resources={}):
        self.name = name
        self.faction = faction
        self.planet = planet
        self.board = board
        self.units = units
        self.victory_points = victory_points
        self.resources = {
            Continuum: 0,
            Food: 0,
            Gorgonium: 0,
            Iron: 0,
            Lithium: 0,
        }
        self.resources.update(resources)
        super().__init__()

    def __str__(self):
        return self.name
