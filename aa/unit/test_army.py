from .army import army_factory
from .unit import unit_factory


def test_attacking_army():
    config = {
        'tank': 5,
        'infantry': 5,
        'artillery': 2
    }
    army = army_factory(config, unit_factory)
    army.sort('attack')
    boosted_infantry_count = 0
    for i, unit in enumerate(army):
        if i < 5:
            assert unit.name == 'Tank'
        elif i > 4 and i < 7:
            assert unit.name == 'Artillery'
        else:
            assert unit.name == 'Infantry'
