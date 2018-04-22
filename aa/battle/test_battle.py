from aa.unit.utils import build_army
from .battle import Battle


def test_battle_damage_and_casulties():
    army_size = 5
    attackers = build_army({'tank': army_size})
    defenders = build_army({'tank': army_size})

    b = Battle(attackers, defenders)

    attack_hits, defense_hits = b.roll_damage()
    b.take_casulties(attack_hits, defense_hits)

    expected_attacker_count = army_size - defense_hits
    assert len(b.attackers) == expected_attacker_count

    expected_defender_count = army_size - attack_hits
    assert len(b.defenders) == expected_defender_count


def test_battle_simulate():
    army_size = 5
    for _ in range(100):
        attackers = build_army({'tank': army_size})
        defenders = build_army({'tank': army_size})

        b = Battle(attackers, defenders)
        print(type(b.attackers))
        print(type(b.defenders))
        b.simulate()

        assert b.winner is not None

        if not b.attackers and not b.defenders:
            assert b.winner == 'draw'

        if b.attackers and not b.defenders:
            assert b.winner == 'attacker'

        if b.defenders and not b.attackers:
            assert b.winner == 'defender'
