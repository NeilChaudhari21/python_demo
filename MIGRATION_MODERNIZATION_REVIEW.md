# Migration and Modernization Review

## Manual Review Compatibility Items

### MRC-001: Replace StrictVersion in suppliers with behavior validation
- File: `warehouse_ops/suppliers.py`
- Issue: The module imports `StrictVersion` from `distutils.version`, which is unavailable in Python 3.14.
- Reason Not Automated: Although `packaging` is already declared, version comparison behavior may differ from `StrictVersion`. The assessment does not provide tests for `warehouse_ops/suppliers.py`, so automatic replacement could alter accepted/rejected version strings.
- Suggested Next Step: Review `validate_supplier_api_version` semantics, decide whether `packaging.version.Version` or `packaging.version.parse` preserves the intended contract, and add or run supplier-version regression tests before implementation.

### MRC-002: Replace LooseVersion in versioning with behavior validation
- File: `warehouse_ops/versioning.py`
- Issue: The module imports `LooseVersion` from `distutils.version`, which is unavailable in Python 3.14.
- Reason Not Automated: `LooseVersion` and `packaging.version` do not necessarily interpret non-standard version strings identically. This module performs multiple catalog comparisons and has behavior-sensitive ordering logic.
- Suggested Next Step: Review expected catalog version formats, compare them against `tests/test_versioning.py`, and validate whether a `packaging`-based replacement preserves ordering and equality behavior before implementation.

### MRC-003: Replace locale.getdefaultlocale with environment-aware logic
- File: `warehouse_ops/compatibility.py`
- Issue: `default_locale_name()` uses `locale.getdefaultlocale()`, which is deprecated and environment-sensitive.
- Reason Not Automated: Locale resolution semantics can vary by platform and environment variables. The intended fallback behavior is not fully specified by tests in the assessment.
- Suggested Next Step: Review intended locale behavior across supported environments and replace with a supported API only after validating equivalent output expectations.

### MRC-004: Replace platform.dist logic with supported distribution detection
- File: `warehouse_ops/compatibility.py`
- Issue: `platform_distribution_name()` relies on `platform.dist`, which is removed from modern Python versions.
- Reason Not Automated: OS/distribution detection is environment-specific, and replacement choices can materially change output. The assessment does not show tests for this behavior, and no new dependency should be introduced by default.
- Suggested Next Step: Review the actual consumer expectations for this helper and choose a supported platform detection strategy, preferring standard library APIs when sufficient. Add targeted tests before implementation.

### MRC-005: Replace imp.load_source with importlib plugin loading
- File: `warehouse_ops/plugin_loader.py`
- Issue: The module uses `imp.load_source` for dynamic plugin loading.
- Reason Not Automated: Dynamic import behavior can be sensitive to module naming, loader state, and plugin side effects. The assessment does not provide tests or plugin examples to prove equivalence of an `importlib` replacement.
- Suggested Next Step: Review current plugin-loading expectations, identify real plugin files or callers, and then implement an `importlib`-based loader with targeted validation of loaded module identity and hook execution.

### MRC-006: Review datetime.utcnow modernization sites for semantic expectations
- File: `warehouse_ops/audit.py`
- Issue: `audit_timestamp()` uses `datetime.utcnow()`.
- Reason Not Automated: This is modernization rather than a required Python 3.14 fix, and timezone-aware replacements can subtly change object semantics or formatting expectations.
- Suggested Next Step: Review whether maintainers want to preserve the current naive-UTC pattern or move to timezone-aware datetime generation, then validate exact timestamp formatting expectations.

### MRC-007: Review documentation and version-support messaging after 3.14 validation
- File: `README.md`
- Issue: The README documents Python 3.10 as the requirement.
- Reason Not Automated: Documentation should only be updated after actual Python 3.14 validation is confirmed. The assessment states tests were not run, so support must not be overstated yet.
- Suggested Next Step: After successful Python 3.14 validation, update README language to reflect confirmed support and installation/testing instructions.

### MRC-008: Verify declared dependency compatibility with Python 3.14
- File: `requirements.txt`
- Issue: Declared dependencies `pytest==7.4.0`, `packaging>=23.0`, `python-dateutil==2.8.2`, and `tabulate==0.9.0` have unknown / manual_review compatibility status for Python 3.14 per the assessment. Build environment support through setuptools in `pyproject.toml` also requires verification.
- Reason Not Automated: The assessment explicitly marks dependency compatibility as unknown / manual_review, and no upstream compatibility evidence is provided. Dependency upgrades are not approved by default.
- Suggested Next Step: Verify Python 3.14 support using upstream project documentation or release notes before recommending any dependency version changes. Keep `pyproject.toml` and `setup.cfg` aligned if future dependency or metadata changes are needed.

## Manual Review Modernization Items

### MRM-001: Review datetime.utcnow modernization across utility/reporting modules
- Files:
  - `warehouse_ops/utils/dates.py`
  - `warehouse_ops/reporting.py`
- Issue: These files contain `datetime.utcnow()` usage identified by the assessment as a discouraged pattern.
- Reason Not Automated: Timezone-aware replacements may affect formatting, object semantics, or downstream expectations. The assessment does not provide enough evidence to automate these changes safely.
- Suggested Next Step: Evaluate whether a timezone-aware replacement is desired and verify that any change preserves formatting and downstream behavior.

## Dependency Compatibility Items Requiring Review

- `packaging>=23.0`
- `pytest==7.4.0`
- `python-dateutil==2.8.2`
- `tabulate==0.9.0`
- `setuptools` build environment support for Python 3.14

## Validation Recommendations

- Run `python -m compileall .`
- Run `python -m pytest`
- Run `python3.14 -m compileall .`
- Run `python3.14 -m pytest -v`
- Run `tox -e py314`

- Focus validation on:
  - `tests/test_csv_utils.py`
  - `tests/test_data_loader.py`
  - `tests/test_inventory.py`
  - `tests/test_orders.py`
  - `tests/test_reporting.py`
  - `tests/test_validators.py`
  - `tests/test_versioning.py`

- Confirm manually that:
  - `warehouse_ops/compatibility.py` locale and platform helpers still meet intended expectations before any future manual-review changes
  - `warehouse_ops/suppliers.py` and `warehouse_ops/versioning.py` receive behavior-preserving replacements for removed `distutils.version` APIs
  - `warehouse_ops/plugin_loader.py` is migrated to `importlib` only after validating plugin-loading semantics
  - README and support messaging are updated only after Python 3.14 validation is confirmed