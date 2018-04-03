def _cost_and_name(unit):
    return '{0}-{1}'.format(unit.cost, unit.name)


def build_army(config, unit_factory):
    army = []
    for name, count in config.items():
        army += [unit_factory(name) for _ in range(count)]
    return sorted(army, key=_cost_and_name)[::-1]
