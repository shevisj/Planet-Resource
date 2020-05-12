from .object import CoreObject


class Axial(CoreObject):
    def __init__(self, q: int, r: int):
        super().__init__()
        self.q = q
        self.r = r
        self.__dict__ = {
            'q': self.q,
            'r': self.r,
        }

    def to_cube(self):
        y = -self.q - self.r
        return Cube(self.q, y, self.r)
    
    def to_tuple(self) -> tuple:
        return (self.q, self.r)
    
    def __str__(self) -> str:
        return str(self.to_tuple())

    def __iter__(self) -> int:
        for k, v in self.__dict__.items():
            yield k, v


class Cube(CoreObject):
    def __init__(self, x: int, y: int, z: int):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.__dict__ = {
            'x': self.x,
            'y': self.y,
            'z': self.z,
        }

    def to_axial(self):
        return Axial(self.x, self.z)

    def to_tuple(self) -> tuple:
        return (self.x, self.y, self.z)
    
    def __str__(self) -> str:
        return str(tuple(self))

    def __iter__(self) -> int:
        for k, v in self.__dict__.items():
            yield k, v
