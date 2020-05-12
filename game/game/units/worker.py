from game.config import WORKER_ATTACK, WORKER_DEFENSE

from .base_unit import BaseUnit

class Worker(BaseUnit):
    def __init__(self, attack=WORKER_ATTACK, defense=WORKER_DEFENSE):
        super().__init__(attack, defense)
