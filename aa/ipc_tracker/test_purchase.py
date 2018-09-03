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
    expected_ipc_cost = 0
    expected_summary = defaultdict(int)
    for u in units_to_purchase:
        expected_ipc_cost += u[COST]
        expected_summary[u[NAME]] += u[COST]
    starting_ipc = expected_ipc_cost + 5

    p = Purchase(units=units_to_purchase, ipc_before=starting_ipc)

    assert p.units == units_to_purchase
    assert p.ipc_before == starting_ipc
    assert p.ipc_cost == expected_ipc_cost
    assert p.summary == expected_summary
    assert p.ipc_after == 5
