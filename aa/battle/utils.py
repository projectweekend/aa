from aa.unit.info import *


def battle_factory(army_cls, battle_cls):
    def factory(config):
        attackers = army_cls.build(config['attacker'])
        defenders = army_cls.build(config['defender'])
        return battle_cls(attackers=attackers, defenders=defenders)
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
