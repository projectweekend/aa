from aa.unit import Army
from .utils import battle_factory


def test_battle_factory():
    new_battle = battle_factory(army=Army)
    config = {
        'attacker': {
            'infantry': 5,
            'tank': 5
        },
        'defender': {
            'infantry': 11
        }
    }

    b = new_battle(config)
    assert len(b.attackers) == 10
    assert len(b.defenders) == 11
