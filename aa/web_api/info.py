import json
import falcon
from aa.unit.info import *


class UnitInfoResource:

    def on_get(self, req, res):
        res.media = {
            'land': [UNIT_INFO[name] for name in LAND_UNITS],
            'air': [UNIT_INFO[name] for name in AIR_UNITS],
            'sea': [UNIT_INFO[name] for name in SEA_UNITS]
        }
