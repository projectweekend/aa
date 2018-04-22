from operator import attrgetter


class Army:

    def __init__(self, units):
        self._units = units

    def __getitem__(self, item):
        return self._units[item]

    def __len__(self):
        return len(self._units)

    def _remove_bonuses(self):
        for u in self._units:
            u.active_bonus = None

    def _bonuses_to_apply(self):
        for u in self._units:
            yield from u.bonuses_granted

    def sort(self, army_type=None):
        if army_type is None:
            sort_key = attrgetter('cost')
        if army_type == 'attack':
            sort_key = attrgetter('attack_rank')
        if army_type == 'defense':
            sort_key = attrgetter('defense_rank')
        self._units = sorted(self._units, key=sort_key, reverse=True)

    def refresh_bonuses(self):
        self._remove_bonuses()
        for b in self._bonuses_to_apply():
            for u in self._units:
                if u.name in b.targets and u.active_bonus is None:
                    u.active_bonus = b
                    break

    def take_casulties(self, count):
        if count != 0:
            self._units = self._units[:count * -1]


def army_factory(cgf, unit_factory):
    units = []
    for name, count in cgf.items():
        units += [unit_factory(name) for _ in range(count)]
    return Army(units=units)
