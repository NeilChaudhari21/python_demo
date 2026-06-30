from warehouse_ops.data_loader import load_order_lines, load_products, load_suppliers


def test_load_products_from_csv(tmp_path):
    path = tmp_path / "products.csv"
    path.write_text(
        "sku,name,supplier_id,unit_cost,reorder_point,quantity_on_hand,location\n"
        "SKU-1001,Tape,sup-001,4.25,20,12,A1\n"
    )

    products = load_products(str(path))
    assert products[0].sku == "SKU-1001"
    assert products[0].quantity_on_hand == 12


def test_load_suppliers_from_csv(tmp_path):
    path = tmp_path / "suppliers.csv"
    path.write_text("supplier_id,name,discount_rate,api_version,catalog_version\nsup-001,North,0.05,1.2,2024.10\n")

    suppliers = load_suppliers(str(path))
    assert suppliers[0].discount_rate == 0.05


def test_load_order_lines_from_csv(tmp_path):
    path = tmp_path / "orders.csv"
    path.write_text("sku,quantity,unit_price\nSKU-1001,2,4.25\n")

    lines = load_order_lines(str(path))
    assert lines[0].subtotal() == 8.5
