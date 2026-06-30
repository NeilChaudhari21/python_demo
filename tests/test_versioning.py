from warehouse_ops.versioning import compare_catalog_versions, diff_supplier_catalogs, is_catalog_newer


def test_catalog_version_comparison():
    assert compare_catalog_versions("2024.9", "2024.10") == -1
    assert compare_catalog_versions("2024.10", "2024.10") == 0
    assert is_catalog_newer("2025.1", "2024.12")


def test_supplier_catalog_diff():
    old = {"sup-001": "2024.8", "sup-002": "2024.7"}
    new = {"sup-001": "2024.10", "sup-002": "2024.7", "sup-003": "1.0"}

    assert diff_supplier_catalogs(old, new) == {
        "sup-001": ("2024.8", "2024.10"),
        "sup-003": (None, "1.0"),
    }
