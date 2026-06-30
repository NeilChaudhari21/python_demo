"""String normalization helpers."""


def slugify(value: str) -> str:
    parts = value.strip().lower().replace("_", "-").split()
    return "-".join(parts)


def compact_whitespace(value: str) -> str:
    return " ".join(value.split())
