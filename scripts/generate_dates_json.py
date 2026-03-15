#!/usr/bin/env python3
"""Generate dates-map.json from dated Python files in month folders."""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

RE_DATE_FILE = re.compile(r"^(\d{2})-(\d{2})-(\d{4})(?:\s*-\s*([A-Za-z]+))?\.py$")
MONTH_FOLDERS = {
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
}


def _format_date(day: int, month: int, year: int) -> str:
    return f"{day}/{month:02d}/{year}"


def _normalize_label(raw_label: str | None) -> str:
    if not raw_label:
        return "Assignment"
    return raw_label.strip().title()


def build_mapping(repo_root: Path) -> dict[str, dict[str, list[str]]]:
    mapping: dict[str, dict[str, list[str]]] = {}

    for folder in sorted(p for p in repo_root.iterdir() if p.is_dir()):
        if folder.name.lower() not in MONTH_FOLDERS:
            continue

        parsed_dates: dict[str, list[tuple[int, int, int]]] = {
            "Assignment": [],
            "Task": [],
        }
        for file in folder.glob("*.py"):
            match = RE_DATE_FILE.match(file.name)
            if not match:
                continue

            day, month, year = map(int, match.groups()[:3])
            label = _normalize_label(match.group(4))
            parsed_dates.setdefault(label, []).append((year, month, day))

        if not any(parsed_dates.values()):
            continue

        month_payload: dict[str, list[str]] = {}
        for label in sorted(parsed_dates):
            rows = parsed_dates[label]
            rows.sort()
            month_payload[label] = [
                _format_date(day=day, month=month, year=year)
                for year, month, day in rows
            ]

        mapping[folder.name] = month_payload

    return mapping


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    output_file = repo_root / "dates-map.json"

    payload = {
        "generatedOn": date.today().isoformat(),
        "folders": build_mapping(repo_root),
    }

    output_file.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {output_file.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
