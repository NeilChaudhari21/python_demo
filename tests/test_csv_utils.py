from warehouse_ops.csv_utils import parse_csv_text, require_columns, rows_to_csv


def test_csv_parse_and_write():
    rows = parse_csv_text("sku,name\nSKU-1001,Tape\n")
    assert rows == [{"sku": "SKU-1001", "name": "Tape"}]
    require_columns(rows, ["sku", "name"])
    assert rows_to_csv(rows, ["sku", "name"]) == "sku,name\nSKU-1001,Tape\n"
