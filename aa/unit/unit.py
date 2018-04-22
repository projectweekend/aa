from random import randint
from .info import UNIT_INFO


class Unit:

    def __init__(self, name, attack, defense, cost, movement, type, bonus):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.cost = cost
        self.movement = movement
        self.type = type
        self.bonus = bonus

    def __repr__(self):
        return self.name

    @property
    def attack_rank(self):
        return self.attack + self.cost + self.bonus_rank

    @property
    def defense_rank(self):
        return self.defense + self.cost + self.bonus_rank

    @property
    def bonus_rank(self):
        return 1.5 if self.bonus else 0

    def roll(self):
        return randint(1, 6)

    def roll_attack(self):
        roll = self.roll()
        if roll <= self.attack:
            return roll, 1
        return roll, 0

    def roll_defense(self):
        roll = self.roll()
        if roll <= self.defense:
            return roll, 1
        return roll, 0

    def apply_bonus(self, bonus_cfg):
        for attr, val in bonus_cfg.items():
            if getattr(self, attr) != val:
                setattr(self, attr, val)


def unit_factory(name):
    name = name.title()
    return Unit(**UNIT_INFO[name])
