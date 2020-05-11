from numpy import ndarray

class Axial(object):
    def __init__(self, q, r):
        self.q = q
        self.r = r

    def to_cube(self):
        y = -self.q - self.r
        return Cube(self.q, y, self.r)
    
    def to_dict(self) -> dict:
        return self.__dict__
    
    def to_tuple(self) -> tuple:
        return (self.q, self.r)
    
    def __str__(self) -> str:
        return str(self.to_tuple())


class Cube(object):
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.__dict__ = vars(self)

    def to_axial(self):
        return Axial(self.x, self.z)

    def to_tuple(self) -> tuple:
        return (self.x, self.y, self.z)
    
    def __str__(self) -> str:
        return str(tuple(self))

    def __iter__(self) -> int:
        for k, v in self.__dict__.items():
            yield k, v
