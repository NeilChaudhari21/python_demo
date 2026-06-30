"""CSV parsing helpers."""

import csv
from io import StringIO
from typing import Dict, Iterable, List


def parse_csv_text(text: str) -> List[Dict[str, str]]:
    reader = csv.DictReader(StringIO(text))
    return [dict(row) for row in reader]


def rows_to_csv(rows: Iterable[Dict[str, object]], fieldnames: List[str]) -> str:
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    return output.getvalue()


def require_columns(rows: List[Dict[str, str]], required: Iterable[str]) -> None:
    if not rows:
        return
    missing = set(required) - set(rows[0].keys())
    if missing:
        raise ValueError("CSV missing required columns: %s" % ", ".join(sorted(missing)))
