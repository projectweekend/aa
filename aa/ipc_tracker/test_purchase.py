from collections import defaultdict

import pytest

from aa.unit.info import *

from .purchase import Purchase


@pytest.fixture
def units_to_purchase():
    infantry = [UNIT_INFO[INFANTRY] for _ in range(3)]
    tanks = [UNIT_INFO[TANK] for _ in range(2)]
    return infantry + tanks


def test_purchase(units_to_purchase):
    p = Purchase(units=units_to_purchase)

    assert p.units == units_to_purchase

    expected_ipc = 0
    expected_summary = defaultdict(int)
    for u in units_to_purchase:
        expected_ipc += u[COST]
        expected_summary[u[NAME]] += u[COST]
    assert p.ipc == expected_ipc
    assert p.summary == expected_summary
