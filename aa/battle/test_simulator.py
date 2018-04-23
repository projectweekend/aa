from .simulator import simulate, simulate_land_battle


EXPECTED_RESULT_LABELS = ('attacker', 'defender', 'draw', 'total_played')


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
    for k, v in results['wins'].items():
        assert k in EXPECTED_RESULT_LABELS
        assert isinstance(v, int)


def test_land_battle_simulator():
    config = {
        'attacker': {
            'tank': 5,
            'battleship': 1
        },
        'defender': {
            'tank': 5
        }
    }
    results = simulate_land_battle(config, 100)
    for k, v in results['wins'].items():
        assert k in EXPECTED_RESULT_LABELS
        assert isinstance(v, int)
