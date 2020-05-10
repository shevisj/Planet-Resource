#!/usr/bin/env python

from numpy import array

from . import Axial, Cube

BLANK_LINEAR_BOARD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

BLANK_AXIAL_BOARD = array([[None, None, 0, 0, 0],
                           [None, 0, 0, 0, 0],
                           [0, 0, 0, 0, None],
                           [0, 0, 0, None, None]])

BLANK_CUBE_BOARD = array([[[None, None, None, None, None],
                           [None, None, None, None, None],
                           [None, None, None, None, None],
                           [None, None, None, None, 0],
                           [None, None, None, 0, None],
                           [None, None, 0, None, None],
                           [None, None, None, None, None]],
                           [[None, None, None, None, None],
                           [None, None, None, None, None],
                           [None, None, None, None, 0],
                           [None, None, None, 0, None],
                           [None, None, 0, None, None],
                           [None, 0, None, None, None],
                           [None, None, None, None, None]],
                           [[None, None, None, None, None],
                           [None, None, None, None, None],
                           [None, None, None, 0, None],
                           [None, None, 0, None, None],
                           [None, 0, None, None, None],
                           [0, None, None, None, None],
                           [None, None, None, None, None]],
                           [[None, None, None, None, None],
                           [None, None, None, None, None],
                           [None, None, 0, None, None],
                           [None, 0, None, None, None],
                           [0, None, None, None, None],
                           [None, None, None, None, None],
                           [None, None, None, None, None]]])


LINEAR_TO_AXIAL_MAP = array([Axial(q, r)
                             for r, row in enumerate(BLANK_AXIAL_BOARD.T)
                             for q, element in enumerate(row)
                             if element is not None])

LINEAR_TO_CUBE_MAP = [axial.to_cube() for axial in LINEAR_TO_AXIAL_MAP]


class Board(object):
    def __init__(self, coordinates_type=Axial, state=BLANK_AXIAL_BOARD):
        self.coordinates_type = coordinates_type
        self.state = state


