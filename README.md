# Warehouse Ops Toolkit

Warehouse Ops Toolkit is a small command-line and library-style utility for product, supplier, order, shipment, and inventory workflows in a warehouse operations team.

It provides helpers for stock adjustments, reorder alerts, supplier catalog comparison, purchase order totals, CSV imports, audit log formatting, and simple inventory reports.

## Requirements

- Python 3.14
- pip

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

## CLI Usage

Generate an inventory report from product and supplier CSV files:

```bash
warehouse-ops report --products examples/sample_products.csv --suppliers examples/sample_suppliers.csv
```

Check reorder alerts:

```bash
warehouse-ops reorder-alerts --products examples/sample_products.csv
```

## Library Usage

```python
from warehouse_ops.inventory import InventoryLedger
from warehouse_ops.models import Product

ledger = InventoryLedger()
product = Product("SKU-1001", "Packing Tape", "sup-001", 4.25, reorder_point=25, quantity_on_hand=12)
ledger.add_product(product)

alerts = ledger.reorder_alerts()
```

## Testing

```bash
pip install -r requirements.txt
pytest -v
```

## Project Layout

The `warehouse_ops` package contains the application modules. The `examples` directory provides small CSV files that can be used with the CLI and tests.