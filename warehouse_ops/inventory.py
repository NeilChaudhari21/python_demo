"""Inventory ledger operations."""

from typing import Dict, Iterable, List

from warehouse_ops.exceptions import InventoryError
from warehouse_ops.models import Product
from warehouse_ops.validators import validate_quantity, validate_sku


class InventoryLedger:
    """In-memory inventory ledger for small warehouse workflows."""

    def __init__(self, products: Iterable[Product] = ()):
        self.products: Dict[str, Product] = {}
        for product in products:
            self.add_product(product)

    def add_product(self, product: Product) -> None:
        product.sku = validate_sku(product.sku)
        validate_quantity(product.quantity_on_hand)
        validate_quantity(product.reorder_point)
        self.products[product.sku] = product

    def remove_product(self, sku: str) -> Product:
        sku = validate_sku(sku)
        try:
            return self.products.pop(sku)
        except KeyError:
            raise InventoryError(f"Unknown SKU: {sku}")

    def adjust_stock(self, sku: str, quantity_delta: int, reason: str = "") -> int:
        sku = validate_sku(sku)
        if sku not in self.products:
            raise InventoryError(f"Unknown SKU: {sku}")
        product = self.products[sku]
        next_quantity = product.quantity_on_hand + int(quantity_delta)
        if next_quantity < 0:
            raise InventoryError("Adjustment would make stock negative")
        product.quantity_on_hand = next_quantity
        return next_quantity

    def add_inventory(self, sku: str, quantity: int) -> int:
        return self.adjust_stock(sku, validate_quantity(quantity), "receiving")

    def remove_inventory(self, sku: str, quantity: int) -> int:
        return self.adjust_stock(sku, -validate_quantity(quantity), "fulfillment")

    def reorder_alerts(self) -> List[Product]:
        return [
            product
            for product in self.products.values()
            if product.quantity_on_hand <= product.reorder_point
        ]

    def inventory_value(self) -> float:
        total = sum(p.unit_cost * p.quantity_on_hand for p in self.products.values())
        return round(total, 2)
