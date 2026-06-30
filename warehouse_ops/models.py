"""Dataclasses used by the warehouse operations toolkit."""

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List, Optional


@dataclass
class Product:
    sku: str
    name: str
    supplier_id: str
    unit_cost: float
    reorder_point: int
    quantity_on_hand: int = 0
    location: str = "unassigned"


@dataclass
class Supplier:
    supplier_id: str
    name: str
    discount_rate: float = 0.0
    api_version: str = "1.0"
    catalog_version: str = "1.0"


@dataclass
class OrderLine:
    sku: str
    quantity: int
    unit_price: float

    def subtotal(self) -> float:
        value = Decimal(str(self.quantity)) * Decimal(str(self.unit_price))
        return float(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


@dataclass
class PurchaseOrder:
    order_id: str
    supplier_id: str
    lines: List[OrderLine] = field(default_factory=list)
    created_on: Optional[date] = None
    status: str = "draft"

    def add_line(self, line: OrderLine) -> None:
        self.lines.append(line)


@dataclass
class Shipment:
    shipment_id: str
    order_id: str
    carrier: str
    tracking_number: str
    status: str = "pending"
    quantities: Dict[str, int] = field(default_factory=dict)
