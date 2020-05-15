from .game_object import GameObject


class Unit(GameObject):
    symbol='U'
    def __init__(self,
                 attack: int,
                 defense: int,
                 location=None):
        super().__init__()
        self.attack = attack
        self.defense = defense
        self.location = location
