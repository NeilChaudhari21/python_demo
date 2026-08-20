"""Validation helpers for product and order data."""

import re

from warehouse_ops.exceptions import ValidationError

SKU_PATTERN = re.compile(r"^[A-Z0-9][A-Z0-9-]{2,31}$")


def is_valid_sku(sku: str) -> bool:
    """Return whether a SKU follows the warehouse naming rules."""
    return bool(isinstance(sku, str) and SKU_PATTERN.match(sku))


def validate_sku(sku: str) -> str:
    """Validate and normalize a SKU."""
    normalized = sku.strip().upper()
    if not is_valid_sku(normalized):
        raise ValidationError(f"Invalid SKU: {sku}")
    return normalized


def validate_quantity(quantity: int) -> int:
    if not isinstance(quantity, int):
        raise ValidationError("Quantity must be an integer")
    if quantity < 0:
        raise ValidationError("Quantity cannot be negative")
    return quantity


def validate_money(amount: float) -> float:
    value = float(amount)
    if value < 0:
        raise ValidationError("Money values cannot be negative")
    return round(value, 2)
