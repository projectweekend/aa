from .info import TRANSPORT
from .unit import unit_factory


def _cost_and_name(unit):
    return '{0}-{1}'.format(unit.cost, unit.name)


def remove_excluded_units(config):
    excluded = (TRANSPORT, )
    return {k: v for k, v in config.items() if k not in excluded}


def build_army(config, unit_factory=unit_factory):
    army = []
    config = remove_excluded_units(config)
    for name, count in config.items():
        army += [unit_factory(name) for _ in range(count)]
    return sorted(army, key=_cost_and_name)[::-1]
