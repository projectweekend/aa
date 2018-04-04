from aa.unit.utils import build_army
from .simulator import simulate


EXPECTED_RESULT_LABELS = ('attacker', 'defender', 'draw')


def test_simulator():
    army_size = 5
    attackers = build_army({'tank': army_size})
    defenders = build_army({'tank': army_size})

    results = simulate(attackers, defenders, 100)
    for k, v in results.items():
        assert k in EXPECTED_RESULT_LABELS
        assert isinstance(v, float)
