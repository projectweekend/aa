import json
import falcon
from aa.battle.utils import land_battle_config


class LandBattleResource:

    def on_get(self, req, res):
        res.media = land_battle_config()
