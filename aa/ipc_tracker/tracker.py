from .production import Production, ProductionHistory
from .purchase import Purchase, PurchaseHistory


class Tracker:
    """
    Tracker manages the state of IPC earnings and purchases
    """

    def __init__(self, purchase_hist, production_hist, avail_ipc=None):
        self.purchase_hist = purchase_hist
        self.production_hist = production_hist
        self.avail_ipc = self.current_ipc if avail_ipc is None else avail_ipc

    @property
    def current_ipc(self):
        return self.production_hist.current_ipc

    def change_ipc(self, ipc):
        self.production_hist.add(Production(ipc))

    def purchase(self, units):
        p = Purchase(units=units)
        if p.ipc > self.avail_ipc:
            raise Exception('Not enough avail_ipc to purchase these units')
        self.purchase_hist.add(p)
        self.avail_ipc -= p.ipc

    def earn_ipc(self):
        self.avail_ipc += self.current_ipc

    @classmethod
    def new(cls, starting_ipc):
        productions = [Production(ipc=starting_ipc)]
        return cls(purchase_hist=PurchaseHistory(),
                   production_hist=ProductionHistory(productions=productions))
