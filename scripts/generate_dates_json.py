#!/usr/bin/env python3
"""Generate dates-map.json from dated Python files in month folders."""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

RE_DATE_FILE = re.compile(r"^(\d{2})-(\d{2})-(\d{4})\.py$")
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


def build_mapping(repo_root: Path) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}

    for folder in sorted(p for p in repo_root.iterdir() if p.is_dir()):
        if folder.name.lower() not in MONTH_FOLDERS:
            continue

        parsed_dates: list[tuple[int, int, int]] = []
        for file in folder.glob("*.py"):
            match = RE_DATE_FILE.match(file.name)
            if not match:
                continue

            day, month, year = map(int, match.groups())
            parsed_dates.append((year, month, day))

        if not parsed_dates:
            continue

        parsed_dates.sort()
        mapping[folder.name] = [
            _format_date(day=day, month=month, year=year)
            for year, month, day in parsed_dates
        ]

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
