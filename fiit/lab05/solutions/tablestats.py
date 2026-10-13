"""Образцовое решение практики lab05 (ФИИТ): Работа с файлами и табличными записями.

Сгенерировано из tests/reference_lib.py. Студентам не выдаётся — это эталон
для проверки того, что задание собрано согласованно.
"""
from __future__ import annotations


def read_rows(lines: list[str]) -> list[dict]:
    """Разбирает CSV с заголовком в список словарей. Пустые и короткие строки пропускаются."""
    rows: list[dict] = []
    header: list[str] = []
    for line in lines:
        if not line.strip():
            continue
        cells = [cell.strip() for cell in line.split(",")]
        if not header:
            header = cells
            continue
        if len(cells) != len(header):
            continue
        rows.append(dict(zip(header, cells)))
    return rows


def count_types(rows: list[dict]) -> dict:
    """Сколько записей каждого типа."""
    counts: dict[str, int] = {}
    for row in rows:
        kind = row.get("тип", "")
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    """Суммарная длительность записей одного типа, округлённая до десятых."""
    total = 0.0
    for row in rows:
        if row.get("тип") != kind:
            continue
        try:
            total += float(row.get("минуты", "").replace(",", "."))
        except ValueError:
            continue
    return round(total, 1)


def to_csv(counts: dict) -> str:
    """Сводка «тип,количество» с заголовком, строки по алфавиту типа."""
    lines = ["тип,количество"]
    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"
