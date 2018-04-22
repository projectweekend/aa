from .info import TRANSPORT
from .unit import unit_factory


def remove_excluded_units(config):
    excluded = (TRANSPORT, )
    return {k: v for k, v in config.items() if k not in excluded}
