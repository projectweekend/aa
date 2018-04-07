from random import randint
from .info import *


ATTACK = 'attack'
DEFENSE = 'defense'
COST = 'cost'

UNITS = {
    INFANTRY: {ATTACK: 1, DEFENSE: 2, COST: 3},
    ARTILLERY: {ATTACK: 2, DEFENSE: 2, COST: 4},
    MECHANIZED_INFANTRY: {ATTACK: 1, DEFENSE: 2, COST: 4},
    TANK: {ATTACK: 3, DEFENSE: 3, COST: 6},
    FIGHTER: {ATTACK: 3, DEFENSE: 4, COST: 10},
    TACTICAL_BOMBER: {ATTACK: 3, DEFENSE: 3, COST: 11},
    STRATEGIC_BOMBER: {ATTACK: 4, DEFENSE: 1, COST: 12},
    AIRCRAFT_CARRIER: {ATTACK: 0, DEFENSE: 2, COST: 16},
    BATTLESHIP: {ATTACK: 4, DEFENSE: 4, COST: 20},
    DESTROYER: {ATTACK: 2, DEFENSE: 2, COST: 8},
    CRUISER: {ATTACK: 3, DEFENSE: 3, COST: 12},
    SUBMARINE: {ATTACK: 2, DEFENSE: 1, COST: 6}
}


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
    return Unit(name=name, **UNITS[name])
