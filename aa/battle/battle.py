from operator import attrgetter


class Battle:

    def __init__(self, attackers, defenders, amphibious_assault=False):
        self.attackers = attackers
        self.defenders = defenders
        self.amphibious_assault = amphibious_assault

    def prepare_armies(self):
        self.attackers.refresh_bonuses()
        self.attackers.sort('attack')
        self.defenders.refresh_bonuses()
        self.defenders.sort('defense')

    def roll_damage(self):
        attack_hits = 0
        defense_hits = 0
        for unit in self.attackers:
            _, damage = unit.roll_attack()
            attack_hits += damage
        for unit in self.defenders:
            _, damage = unit.roll_defense()
            defense_hits += damage
        return attack_hits, defense_hits

    def take_casulties(self, attack_hits, defense_hits):
        self.attackers.take_casulties(defense_hits)
        self.defenders.take_casulties(attack_hits)

    @property
    def winner(self):
        if self.attackers and self.defenders:
            return None
        if not self.attackers and not self.defenders:
            return 'draw'
        if self.attackers and not self.defenders:
            return 'attacker'
        if self.defenders and not self.attackers:
            return 'defender'

    def simulate(self):
        while self.winner is None:
            self.prepare_armies()
            attack_hits, defense_hits = self.roll_damage()
            self.take_casulties(attack_hits=attack_hits,
                                defense_hits=defense_hits)


class LandBattle(Battle):

    def simulate(self):
        round = 0
        while self.winner is None:
            self.prepare_armies()
            attack_hits, defense_hits = self.roll_damage()
            # Remove sea units from amphibious assault
            if round == 0:
                self.attackers.remove_sea_units()
            self.take_casulties(attack_hits=attack_hits,
                                defense_hits=defense_hits)
            round += 1
