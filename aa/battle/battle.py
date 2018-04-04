class Battle:

    def __init__(self, attackers, defenders):
        self.attackers = attackers
        self.defenders = defenders

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
        attack_hits = attack_hits * -1
        defense_hits = defense_hits * -1
        if attack_hits != 0:
            self.defenders = self.defenders[:attack_hits]
        if defense_hits != 0:
            self.attackers = self.attackers[:defense_hits]

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
            attack_hits, defense_hits = self.roll_damage()
            self.take_casulties(attack_hits=attack_hits,
                                defense_hits=defense_hits)
