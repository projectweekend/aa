from collections import Counter
from aa.unit import Army
from .battle import Battle, LandBattle
from .utils import battle_factory


new_battle = battle_factory(army_cls=Army, battle_cls=Battle)
new_land_battle = battle_factory(army_cls=Army, battle_cls=LandBattle)


def simulate_battles(battle_config, count, factory):
    results = Counter()
    for _ in range(count):
        b = factory(config=battle_config)
        b.simulate()
        results[b.winner] += 1
    labels = ('attacker', 'defender', 'draw')
    return {label: (results[label] / count) * 100 for label in labels}


def simulate(battle_config, count):
    return simulate_battles(battle_config, count, new_battle)


def simulate_land_battle(battle_config, count):
    return simulate_battles(battle_config, count, new_land_battle)
