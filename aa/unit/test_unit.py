from .info import *
from .unit import unit_factory, Bonus

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


def test_unit_with_bonuses_granted():
    u = unit_factory('artillery')
    assert u.attack_rank == 7.5
    assert u.defense_rank == 7.5
    for b in u.bonuses_granted:
        assert b.targets == [INFANTRY, MECHANIZED_INFANTRY]
        assert b.boosted_attribute == ATTACK
        assert b.boost_value == 2


def test_unit_with_active_bonus():
    giver = unit_factory('artillery')
    receiver = unit_factory('infantry')

    receiver.active_bonus = giver.bonuses_granted[0]
    assert receiver.attack_with_bonus == 2
    assert receiver.defense_with_bonus == 2
    receiver.active_bonus = None
    assert receiver.attack_with_bonus == 1
    assert receiver.defense_with_bonus == 2

    defense_bonus = Bonus(targets=['Infantry'], boosted_attribute='defense',
                          boost_value=4)
    receiver.active_bonus = defense_bonus
    assert receiver.attack_with_bonus == 1
    assert receiver.defense_with_bonus == 4
