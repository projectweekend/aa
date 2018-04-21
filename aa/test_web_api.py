from falcon import testing
import pytest

from aa.app import create_application
from aa.unit.info import *


@pytest.fixture()
def client():
    return testing.TestClient(create_application())


def test_get_unit_info(client):
    result = client.simulate_get('/unit-info')
    for unit in result.json[LAND]:
        assert unit == UNIT_INFO[unit['name']]


def test_simulate_battle(client):
    battle = {
        'attacker': {
            'Infantry': 5,
            'Tank': 5
        },
        'defender': {
            'Infantry': 10
        }
    }
    result = client.simulate_post('/', json=battle)
    assert isinstance(result.json['attacker'], float)
    assert isinstance(result.json['defender'], float)
    assert isinstance(result.json['draw'], float)
