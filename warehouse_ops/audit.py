"""Audit log formatting."""

from datetime import datetime
from typing import Dict


def audit_timestamp() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def format_audit_log(action: str, actor: str, details: Dict[str, object]) -> str:
    detail_text = "; ".join(f"{key}={value}" for key, value in sorted(details.items()))
    return f"[{audit_timestamp()}] actor={actor} action={action} {detail_text}"
