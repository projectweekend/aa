from .info import *
from .unit import Unit, Bonus

VALID_ROLL_VALUES = [1, 2, 3, 4, 5, 6]


def test_unit():
    u = Unit.build_by_name('infantry')
    assert repr(u) == 'Infantry'

    assert u.rank.attack == 4
    assert u.rank.defense == 5
    assert u.bonuses_granted == []

    for _ in range(10):
        roll, damage = u.roll.attack()
        if roll <= u.attack:
            assert damage == 1
        else:
            assert damage == 0

        roll, damage = u.roll.defense()
        if roll <= u.defense:
            assert damage == 1
        else:
            assert damage == 0


def test_unit_with_bonuses_granted():
    u = Unit.build_by_name('artillery')
    assert u.rank.attack == 7.5
    assert u.rank.defense == 7.5
    for b in u.bonuses_granted:
        assert b.targets == [INFANTRY, MECHANIZED_INFANTRY]
        assert b.boosted_attribute == ATTACK
        assert b.boost_value == 2


def test_unit_with_active_bonus():
    giver = Unit.build_by_name('artillery')
    receiver = Unit.build_by_name('infantry')

    receiver.active_bonus = giver.bonuses_granted[0]
    assert receiver.attack == 2
    assert receiver.defense == 2
    receiver.active_bonus = None
    assert receiver.attack == 1
    assert receiver.defense == 2

    defense_bonus = Bonus(targets=['Infantry'], boosted_attribute='defense',
                          boost_value=4)
    receiver.active_bonus = defense_bonus
    assert receiver.attack == 1
    assert receiver.defense == 4
