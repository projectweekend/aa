import json
import falcon
from aa.battle import simulate
from aa.unit.info import UNIT_NAMES


def validate_payload(media):
    for army_type in ('attacker', 'defender'):
        army = media.get(army_type)
        # an attacker/defender army element is not present
        if army is None:
            msg = 'Missing army for {0}'
            raise falcon.HTTPBadRequest(msg.format(army_type))
        # an attacker/defender army element is present, but has no units
        if not army:
            msg = 'Army has no units for {0}'
            raise falcon.HTTPBadRequest(msg.format(army_type))
        for k, v in army.items():
            if k not in UNIT_NAMES:
                msg = 'Incorrect unit name: {0}'
                raise falcon.HTTPBadRequest(msg.format(k))
            if not isinstance(v, int):
                msg = '{0} count must be an integer'
                raise falcon.HTTPBadRequest(msg.format(k))

    return media


class SimulationResource:

    def on_post(self, req, res):
        payload = validate_payload(req.media)
        res.media = simulate(battle_config=payload, count=1000)
        res.status = falcon.HTTP_OK
