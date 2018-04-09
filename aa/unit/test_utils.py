from .unit import unit_factory
from .utils import build_army


def test_build_army():
    config = {
        'infantry': 2,
        'tank': 1
    }
    army = build_army(config=config, unit_factory=unit_factory)
    assert len(army) == 3
    assert army[0].name == 'Tank'
    assert army[0].cost == 6
    assert army[0].attack == 3
    assert army[0].defense == 3

    assert army[1].name == 'Infantry'
    assert army[1].cost == 3
    assert army[1].attack == 1
    assert army[1].defense == 2

    assert army[2].name == 'Infantry'
    assert army[2].cost == 3
    assert army[2].attack == 1
    assert army[2].defense == 2
