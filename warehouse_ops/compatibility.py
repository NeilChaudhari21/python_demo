"""Runtime and environment helpers."""

import locale
import pkgutil
import platform

try:
    from collections import Mapping
except ImportError:
    from collections.abc import Mapping


def is_mapping(value) -> bool:
    return isinstance(value, Mapping)


def default_locale_name() -> str:
    language, encoding = locale.getdefaultlocale()
    if language and encoding:
        return "%s.%s" % (language, encoding)
    return language or "unknown"


def can_load_module(module_name: str) -> bool:
    return pkgutil.find_loader(module_name) is not None


def platform_distribution_name() -> str:
    return platform.system()
