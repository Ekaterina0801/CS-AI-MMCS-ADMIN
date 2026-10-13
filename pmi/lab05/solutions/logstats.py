"""Образцовое решение практики lab05 (ПМИ): Текстовые файлы.

Сгенерировано из tests/reference_lib.py. Студентам не выдаётся — это эталон
для проверки того, что задание собрано согласованно.
"""
from __future__ import annotations


def parse_event(line: str) -> dict:
    """Строка журнала «время уровень сообщение» в словарь. Негодная строка — ValueError."""
    levels = ("DEBUG", "INFO", "WARNING", "ERROR")
    parts = line.strip().split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("В строке журнала должны быть время, уровень и сообщение")
    time, level, message = parts
    if level not in levels:
        raise ValueError(f"Неизвестный уровень «{level}»")
    return {"time": time, "level": level, "message": message.strip()}


def count_levels(lines: list[str]) -> dict:
    """Сколько строк каждого уровня. Негодные строки считаются под ключом BROKEN."""
    counts: dict[str, int] = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            level = parse_event(line)["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines: list[str], n: int) -> list[list]:
    """n самых частых сообщений уровня ERROR: пары «сообщение, сколько раз».

    При равной частоте — в алфавитном порядке сообщения.
    """
    counts: dict[str, int] = {}
    for line in lines:
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            counts[event["message"]] = counts.get(event["message"], 0) + 1
    ordered = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return [[message, count] for message, count in ordered[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    """Текст отчёта: строки «уровень: количество» и список частых ошибок."""
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    for message, count in errors:
        lines.append(f"- {message} — {count}")
    return "\n".join(lines) + "\n"
