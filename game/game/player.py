from collections import Counter
from typing import Type

from .core import GameObject, Unit, Hex
from .resources import Continuum, Food, Gorgonium, Iron, Lithium

class Player(GameObject):
    def __init__(self,
                 faction=None,
                 planet=None,
                 board=None,
                 units={},
                 resources={},
                 victory_points=0,
                 name=None):
        super().__init__()
        self.faction = faction
        self.planet = planet
        self.board = board
        self.units = units
        self.victory_points = victory_points
        self.resources = Counter({
            Continuum: 0,
            Food: 0,
            Gorgonium: 0,
            Iron: 0,
            Lithium: 0,
        })
        self.resources += Counter(resources)
        self.name = name or str(faction)

    def __str__(self):
        return self.name

    def add_unit(self, unit: Unit, location):
        self.units[unit.uuid] = unit
        if isinstance(location, Hex):
            return location.board.add_unit(unit, location.index)
        elif isinstance(location, int):
            return self.board.add_unit(unit, location)
        else:
            raise Exception(f"Invalid location: {location}")

    def create_unit(self, unit_type: Type, location, **unit_args):
        if not issubclass(unit_type, Unit):
            raise Exception(f"Invalid unit type: {unit_type}")
        unit = unit_type(**unit_args)
        return self.add_unit(unit, location)

    def destroy_unit(self, unit: Unit):
        if unit.uuid in self.units:
            del self.units[unit.uuid]
        if not unit.location.board.remove_unit(unit):
            raise Exception(f"Failed to destroy unit: {unit}")

    def gather_resources(self):
        for u in self.units.values():
            self.resources += u.gather_resource()
