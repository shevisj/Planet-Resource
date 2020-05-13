#!/usr/bin/env python

from numpy import array, vectorize, where, ndenumerate, int8
from copy import deepcopy
from typing import Dict, Type
from pprint import pformat

from .game_object import GameObject
from .coordinates import Axial, Cube
from .resource import Resource
from .planet import Planet

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
    def __init__(self, board, linear_position: int, resource_type: Type, unit_capacity=5):
        self.board = board
        self.linear_position = linear_position
        self.resource_type = resource_type
        self.axial = LINEAR_TO_AXIAL_MAP[linear_position]
        self.cube = LINEAR_TO_CUBE_MAP[linear_position]
        self.units = {}
        self.unit_capacity = unit_capacity
        super().__init__()

    def produce_resource(self, n=1) -> Dict:
        return {self.resource_type: n}

    def add_unit(self, unit):
        if len(self.units) >= self.unit_capacity:
            return False
        unit.location.update({
            Hex: self,
            Board: self.board,
            Planet: self.board.planet
        })
        self.units[unit.uuid] = unit
        return True

    def remove_unit(self, unit):
        if unit.uuid not in self.units:
            return False
        unit.location.update({
            Hex: None,
            Board: None,
            Planet: None
        })
        del self.units[unit.uuid]
        return True

    def __str__(self):
        return str(vars(self))


class Board(GameObject):
    def __init__(self, faction=None, planet=None, resources=DEFAULT_RESOURCE_ALLOCATION):
        self.state = array([Hex(self, i, r) for i, r in enumerate(DEFAULT_RESOURCE_ALLOCATION)])
        self.planet = planet
        self.faction = faction
        super().__init__()

    def add_unit(self, unit, linear_position):
        return self.state[linear_position].add_unit(unit)

    def remove_unit(self, unit):
        linear_position = unit.location[Hex].linear_position
        return self.state[linear_position].remove_unit(unit)

    def move_unit(self, unit, destination):
        if not self.remove_unit(unit):
            return False
        return self.add_unit(unit, destination)

    def __str__(self):
        return pformat({i+1: vars(self.state[i]) for i in range(len(self.state))})

