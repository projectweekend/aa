import json
import falcon
from aa.unit.info import *


class UnitInfoResource:

    def on_get(self, req, res):
        res.media = {
            LAND: [UNIT_INFO[name] for name in LAND_UNITS],
            AIR: [UNIT_INFO[name] for name in AIR_UNITS],
            SEA: [UNIT_INFO[name] for name in SEA_UNITS]
        }
