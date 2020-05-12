from ..core import CoreObject

class BaseUnit(CoreObject):
    def __init__(self, attack, defense):
        super().__init__()
        self.attack = attack
        self.defense = defense

    def battle(self, enemy: CoreObject):
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
