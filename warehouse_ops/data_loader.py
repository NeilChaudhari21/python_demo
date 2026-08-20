"""Load products, suppliers, and orders from CSV files."""

from typing import List

from warehouse_ops.csv_utils import parse_csv_text, require_columns
from warehouse_ops.exceptions import DataLoadError
from warehouse_ops.models import OrderLine, Product, Supplier


def read_text_file(path: str) -> str:
    try:
        with open(path) as f:
            return f.read()
    except OSError as exc:
        raise DataLoadError(f"Unable to read {path}: {exc}")


def load_products(path: str) -> List[Product]:
    rows = parse_csv_text(read_text_file(path))
    require_columns(rows, ["sku", "name", "supplier_id", "unit_cost", "reorder_point", "quantity_on_hand"])
    return [
        Product(
            sku=row["sku"],
            name=row["name"],
            supplier_id=row["supplier_id"],
            unit_cost=float(row["unit_cost"]),
            reorder_point=int(row["reorder_point"]),
            quantity_on_hand=int(row["quantity_on_hand"]),
            location=row.get("location", "unassigned"),
        )
        for row in rows
    ]


def load_suppliers(path: str) -> List[Supplier]:
    rows = parse_csv_text(read_text_file(path))
    require_columns(rows, ["supplier_id", "name", "discount_rate"])
    return [
        Supplier(
            supplier_id=row["supplier_id"],
            name=row["name"],
            discount_rate=float(row["discount_rate"]),
            api_version=row.get("api_version", "1.0"),
            catalog_version=row.get("catalog_version", "1.0"),
        )
        for row in rows
    ]


def load_order_lines(path: str) -> List[OrderLine]:
    rows = parse_csv_text(read_text_file(path))
    require_columns(rows, ["sku", "quantity", "unit_price"])
    return [
        OrderLine(sku=row["sku"], quantity=int(row["quantity"]), unit_price=float(row["unit_price"]))
        for row in rows
    ]
