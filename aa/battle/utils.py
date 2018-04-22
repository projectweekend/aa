from .battle import Battle


def battle_factory(army):
    def factory(config):
        attackers = army.build(config['attacker'])
        defenders = army.build(config['defender'])
        return Battle(attackers=attackers, defenders=defenders)
    return factory
