import json
import falcon
from aa.unit.info import *


class UnitInfoResource:

    def on_get(self, req, res):
        res.media = {
            'land': (
                UNIT_INFO[INFANTRY],
                UNIT_INFO[ARTILLERY],
                UNIT_INFO[MECHANIZED_INFANTRY],
                UNIT_INFO[TANK]
            ),
            'air': (
                UNIT_INFO[FIGHTER],
                UNIT_INFO[TACTICAL_BOMBER],
                UNIT_INFO[STRATEGIC_BOMBER]
            ),
            'sea': (
                UNIT_INFO[TRANSPORT],
                UNIT_INFO[SUBMARINE],
                UNIT_INFO[DESTROYER],
                UNIT_INFO[CRUISER],
                UNIT_INFO[AIRCRAFT_CARRIER],
                UNIT_INFO[BATTLESHIP]
            )
        }
