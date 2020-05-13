from .game_object import GameObject
from .board import Board, Hex
from .planet import Planet

class Unit(GameObject):
    def __init__(self, attack, defense, location = {}):
        self.attack = attack
        self.defense = defense
        self.location = {
            Hex: None,
            Board: None,
            Planet: None,
        }
        super().__init__()

    def battle(self, enemy: GameObject):
        if self.attack >= enemy.defense and self.defense > enemy.attack:
            # Victory: enemy died, I survived
            return 1
        elif self.attack >= enemy.defense and self.defense <= enemy.attack:
            # Mutual Destruction: we both died
            return 0
        elif self.attack < enemy.defense and self.defense <= enemy.attack:
            # Defeat: enemy survived, I died
            return -1
        else:
            # No contest: we both survived
            return None
