from .core import Unit
from .config import COMBAT_ATTACK, COMBAT_DEFENSE
from .config import WORKER_ATTACK, WORKER_DEFENSE


class Combat(Unit):
    def __init__(self, attack=COMBAT_ATTACK, defense=COMBAT_DEFENSE):
        super().__init__(attack, defense)


class Worker(Unit):
    def __init__(self, attack=WORKER_ATTACK, defense=WORKER_DEFENSE):
        super().__init__(attack, defense)
