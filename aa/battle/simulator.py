from collections import Counter
import pandas as pd
from aa.unit import Army
from .battle import Battle, LandBattle
from .utils import battle_factory


new_battle = battle_factory(army_cls=Army, battle_cls=Battle)
new_land_battle = battle_factory(army_cls=Army, battle_cls=LandBattle)


def simulate_battles(battle_config, count, factory):
    wins = []
    stats = []

    for _ in range(count):
        b = factory(config=battle_config)
        b.simulate()
        wins.append(b.winner)
        stats.append(b.stats())

    win_series = pd.Series(wins)
    win_summary = win_series.value_counts().to_dict()
    win_summary['total_played'] = int(win_series.count())

    stats_df = pd.DataFrame(stats)

    return {
        'wins': win_summary,
        'stats': stats_df.mean().to_dict()
    }


def simulate(battle_config, count):
    return simulate_battles(battle_config, count, new_battle)


def simulate_land_battle(battle_config, count):
    return simulate_battles(battle_config, count, new_land_battle)
