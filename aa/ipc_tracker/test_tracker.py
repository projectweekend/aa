import pytest

from aa.unit.info import *

from .tracker import Tracker


def test_tracker():
    t = Tracker.new(starting_ipc=30)
    assert t.current_ipc == 30
    assert t.avail_ipc == 30

    t.purchase(units=[UNIT_INFO[INFANTRY]])
    assert t.current_ipc == 30
    assert t.avail_ipc == 27

    t.earn_ipc()
    assert t.current_ipc == 30
    assert t.avail_ipc == 57

    units = [UNIT_INFO[INFANTRY] for _ in range(20)]
    with pytest.raises(Exception):
        t.purchase(units=units)
    assert t.current_ipc == 30
    assert t.avail_ipc == 57    
