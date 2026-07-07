"""Audit log formatting."""

from datetime import datetime, timezone
from typing import Dict


def audit_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat() + "Z"


def format_audit_log(action: str, actor: str, details: Dict[str, object]) -> str:
    detail_text = "; ".join("%s=%s" % (key, value) for key, value in sorted(details.items()))
    return "[%s] actor=%s action=%s %s" % (audit_timestamp(), actor, action, detail_text)
