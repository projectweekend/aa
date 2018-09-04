class Production:
    """
    Production represents the IPC amount currently being earned.
    """

    def __init__(self, ipc):
        self.ipc = ipc


class ProductionHistory:

    def __init__(self, productions=None):
        self._productions = [] if productions is None else productions

    def __len__(self):
        return len(self._productions)

    def __getitem__(self, key):
        return self._productions[key]

    @property
    def current_ipc(self):
        try:
            return self._productions[-1].ipc
        except IndexError:
            return 0

    def add(self, production):
        self._productions.append(production)

    @classmethod
    def new(cls, starting_ipc):
        return cls(productions=[Production(ipc=starting_ipc)])
