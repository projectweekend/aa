import json
import falcon
from aa.unit.info import *


def unit_info(unit_name):
    info = {'name': unit_name}
    info.update(UNIT_INFO[unit_name])
    return info


class UnitInfoResource:

    def on_get(self, req, res):
        res.media = {
            'land': [unit_info(name) for name in LAND_UNITS],
            'air': [unit_info(name) for name in AIR_UNITS],
            'sea': [unit_info(name) for name in SEA_UNITS]
        }
