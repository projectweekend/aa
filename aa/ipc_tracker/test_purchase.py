from collections import defaultdict

import pytest

from aa.unit.info import *

from .purchase import Purchase, PurchaseHistory


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

    p = Purchase(units=units_to_purchase)

    assert p.units == units_to_purchase
    assert p.ipc == expected_ipc_cost
    assert p.summary == expected_summary


def test_purchase_history(units_to_purchase):
    purchase_hist = PurchaseHistory()
    purchase_hist.add(Purchase(units=units_to_purchase))

    assert len(purchase_hist) == 1
    assert purchase_hist.total_spent == 21

    purchase_hist.add(Purchase(units=units_to_purchase))

    assert len(purchase_hist) == 2
    assert purchase_hist.total_spent == 42
