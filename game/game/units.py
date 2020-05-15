from .core import Unit
from .config import *


class Worker(Unit):
    symbol='W'
    def __init__(self,
                 attack=WORKER_ATTACK,
                 defense=WORKER_DEFENSE,
                 production=WORKER_PRODUCTION,
                 **kwargs):
        super().__init__(attack, defense, **kwargs)
        self.production = production

    def gather_resource(self):
        if self.location is not None:
            return self.location.produce_resource(self.production)


class Combat(Worker):
    symbol='C'
    def __init__(self,
                 attack=COMBAT_ATTACK,
                 defense=COMBAT_DEFENSE,
                 production=COMBAT_PRODUCTION,
                 **kwargs):
        super().__init__(attack, defense, production, **kwargs)

    def battle(self, enemy: Unit):
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


class Hero(Combat):
    symbol='H'
    def __init__(self,
                 attack=HERO_ATTACK,
                 defense=HERO_DEFENSE,
                 production=HERO_PRODUCTION,
                 special_attack=HERO_SPECIAL_ATTACK,
                 **kwargs):
        super().__init__(attack, defense, production, **kwargs)
        self.special_attack = special_attack

    def battle(self, enemy: Unit, use_special_attack=False):
        # Same as Combat.battle() unless use_special_attack is True
        # in which case it uses special_attack as the attack value
        # for this battle
        base_attack = self.attack
        if use_special_attack:
            self.attack = self.special_attack
        outcome = super().battle(enemy)
        self.attack = base_attack
        return outcome
