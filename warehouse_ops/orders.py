"""Purchase order calculations."""

from datetime import date
from typing import Dict, Iterable

from warehouse_ops.models import OrderLine, PurchaseOrder, Supplier
from warehouse_ops.pricing import apply_supplier_discount, money
from warehouse_ops.validators import validate_quantity, validate_sku


def create_purchase_order(order_id: str, supplier_id: str, lines: Iterable[OrderLine]) -> PurchaseOrder:
    order = PurchaseOrder(order_id=order_id, supplier_id=supplier_id, created_on=date.today())
    for line in lines:
        add_order_line(order, line)
    return order


def add_order_line(order: PurchaseOrder, line: OrderLine) -> PurchaseOrder:
    line.sku = validate_sku(line.sku)
    validate_quantity(line.quantity)
    order.add_line(line)
    return order


def calculate_order_total(order: PurchaseOrder, suppliers: Dict[str, Supplier] = None) -> float:
    subtotal = sum(line.subtotal() for line in order.lines)
    supplier = suppliers.get(order.supplier_id) if suppliers else None
    if supplier:
        return apply_supplier_discount(subtotal, supplier)
    return money(subtotal)


def order_summary(order: PurchaseOrder) -> str:
    return "PO %s for supplier %s has %d lines" % (
        order.order_id,
        order.supplier_id,
        len(order.lines),
    )
