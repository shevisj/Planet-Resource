from game.config import COMBAT_ATTACK, COMBAT_DEFENSE

from .base_unit import BaseUnit

class Combat(BaseUnit):
    def __init__(self, attack=COMBAT_ATTACK, defense=COMBAT_DEFENSE):
        super().__init__(attack, defense)
