"""Plain-text templates used by reporting helpers."""

INVENTORY_HEADER = "SKU,Name,On Hand,Reorder Point,Location"
REORDER_HEADER = "SKU,Name,On Hand,Reorder Point"


def format_inventory_row(product) -> str:
    return "%s,%s,%d,%d,%s" % (
        product.sku,
        product.name,
        product.quantity_on_hand,
        product.reorder_point,
        product.location,
    )
