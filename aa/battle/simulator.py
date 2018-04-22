from collections import Counter
from copy import copy
from aa.unit import Army
from .utils import battle_factory


new_battle = battle_factory(army=Army)


def simulate(battle_config, count):
    results = Counter()
    for _ in range(count):
        b = new_battle(config=battle_config)
        b.simulate()
        results[b.winner] += 1
    labels = ('attacker', 'defender', 'draw')
    return {label: (results[label] / count) * 100 for label in labels}
