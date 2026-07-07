"""Date and time formatting helpers."""

from datetime import datetime, timedelta, timezone


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat() + "Z"


def days_from_now(days: int) -> datetime:
    return datetime.now(timezone.utc) + timedelta(days=days)


def parse_yyyymmdd(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d")
