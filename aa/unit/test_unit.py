from .info import UNIT_INFO
from .unit import Unit

VALID_ROLL_VALUES = [1, 2, 3, 4, 5, 6]


def test_unit():
    u = Unit(**UNIT_INFO['Infantry'])
    assert repr(u) == 'Infantry'

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
