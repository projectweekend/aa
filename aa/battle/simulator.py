from collections import Counter
from copy import copy
from .battle import Battle


def simulate(attackers, defenders, count):
    results = Counter()
    for _ in range(count):
        b = Battle(attackers=copy(attackers), defenders=copy(defenders))
        b.simulate()
        results[b.winner] += 1
    labels = ('attacker', 'defender', 'draw')
    return {label: (results[label] / count) * 100 for label in labels}