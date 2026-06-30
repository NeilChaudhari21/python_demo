from warehouse_ops.models import OrderLine, Supplier
from warehouse_ops.pricing import apply_supplier_discount, calculate_line_total, calculate_order_subtotal


def test_pricing_helpers_round_money():
    supplier = Supplier("sup-001", "North Coast", discount_rate=0.15)
    assert apply_supplier_discount(100, supplier) == 85.0
    assert calculate_line_total(OrderLine("SKU-1001", 3, 1.335)) == 4.01
    assert calculate_order_subtotal([OrderLine("SKU-1001", 2, 2.50)]) == 5.0
