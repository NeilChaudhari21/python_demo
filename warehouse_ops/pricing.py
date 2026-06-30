"""Pricing and supplier discount calculations."""

from decimal import Decimal, ROUND_HALF_UP
from typing import Iterable

from warehouse_ops.models import OrderLine, Supplier


def money(value) -> float:
    rounded = Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return float(rounded)


def apply_supplier_discount(amount: float, supplier: Supplier) -> float:
    discount_rate = max(0.0, min(float(supplier.discount_rate), 1.0))
    return money(amount * (1 - discount_rate))


def calculate_line_total(line: OrderLine, supplier: Supplier = None) -> float:
    subtotal = line.subtotal()
    if supplier is None:
        return money(subtotal)
    return apply_supplier_discount(subtotal, supplier)


def calculate_order_subtotal(lines: Iterable[OrderLine]) -> float:
    return money(sum(line.subtotal() for line in lines))
