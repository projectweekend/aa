from operator import attrgetter


class Battle:

    def __init__(self, attackers, defenders):
        self.attackers = attackers
        self.defenders = defenders

        self._attackers_ipc_before = self.attackers_ipc_value
        self._defenders_ipc_before = self.defenders_ipc_value

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

    @property
    def attackers_count(self):
        return len(self.attackers)

    @property
    def attackers_ipc_value(self):
        return sum(u.cost for u in self.attackers)

    @property
    def defenders_count(self):
        return len(self.defenders)

    @property
    def defenders_ipc_value(self):
        return sum(u.cost for u in self.defenders)

    def prepare_armies(self):
        self.attackers.refresh_bonuses()
        self.attackers.sort('attack')
        self.defenders.refresh_bonuses()
        self.defenders.sort('defense')

    def roll_damage(self):
        return self.attackers.roll_attack(), self.defenders.roll_defense()

    def take_casulties(self, attack_hits, defense_hits):
        self.attackers.take_casulties(defense_hits)
        self.defenders.take_casulties(attack_hits)

    def stats(self):
        att_ipc_lost = self._attackers_ipc_before - self.attackers_ipc_value
        def_ipc_lost = self._defenders_ipc_before - self.defenders_ipc_value
        return {
            'attackers_remaining': self.attackers_count,
            'attackers_ipc_lost': att_ipc_lost,
            'defenders_remaining': self.defenders_count,
            'defenders_ipc_lost': def_ipc_lost,
        }

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


class NavalBattle(Battle):

    def simulate(self):
        round = 0
        while self.winner is None:
            pass
