from .army import army_factory
from .info import TRANSPORT
from .unit import unit_factory


def remove_excluded_units(config):
    excluded = (TRANSPORT, )
    return {k: v for k, v in config.items() if k not in excluded}


def build_army(config):
    config = remove_excluded_units(config)
    return army_factory(config, unit_factory=unit_factory)
