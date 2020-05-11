#!/usr/bin/env python

from numpy import array, vectorize, where, ndenumerate, int8
from copy import deepcopy

from . import Axial, Cube

BLANK_LINEAR_BOARD = array([0]*14)

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


class Board(object):
    def __init__(self, coordinates_type=Axial, state=BLANK_AXIAL_BOARD):
        self.coordinates_type = coordinates_type
        self.state = state


