# import falcon
# from falcon import testing
# import pytest
#
# from aa.app import create_application
# from aa.unit.info import *
#
#
# @pytest.fixture()
# def client():
#     return testing.TestClient(create_application())
#
#
# def test_get_unit_info(client):
#     result = client.simulate_get('/unit-info')
#     for unit in result.json[LAND]:
#         assert unit == UNIT_INFO[unit['name']]
#
#
# def test_simulate_battle(client):
#     battle = {
#         'attacker': {
#             'Infantry': 5,
#             'Tank': 5
#         },
#         'defender': {
#             'Infantry': 10
#         }
#     }
#     result = client.simulate_post('/', json=battle)
#     assert isinstance(result.json['attacker'], float)
#     assert isinstance(result.json['defender'], float)
#     assert isinstance(result.json['draw'], float)
#
#
# def test_simulate_battle_missing_army(client):
#     battle_missing_army = {
#         'attacker': {
#             'Tank': 5
#         }
#     }
#     result = client.simulate_post('/', json=battle_missing_army)
#     assert result.status == falcon.HTTP_400
#
#
# def test_simulate_battle_army_with_no_units(client):
#     battle_army_with_no_units = {
#         'attacker': {},
#         'defender': {}
#     }
#     result = client.simulate_post('/', json=battle_army_with_no_units)
#     assert result.status == falcon.HTTP_400
#
#
# def test_simulate_battle_invalid_unit_name(client):
#     battle_invalid_unit_name = {
#         'attacker': {
#             'Tank': 5
#         },
#         'defender': {
#             'Paratrooper': 5
#         }
#     }
#     result = client.simulate_post('/', json=battle_invalid_unit_name)
#     assert result.status == falcon.HTTP_400
#
#
# def test_simulate_battle_invalid_unit_count(client):
#     battle_invalid_unit_count = {
#         'attacker': {
#             'Tank': 5
#         },
#         'defender': {
#             'Infantry': 'not int'
#         }
#     }
#     result = client.simulate_post('/', json=battle_invalid_unit_count)
#     assert result.status == falcon.HTTP_400
