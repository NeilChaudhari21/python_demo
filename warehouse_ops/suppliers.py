"""Supplier lookup and API version helpers."""

from packaging.version import Version
from typing import Dict, Iterable

from warehouse_ops.models import Supplier


def build_supplier_index(suppliers: Iterable[Supplier]) -> Dict[str, Supplier]:
    return {supplier.supplier_id: supplier for supplier in suppliers}


def validate_supplier_api_version(version: str, minimum: str = "1.0") -> bool:
    return Version(version) >= Version(minimum)


def preferred_supplier(suppliers: Iterable[Supplier]) -> Supplier:
    ordered = sorted(suppliers, key=lambda supplier: supplier.discount_rate, reverse=True)
    if not ordered:
        raise ValueError("No suppliers available")
    return ordered[0]
