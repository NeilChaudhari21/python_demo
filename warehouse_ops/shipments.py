"""Shipment receiving helpers."""

from warehouse_ops.inventory import InventoryLedger
from warehouse_ops.models import Shipment
from warehouse_ops.validators import validate_quantity, validate_sku


def receive_shipment(ledger: InventoryLedger, shipment: Shipment) -> Shipment:
    for sku, quantity in shipment.quantities.items():
        ledger.add_inventory(validate_sku(sku), validate_quantity(quantity))
    shipment.status = "received"
    return shipment


def mark_in_transit(shipment: Shipment) -> Shipment:
    shipment.status = "in_transit"
    return shipment
