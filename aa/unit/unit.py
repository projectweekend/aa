from random import randint
from .info import *


class Bonus:

    def __init__(self, targets, boosted_attribute, boost_value):
        self.targets = targets
        self.boosted_attribute = boosted_attribute
        self.boost_value = boost_value


class Unit:

    def __init__(self, name, attack, defense, cost, movement, type,
                 bonuses_granted, active_bonus=None):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.cost = cost
        self.movement = movement
        self.type = type
        self.bonuses_granted = bonuses_granted
        self.active_bonus = active_bonus

    def __repr__(self):
        return self.name

    @classmethod
    def build_by_name(cls, name):
        unit_args = UNIT_INFO[name.title()]
        kwargs = dict(unit_args)
        kwargs[BONUSES] = [Bonus(**e) for e in unit_args[BONUSES]]
        return cls(**kwargs)

    @property
    def attack_rank(self):
        return self.attack + self.cost + self.bonus_rank

    @property
    def defense_rank(self):
        return self.defense + self.cost + self.bonus_rank

    @property
    def bonus_rank(self):
        return 1.5 if self.bonuses_granted else 0

    @property
    def attack_with_bonus(self):
        if self.active_bonus is None:
            return self.attack
        if self.active_bonus.boosted_attribute != ATTACK:
            return self.attack
        return self.active_bonus.boost_value

    @property
    def defense_with_bonus(self):
        if self.active_bonus is None:
            return self.defense
        if self.active_bonus.boosted_attribute != DEFENSE:
            return self.defense
        return self.active_bonus.boost_value

    def roll(self):
        return randint(1, 6)

    def roll_attack(self):
        roll = self.roll()
        if roll <= self.attack_with_bonus:
            return roll, 1
        return roll, 0

    def roll_defense(self):
        roll = self.roll()
        if roll <= self.defense_with_bonus:
            return roll, 1
        return roll, 0
