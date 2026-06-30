import pytest

from warehouse_ops.exceptions import ValidationError
from warehouse_ops.validators import validate_quantity, validate_sku


def test_validate_sku_normalizes_valid_values():
    assert validate_sku(" sku-1001 ") == "SKU-1001"


def test_validate_sku_rejects_bad_values():
    with pytest.raises(ValidationError):
        validate_sku("no")


def test_validate_quantity():
    assert validate_quantity(0) == 0
    with pytest.raises(ValidationError):
        validate_quantity(-1)
