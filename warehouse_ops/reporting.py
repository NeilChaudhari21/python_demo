"""Report generation for inventory and reorder workflows."""

from datetime import datetime, timezone
from typing import Iterable, List

from warehouse_ops.models import Product
from warehouse_ops.report_templates import INVENTORY_HEADER, REORDER_HEADER, format_inventory_row


def generate_inventory_report(products: Iterable[Product]) -> str:
    rows = [INVENTORY_HEADER]
    rows.extend(format_inventory_row(product) for product in products)
    rows.append("Generated,%s" % datetime.now(timezone.utc).isoformat())
    return "\n".join(rows)


def generate_reorder_report(products: Iterable[Product]) -> str:
    rows: List[str] = [REORDER_HEADER]
    for product in products:
        if product.quantity_on_hand <= product.reorder_point:
            rows.append("%s,%s,%d,%d" % (
                product.sku,
                product.name,
                product.quantity_on_hand,
                product.reorder_point,
            ))
    return "\n".join(rows)


def summarize_inventory(products: Iterable[Product]) -> dict:
    products = list(products)
    return {
        "product_count": len(products),
        "total_units": sum(product.quantity_on_hand for product in products),
        "total_value": round(sum(product.quantity_on_hand * product.unit_cost for product in products), 2),
    }
