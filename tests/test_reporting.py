from warehouse_ops.models import Product
from warehouse_ops.reporting import generate_inventory_report, generate_reorder_report, summarize_inventory


def test_inventory_report_contains_products_and_summary():
    products = [
        Product("SKU-1001", "Tape", "sup-001", 4.25, reorder_point=20, quantity_on_hand=12, location="A1")
    ]

    report = generate_inventory_report(products)
    assert "SKU,Name,On Hand,Reorder Point,Location" in report
    assert "SKU-1001,Tape,12,20,A1" in report
    assert summarize_inventory(products) == {"product_count": 1, "total_units": 12, "total_value": 51.0}


def test_reorder_report_filters_products():
    products = [
        Product("SKU-1001", "Tape", "sup-001", 4.25, reorder_point=20, quantity_on_hand=12),
        Product("SKU-1002", "Mailer", "sup-001", 0.85, reorder_point=20, quantity_on_hand=50),
    ]

    report = generate_reorder_report(products)
    assert "SKU-1001" in report
    assert "SKU-1002" not in report
