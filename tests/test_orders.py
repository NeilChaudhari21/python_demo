from warehouse_ops.models import OrderLine, Supplier
from warehouse_ops.orders import calculate_order_total, create_purchase_order, order_summary


def test_purchase_order_total_with_supplier_discount():
    order = create_purchase_order(
        "PO-100",
        "sup-001",
        [OrderLine("SKU-1001", 2, 10.00), OrderLine("SKU-1002", 1, 5.00)],
    )
    suppliers = {"sup-001": Supplier("sup-001", "North Coast", discount_rate=0.10)}

    assert calculate_order_total(order, suppliers) == 22.5
    assert order_summary(order) == "PO PO-100 for supplier sup-001 has 2 lines"
