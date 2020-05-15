from .game_object import GameObject

class Planet(GameObject):
    def __init__(self,
                 faction,
                 initial_position=0,
                 rate=1,
                 solar_system=None,
                 board=None):
        super().__init__()
        self.faction = faction
        self.initial_position = initial_position
        self.position = initial_position
        self.rate = rate
        self.board = board
        self.solar_system = solar_system

    def increment_orbit(self, n=1):
        self.position = (self.position + (self.rate * n)) % self.solar_system.size
        return self.position

    def decrement_orbit(self, n=1):
        self.position = (self.solar_system.size + 1 
                            if self.position == 0 
                            else self.position) - (self.rate * n)
        return self.position

    def distance_from(self, target):
        i = (self.position - target) % self.solar_system.size
        j = (target - self.position) % self.solar_system.size
        return min(i, j)

