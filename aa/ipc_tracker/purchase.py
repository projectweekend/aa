from collections import defaultdict


class Purchase:
    """
    Purchase represents the items purchased and IPCs spent for a turn
    """

    def __init__(self, units):
        self.units = units
        self.ipc, self.summary = self.summarize(units=units)

    @staticmethod
    def summarize(units):
        ipc = 0
        summary = defaultdict(int)
        for u in units:
            summary[u['name']] += u['cost']
            ipc += u['cost']
        return ipc, summary
