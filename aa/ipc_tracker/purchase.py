from collections import defaultdict


class Purchase:
    """
    Purchase represents the items purchased and IPCs spent for a turn
    """

    def __init__(self, units, ipc_before):
        self.units = units
        self.ipc_before = ipc_before
        self.ipc_cost, self.summary = self.summarize(units=units)

        if self.ipc_after < 0:
            raise Exception

    @property
    def ipc_after(self):
        return self.ipc_before - self.ipc_cost

    @classmethod
    def new(cls, tracker, units):
        return cls(units=units, ipc_before=tracker.ipc_avail)

    @staticmethod
    def summarize(units):
        ipc = 0
        summary = defaultdict(int)
        for u in units:
            summary[u['name']] += u['cost']
            ipc += u['cost']
        return ipc, summary
