"""Application-specific exceptions."""


class WarehouseOpsError(Exception):
    """Base exception for warehouse operations errors."""


class ValidationError(WarehouseOpsError):
    """Raised when input data fails validation."""


class InventoryError(WarehouseOpsError):
    """Raised for invalid inventory operations."""


class DataLoadError(WarehouseOpsError):
    """Raised when a file cannot be loaded into application records."""
