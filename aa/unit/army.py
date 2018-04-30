from collections import Counter
from operator import attrgetter
from .unit import Unit


class Bonuses:

    def __init__(self, army):
        self._army = army

    def remove(self):
        for unit in self._army:
            unit.active_bonus = None

    def to_grant(self):
        for unit in self._army:
            yield from unit.bonuses_granted

    def refresh(self):
        self.remove()
        for bonus in self.to_grant():
            for unit in self._army:
                if unit.name in bonus.targets and unit.active_bonus is None:
                    unit.active_bonus = bonus
                    break


class Roll:

    def __init__(self, army):
        self._army = army

    def attack(self, included_types=None):
        if included_types is None:
            return sum(u.roll.attack()[1] for u in self._army)
        to_roll = (u for u in self._army if u.type in included_types)
        return sum(u.roll.attack()[1] for u in to_roll)

    def defense(self, included_types=None):
        if included_types is None:
            return sum(u.roll.defense()[1] for u in self._army)
        to_roll = (u for u in self._army if u.type in included_types)
        return sum(u.roll.defense()[1] for u in to_roll)


class Remove:

    def __init__(self, army):
        self._army = army

    def by_name(self, unit_name):
        self._army._units = [u for u in self._army._units
                             if u.name != unit_name]

    def by_type(self, type_name):
        self._army._units = [u for u in self._army._units
                             if u.type != type_name]


class Army:

    def __init__(self, units):
        self._units = units
        self.bonuses = Bonuses(army=self)
        self.remove = Remove(army=self)
        self.roll = Roll(army=self)

    def __getitem__(self, item):
        return self._units[item]

    def __len__(self):
        return len(self._units)

    @classmethod
    def build(cls, config):
        units = []
        for name, count in config.items():
            units += [Unit.build_by_name(name) for _ in range(count)]
        return cls(units=units)

    def sort(self, army_type=None):
        if army_type is None:
            sort_key = attrgetter('cost')
        if army_type == 'attack':
            sort_key = attrgetter('rank.attack')
        if army_type == 'defense':
            sort_key = attrgetter('rank.attack')
        self._units = sorted(self._units, key=sort_key, reverse=True)

    def unit_summary(self):
        unit_counts = Counter()
        for u in self._units:
            unit_counts[u.name] += 1
        return dict(unit_counts)

    def take_casulties(self, count):
        if count != 0:
            self._units = self._units[:count * -1]
