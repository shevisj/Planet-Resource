class Axial(object):
    def __init__(self, q, r):
        self.q = q
        self.r = r

    def to_cube(self):
        y = -self.q - self.r
        return Cube(self.q, y, self.r)
    
    def to_dict(self):
        return {"q": self.q, "r": self.r}
    
    def to_tuple(self):
        return (self.q, self.r)
    
    def __str__(self):
        return str(self.to_tuple())


class Cube(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_axial(self):
        return Hex(self.x, self.z)
    
    def to_dict(self):
        return {"x": self.x, "y": self.y, "z": self.z}
    
    def to_tuple(self):
        return (self.x, self.y, self.z)
    
    def __str__(self):
        return str(self.to_tuple())
