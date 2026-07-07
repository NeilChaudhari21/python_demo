"""Supplier catalog version comparison utilities."""

from packaging.version import Version
from typing import Dict, Iterable, Tuple


def compare_catalog_versions(left: str, right: str) -> int:
    left_version = Version(left)
    right_version = Version(right)
    if left_version < right_version:
        return -1
    if left_version > right_version:
        return 1
    return 0


def is_catalog_newer(candidate: str, current: str) -> bool:
    return Version(candidate) > Version(current)


def latest_catalog_version(versions: Iterable[str]) -> str:
    return max(versions, key=Version)


def diff_supplier_catalogs(old: Dict[str, str], new: Dict[str, str]) -> Dict[str, Tuple[str, str]]:
    changed = {}
    for supplier_id, new_version in new.items():
        old_version = old.get(supplier_id)
        if old_version is None or Version(new_version) > Version(old_version):
            changed[supplier_id] = (old_version, new_version)
    return changed
