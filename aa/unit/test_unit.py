from .info import *
from .unit import unit_factory

VALID_ROLL_VALUES = [1, 2, 3, 4, 5, 6]


def test_unit():
    u = unit_factory('infantry')
    assert repr(u) == 'Infantry'

    assert u.attack_rank == 4
    assert u.defense_rank == 5
    assert u.bonuses_granted == []

    for _ in range(10):
        assert u.roll() in VALID_ROLL_VALUES

        roll, damage = u.roll_attack()
        if roll <= u.attack:
            assert damage == 1
        else:
            assert damage == 0

        roll, damage = u.roll_defense()
        if roll <= u.defense:
            assert damage == 1
        else:
            assert damage == 0


def test_unit_with_enhancements():
    u = unit_factory('artillery')
    assert u.attack_rank == 7.5
    assert u.defense_rank == 7.5
    for b in u.bonuses_granted:
        assert b.targets == [INFANTRY, MECHANIZED_INFANTRY]
        assert b.boosted_attribute == ATTACK
        assert b.boost_value == 2
