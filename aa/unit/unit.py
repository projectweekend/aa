from random import randint
from .info import UNIT_INFO


class Unit:

    def __init__(self, name, attack, defense, cost):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.cost = cost

    def __repr__(self):
        return self.name

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


def unit_factory(name):
    return Unit(name=name, **UNIT_INFO[name])
