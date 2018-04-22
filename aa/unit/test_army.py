from .army import Army


def test_attacking_army():
    config = {
        'tank': 5,
        'infantry': 5,
        'artillery': 2
    }
    army = Army.build(config)
    army.sort('attack')
    for i, unit in enumerate(army):
        if i < 5:
            assert unit.name == 'Tank'
        elif i > 4 and i < 7:
            assert unit.name == 'Artillery'
        else:
            assert unit.name == 'Infantry'
    army.refresh_bonuses()
    boosted_units = [unit for unit in army if unit.active_bonus]
    assert len(boosted_units) == 2
