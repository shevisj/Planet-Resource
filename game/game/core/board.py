#!/usr/bin/env python

from numpy import array, vectorize, where, ndenumerate, int8
from copy import deepcopy
from typing import Type, Counter
from pprint import pformat
from collections import Counter

from .game_object import GameObject
from .coordinates import Axial, Cube
from .resource import Resource
from .planet import Planet


BOARD_DISPLAY = """
     / \ / \ 
    | {} | {} |
   / \ / \ / \ 
  | {} | {} | {} |
 / \ / \ / \ / \ 
| {} | {} | {} | {} |
 \ / \ / \ / \ /
  | {} | {} | {} |
   \ / \ / \ / 
    | {} | {} |
     \ / \ / 
"""

BOARD_DISPLAY_WIDE = """
          /   \   /   \ 
        |   {}   |   {}   |
      /   \   /   \   /   \ 
    |   {}   |   {}   |   {}   |
  /   \   /   \   /   \   /   \ 
|   {}   |   {}   |   {}   |   {}   |
  \   /   \   /   \   /   \   /
    |   {}   |   {}   |   {}   |
      \   /   \   /   \   / 
        |   {}   |   {}   |
          \   /   \   / 
"""

DEFAULT_RESOURCE_ALLOCATION = array([Resource]*14)

# See more about hexagonal grids here: https://www.redblobgames.com/grids/hexagons/

BLANK_AXIAL_BOARD = array([[-1 for _ in range(5)] for _ in range(4)], dtype=int8)
for i, c in ndenumerate(BLANK_AXIAL_BOARD):
    if 1 < (i[0] + i[1]) < 6:
        BLANK_AXIAL_BOARD[i[0]][i[1]] = 0

BLANK_CUBE_BOARD = array([[[-1 for _ in range(5)] for _ in range(7)] for _ in range(4)], dtype=int8)
for i, c in ndenumerate(BLANK_AXIAL_BOARD):
    if c == 0:
        cube = Axial(i[0], i[1]).to_cube()
        BLANK_CUBE_BOARD[cube.x][cube.y][cube.z] = 0

LINEAR_TO_AXIAL_MAP = array([Axial(q, r)
                             for r, row in enumerate(BLANK_AXIAL_BOARD.T)
                             for q, element in enumerate(row)
                             if element == 0], dtype=Axial)

LINEAR_TO_CUBE_MAP = array([axial.to_cube() for axial in LINEAR_TO_AXIAL_MAP], dtype=Cube)

AXIAL_TO_LINEAR_MAP = deepcopy(BLANK_AXIAL_BOARD)
for i, c in enumerate(LINEAR_TO_AXIAL_MAP):
    AXIAL_TO_LINEAR_MAP[c.q][c.r] = i

CUBE_TO_LINEAR_MAP = deepcopy(BLANK_CUBE_BOARD)
for i, c in enumerate(LINEAR_TO_CUBE_MAP):
    CUBE_TO_LINEAR_MAP[c.x][c.y][c.z] = i


class Hex(GameObject):
    def __init__(self, board, index: int, resource_type: Type, unit_capacity=5):
        super().__init__()
        self.board = board
        self.index = index
        if not issubclass(resource_type, Resource):
            raise Exception(f"Invalid resource type: {resource_type}")
        self.resource_type = resource_type
        self.axial = LINEAR_TO_AXIAL_MAP[index]
        self.cube = LINEAR_TO_CUBE_MAP[index]
        self.units = {}
        self.unit_capacity = unit_capacity

    def produce_resource(self, n=1) -> Counter:
        return Counter({self.resource_type: n})

    def add_unit(self, unit) -> bool:
        if len(self.units) >= self.unit_capacity:
            return False
        unit.location = self
        self.units[unit.uuid] = unit
        return True

    def remove_unit(self, unit) -> bool:
        if unit.uuid not in self.units:
            return False
        unit.location = None
        del self.units[unit.uuid]
        return True

    def __str__(self) -> str:
        return str(vars(self))


class Board(GameObject):
    def __init__(self, faction=None, planet=None, resources=DEFAULT_RESOURCE_ALLOCATION):
        super().__init__()
        self.state = array([Hex(self, i, r) for i, r in enumerate(resources)])
        self.planet = planet
        self.faction = faction

    def add_unit(self, unit, index) -> bool:
        return self.state[index].add_unit(unit)

    def remove_unit(self, unit) -> bool:
        index = unit.location.index
        return self.state[index].remove_unit(unit)

    def move_unit(self, unit, destination) -> bool:
        if not self.remove_unit(unit):
            return False
        return self.add_unit(unit, destination)

    def display(self, mode='resources', as_str=False):
        values = []
        for i in self.state:
            if mode == 'resources':
                values.append(i.resource_type.symbol)
            elif mode == 'units':
                values.append(list(i.units.values())[0].symbol if len(i.units) > 0 else ' ')
            else:
                values.append('?')
        output = BOARD_DISPLAY_WIDE.format(*values)
        if as_str:
            return output
        print(output)

    def __str__(self) -> str:
        return pformat({i+1: vars(self.state[i]) for i in range(len(self.state))})
