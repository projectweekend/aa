from random import randint
from .info import *


class Bonus:

    def __init__(self, targets, boosted_attribute, boost_value):
        self.targets = targets
        self.boosted_attribute = boosted_attribute
        self.boost_value = boost_value


class Roll:

    def __init__(self, unit):
        self._unit = unit

    def _roll(self):
        return randint(1, 6)

    def attack(self):
        roll = self._roll()
        if roll <= self._unit.attack:
            return roll, 1
        return roll, 0

    def defense(self):
        roll = self._roll()
        if roll <= self._unit.defense:
            return roll, 1
        return roll, 0


class Rank:

    def __init__(self, unit):
        self._unit = unit

    @property
    def attack(self):
        return self._unit.attack + self._unit.cost + self.bonus

    @property
    def defense(self):
        return self._unit.defense + self._unit.cost + self.bonus

    @property
    def bonus(self):
        return 1.5 if self._unit.bonuses_granted else 0


class Unit:

    def __init__(self, name, attack, defense, cost, movement, type,
                 bonuses_granted, active_bonus=None):
        self.name = name
        self._attack = attack
        self._defense = defense
        self.cost = cost
        self.movement = movement
        self.type = type
        self.bonuses_granted = bonuses_granted
        self.active_bonus = active_bonus
        self.roll = Roll(unit=self)
        self.rank = Rank(unit=self)

    def __repr__(self):
        return self.name

    @classmethod
    def build_by_name(cls, name):
        unit_args = UNIT_INFO[name.title()]
        kwargs = dict(unit_args)
        kwargs[BONUSES] = [Bonus(**e) for e in unit_args[BONUSES]]
        return cls(**kwargs)

    @property
    def attack(self):
        if self.active_bonus is None:
            return self._attack
        if self.active_bonus.boosted_attribute != ATTACK:
            return self._attack
        return self.active_bonus.boost_value

    @property
    def defense(self):
        if self.active_bonus is None:
            return self._defense
        if self.active_bonus.boosted_attribute != DEFENSE:
            return self._defense
        return self.active_bonus.boost_value
