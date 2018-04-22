from .simulator import simulate


EXPECTED_RESULT_LABELS = ('attacker', 'defender', 'draw')


def test_simulator():
    config = {
        'attacker': {
            'tank': 5
        },
        'defender': {
            'tank': 5
        }
    }

    results = simulate(config, 100)
    for k, v in results.items():
        assert k in EXPECTED_RESULT_LABELS
        assert isinstance(v, float)
