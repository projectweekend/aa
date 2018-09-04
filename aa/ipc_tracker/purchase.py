from collections import defaultdict


class Purchase:
    """
    Purchase represents the items purchased and IPCs spent in a single action.
    """

    def __init__(self, units):
        self.units = units
        self.ipc, self.summary = self._summarize(units=units)

    @staticmethod
    def _summarize(units):
        ipc = 0
        summary = defaultdict(int)
        for u in units:
            summary[u['name']] += u['cost']
            ipc += u['cost']
        return ipc, summary


class PurchaseHistory:
    """
    PurchaseHistory is a sequence of Purchase items with other helpful
    properties.
    """

    def __init__(self, purchases=None):
        self._purchases = [] if purchases is None else purchases
        self.total_spent = sum(p.ipc for p in self._purchases)

    def __len__(self):
        return len(self._purchases)

    def __getitem__(self, key):
        return self._purchases[key]

    def add(self, purchase):
        self.total_spent += purchase.ipc
        self._purchases.append(purchase)
