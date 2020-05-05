#!/usr/bin/env python


BLANK_AXIAL_BOARD = [[0, 0, None, None, None],
                     [0, 0, 0, 0, None],
                     [None, 0, 0, 0, 0],
                     [None, None, 0, 0, 0]]

BLANK_AXIAL_BOARD = [[0, 0, None, None, None],
                     [0, 0, 0, 0, None],
                     [None, 0, 0, 0, 0],
                     [None, None, 0, 0, 0]]


class Axial(object):
    def __init__(self, q, r):
        self.q = q
        self.r = r

    def to_cube(self):
        z = -self.q - self.r
        return Cube(self.q, self.r, z)
    
    def to_dict(self):
        return {"q": self.q, "r": self.r}
    
    def __str__(self):
        return str(self.to_dict())


class Cube(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_axial(self):
        return Hex(self.x, self.z)
    
    def to_dict(self):
        return {"x": self.x, "y": self.y, "z": self.z}
    
    def __str__(self):
        return str(self.to_dict())



class Board(object):

