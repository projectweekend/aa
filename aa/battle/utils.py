from aa.unit.info import *
from .battle import Battle


def battle_factory(army):
    def factory(config):
        attackers = army.build(config['attacker'])
        defenders = army.build(config['defender'])
        return Battle(attackers=attackers, defenders=defenders)
    return factory


def land_battle_attacker_units():
    yield from LAND_UNITS
    yield from AIR_UNITS
    yield from (CRUISER, BATTLESHIP)


def land_battle_defender_units():
    yield from LAND_UNITS
    yield from AIR_UNITS


def land_battle_config():
    return {
        'attacker': {unit: 0 for unit in land_battle_attacker_units()},
        'defender': {unit: 0 for unit in land_battle_defender_units()}
    }
