from collections import Counter
import pandas as pd
from aa.unit import Army
from .battle import Battle, LandBattle
from .utils import battle_factory


new_battle = battle_factory(army_cls=Army, battle_cls=Battle)
new_land_battle = battle_factory(army_cls=Army, battle_cls=LandBattle)


def simulate_battles(battle_config, count, factory):
    wins = []
    attackers_remaining = []
    defenders_remaining = []
    winner_counts = Counter()
    for _ in range(count):
        b = factory(config=battle_config)
        b.simulate()
        if b.winner == 'attacker':
            attackers_remaining.append(b.attackers.unit_summary())
        if b.winner == 'defender':
            defenders_remaining.append(b.defenders.unit_summary())
        wins.append(b.winner)
    win_summary = pd.Series(wins).value_counts()
    wins = {label: ((win_count / count) * 100) for label, win_count
            in win_summary.items()}
    return {'wins': wins}


def simulate(battle_config, count):
    return simulate_battles(battle_config, count, new_battle)


def simulate_land_battle(battle_config, count):
    return simulate_battles(battle_config, count, new_land_battle)
