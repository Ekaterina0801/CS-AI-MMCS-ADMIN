"""Образцовое решение практики lab07 (ПМИ): Форматы хранения данных.

Сгенерировано из tests/reference_lib.py. Студентам не выдаётся — это эталон
для проверки того, что задание собрано согласованно.
"""
from __future__ import annotations

import json

def csv_to_records(text: str) -> list[dict]:
    """Разбирает CSV с заголовком в список словарей. Значения остаются строками."""
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return []
    header = [c.strip() for c in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        cells = [c.strip() for c in line.split(",")]
        records.append({key: cells[i] if i < len(cells) else "" for i, key in enumerate(header)})
    return records


def _typed(text: str):
    """Строка из файла настроек в число, логическое значение или строку."""
    lowered = text.strip().strip('"\'')
    if lowered.lower() in ("true", "yes"):
        return True
    if lowered.lower() in ("false", "no"):
        return False
    try:
        return int(lowered)
    except ValueError:
        pass
    try:
        return float(lowered.replace(",", "."))
    except ValueError:
        return lowered


def parse_settings(lines: list[str]) -> dict:
    """Простой YAML: «ключ: значение», списки через «- », комментарии после #.

    Значения приводятся к типам: 12 — число, 3.5 — дробное, true/false — логическое,
    остальное остаётся строкой. Вложенность не поддерживается: формат учебный.
    """
    settings: dict = {}
    current_list: str | None = None
    for raw in lines:
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if line.lstrip().startswith("- ") and current_list:
            settings[current_list].append(_typed(line.lstrip()[2:].strip()))
            continue
        key, separator, value = line.partition(":")
        if not separator:
            continue
        key, value = key.strip(), value.strip()
        if not value:
            settings[key] = []
            current_list = key
        else:
            settings[key] = _typed(value)
            current_list = None
    return settings


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    """Дополняет записи сведениями из словаря по значению ключа key.

    Записи без пары остаются как есть; поля записи не затираются данными из extra.
    """
    merged: list[dict] = []
    for row in rows:
        addition = extra.get(str(row.get(key, "")), {})
        combined = dict(addition)
        combined.update(row)
        merged.append(combined)
    return merged


def records_to_json(records: list[dict]) -> str:
    """Список словарей в JSON: отступ 2, ключи по алфавиту, кириллица как есть."""
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
