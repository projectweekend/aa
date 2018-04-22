from operator import attrgetter


class Army:

    def __init__(self, units):
        self.units = units
        self._refresh_bonuses()

    def _remove_bonuses(self):
        for u in self.units:
            u.active_bonus = None

    def _bonuses_to_apply(self):
        for u in self.units:
            yield from u.bonuses_granted

    def _refresh_bonuses(self):
        self._remove_bonuses()
        for b in self._bonuses_to_apply():
            for u in self.units:
                if u.name in b.targets and u.active_bonus is None:
                    u.active_bonus = b
                    break

    def sort(self, army_type):
        if army_type == 'attack':
            sort_key = attrgetter('attack_rank')
        elif army_type == 'defense':
            sort_key = attrgetter('defense_rank')
        else:
            raise ValueError('Invalid army_type')

        self.units = sorted(self.units, key=sort_key, reverse=True)


def army_factory(cgf, unit_factory):
    units = []
    for name, count in cgf.items():
        units += [unit_factory(name) for _ in range(count)]
    return Army(units=units)
