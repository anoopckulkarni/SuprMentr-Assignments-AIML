#!/usr/bin/env python3
"""Generate dates-map.xml from dated files/folders in month folders."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

RE_DATE_LABEL = re.compile(r"^(\d{2})-(\d{2})-(\d{4})(?:\s*-\s*([A-Za-z]+))?$")
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


def _parse_dated_name(raw_name: str) -> tuple[int, int, int, str] | None:
    match = RE_DATE_LABEL.match(raw_name)
    if not match:
        return None

    day, month, year = map(int, match.groups()[:3])
    label = _normalize_label(match.group(4))
    return year, month, day, label


def build_mapping(repo_root: Path) -> dict[str, dict[str, list[str]]]:
    mapping: dict[str, dict[str, list[str]]] = {}

    for folder in sorted(p for p in repo_root.iterdir() if p.is_dir()):
        if folder.name.lower() not in MONTH_FOLDERS:
            continue

        parsed_dates: dict[str, list[tuple[int, int, int]]] = {
            "Assignment": [],
            "Task": [],
        }
        for child in folder.iterdir():
            parsed: tuple[int, int, int, str] | None = None
            if child.is_file() and child.suffix.lower() == ".py":
                parsed = _parse_dated_name(child.stem)
            elif child.is_dir():
                parsed = _parse_dated_name(child.name)

            if not parsed:
                continue

            year, month, day, label = parsed
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


def _build_xml(mapping: dict[str, dict[str, list[str]]]) -> ET.Element:
    root = ET.Element("root")
    generated_on = ET.SubElement(root, "generatedOn")
    generated_on.text = date.today().isoformat()

    folders_node = ET.SubElement(root, "folders")
    for month_name, labels in mapping.items():
        month_node = ET.SubElement(folders_node, month_name)
        for label, dates in labels.items():
            for date_value in dates:
                label_node = ET.SubElement(month_node, label)
                label_node.text = date_value

    return root


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    output_file = repo_root / "dates-map.xml"

    root = _build_xml(build_mapping(repo_root))
    ET.indent(root, space="    ")
    xml_content = ET.tostring(root, encoding="unicode")
    output_file.write_text(
        "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n" + xml_content + "\n",
        encoding="utf-8",
    )
    print(f"Updated {output_file.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
