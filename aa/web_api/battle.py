import json
import falcon
from aa.battle import simulate_land_battle
from aa.battle.utils import land_battle_config


class LandBattleResource:

    battle_config = land_battle_config()

    def on_get(self, req, res):
        res.media = LandBattleResource.battle_config

    def on_post(self, req, res):
        res.media = simulate_land_battle(battle_config=req.media, count=1000)
