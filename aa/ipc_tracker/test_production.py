from .production import Production, ProductionHistory


def test_production_history():
    ph = ProductionHistory()
    assert ph.current_ipc == 0
    assert len(ph) == 0

    ph.add(Production(ipc=30))
    assert ph.current_ipc == 30
    assert len(ph) == 1
