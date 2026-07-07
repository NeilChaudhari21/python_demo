"""Runtime and environment helpers."""

import importlib.util
import locale
import platform

from collections.abc import Mapping


def is_mapping(value) -> bool:
    return isinstance(value, Mapping)


def default_locale_name() -> str:
    language, encoding = locale.getlocale()
    if language and encoding:
        return "%s.%s" % (language, encoding)
    return language or "unknown"


def can_load_module(module_name: str) -> bool:
    spec = importlib.util.find_spec(module_name)
    return spec is not None


def platform_distribution_name() -> str:
    dist = getattr(platform, "dist", None)
    if dist is None:
        return platform.system()
    result = dist()
    return " ".join(part for part in result if part)
