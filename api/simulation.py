import json
import falcon


def validate_payload(media):
    unit_names = ('infantry', 'artillery', 'mech_infantry', 'tank',
                  'fighter', 'tactical_bomber', 'bomber')

    for army_type in ('attacker', 'defender'):
        army = media.get(army_type)
        if army is None:
            raise falcon.HTTPBadRequest()
        for k, v in army.items():
            if k not in unit_names or not isinstance(v, int):
                raise falcon.HTTPBadRequest()

    return media


class SimulationResource:

    def __init__(self, army_builder, battle_simulator):
        self._army_builder = army_builder
        self._battle_simulator = battle_simulator

    def on_post(self, req, res):
        payload = validate_payload(req.media)
        attackers = self._army_builder(payload['attacker'])
        defenders = self._army_builder(payload['defender'])
        res.media = self._battle_simulator(attackers, defenders, 1000)
        res.status = falcon.HTTP_OK
