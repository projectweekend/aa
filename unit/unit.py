from random import choice, randint


ATTACK = 'attack'
DEFENSE = 'defense'
COST = 'cost'
DIE_VALUES = [1, 2, 3, 4, 5, 6]


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
    units = {
        'infantry': {ATTACK: 1, DEFENSE: 2, COST: 3},
        'artillery': {ATTACK: 2, DEFENSE: 2, COST: 4},
        'mech_infantry': {ATTACK: 1, DEFENSE: 2, COST: 4},
        'tank': {ATTACK: 3, DEFENSE: 3, COST: 6},
        'fighter': {ATTACK: 3, DEFENSE: 4, COST: 10},
        'tactical_bomber': {ATTACK: 3, DEFENSE: 3, COST: 11},
        'bomber': {ATTACK: 4, DEFENSE: 1, COST: 12}
    }
    return Unit(name=name, **units[name])
