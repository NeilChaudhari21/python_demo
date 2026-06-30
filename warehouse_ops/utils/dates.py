"""Date and time formatting helpers."""

from datetime import datetime, timedelta


def utc_now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def days_from_now(days: int) -> datetime:
    return datetime.utcnow() + timedelta(days=days)


def parse_yyyymmdd(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d")
