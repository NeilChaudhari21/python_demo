import pytest

from warehouse_ops.exceptions import InventoryError
from warehouse_ops.inventory import InventoryLedger
from warehouse_ops.models import Product


def test_inventory_adjustments_and_reorder_alerts():
    ledger = InventoryLedger([
        Product("SKU-1001", "Tape", "sup-001", 4.25, reorder_point=20, quantity_on_hand=12),
        Product("SKU-1002", "Mailer", "sup-001", 0.85, reorder_point=50, quantity_on_hand=120),
    ])

    assert ledger.add_inventory("SKU-1001", 8) == 20
    assert ledger.remove_inventory("SKU-1002", 20) == 100
    assert [product.sku for product in ledger.reorder_alerts()] == ["SKU-1001"]


def test_inventory_rejects_negative_stock():
    ledger = InventoryLedger([
        Product("SKU-1001", "Tape", "sup-001", 4.25, reorder_point=20, quantity_on_hand=2),
    ])

    with pytest.raises(InventoryError):
        ledger.remove_inventory("SKU-1001", 3)
