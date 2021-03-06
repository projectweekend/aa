import datetime

import falcon
from falcon import testing
import pytest

from aa.app import create_application
from aa.unit.info import *


@pytest.fixture()
def client():
    return testing.TestClient(create_application())


def test_get_a_land_battle_template(client):
    result = client.simulate_get('/land-battle')
    expected_attacker_keys = [unit for unit in
                              LAND_UNITS + AIR_UNITS + (CRUISER, BATTLESHIP)]
    expected_defender_keys = [unit for unit in LAND_UNITS + AIR_UNITS]

    for k, v in result.json['attacker'].items():
        assert k in expected_attacker_keys
        assert v == 0

    for k, v in result.json['defender'].items():
        assert k in expected_defender_keys
        assert v == 0


def test_simulate_land_battle(client):
    battle_config = client.simulate_get('/land-battle').json
    battle_config['attacker']['Infantry'] = 5
    battle_config['defender']['Infantry'] = 5
    result = client.simulate_post('/land-battle', json=battle_config)
    assert isinstance(result.json['wins']['attacker'], int)
    assert isinstance(result.json['wins']['defender'], int)
    assert isinstance(result.json['wins']['draw'], int)
    assert isinstance(result.json['stats']['attackers_remaining'], float)
    assert isinstance(result.json['stats']['defenders_remaining'], float)
    assert isinstance(result.json['stats']['attackers_ipc_lost'], float)
    assert isinstance(result.json['stats']['defenders_ipc_lost'], float)


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
    assert isinstance(result.json['wins']['attacker'], int)
    assert isinstance(result.json['wins']['defender'], int)
    assert isinstance(result.json['wins']['draw'], int)


def test_simulate_battle_missing_army(client):
    battle_missing_army = {
        'attacker': {
            'Tank': 5
        }
    }
    result = client.simulate_post('/', json=battle_missing_army)
    assert result.status == falcon.HTTP_400


def test_simulate_battle_army_with_no_units(client):
    battle_army_with_no_units = {
        'attacker': {},
        'defender': {}
    }
    result = client.simulate_post('/', json=battle_army_with_no_units)
    assert result.status == falcon.HTTP_400


def test_simulate_battle_invalid_unit_name(client):
    battle_invalid_unit_name = {
        'attacker': {
            'Tank': 5
        },
        'defender': {
            'Paratrooper': 5
        }
    }
    result = client.simulate_post('/', json=battle_invalid_unit_name)
    assert result.status == falcon.HTTP_400


def test_simulate_battle_invalid_unit_count(client):
    battle_invalid_unit_count = {
        'attacker': {
            'Tank': 5
        },
        'defender': {
            'Infantry': 'not int'
        }
    }
    result = client.simulate_post('/', json=battle_invalid_unit_count)
    assert result.status == falcon.HTTP_400


def test_ipctracker_create_valid(client):
    new_ipc_tracker = {
        'name': 'A&A Game',
        'starting_ipc': 30
    }
    result = client.simulate_post('/ipc-tracker', json=new_ipc_tracker)
    assert result.status == falcon.HTTP_201
    assert result.json['starting_ipc'] == 30
    assert result.json['name'] == 'A&A Game'
    assert type(result.json['game_id']) == str
    assert type(result.json['created_at']) == int
