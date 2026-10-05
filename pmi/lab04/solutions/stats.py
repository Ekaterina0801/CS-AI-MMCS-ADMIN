"""Образцовое решение практики lab04 (ПМИ): Повторение Python для обработки данных.

Сгенерировано из tests/reference_lib.py. Студентам не выдаётся — это эталон
для проверки того, что задание собрано согласованно.
"""
from __future__ import annotations


def parse_record(line: str) -> dict:
    """Разбирает строку «город;температура;дата» в словарь. Негодная строка — ValueError."""
    parts = [part.strip() for part in line.split(";")]
    if len(parts) != 3:
        raise ValueError(f"Нужно три поля через «;», получено {len(parts)}")
    city, raw_temp, date = parts
    if not city or not date:
        raise ValueError("Город и дата не могут быть пустыми")
    try:
        temperature = float(raw_temp.replace(",", "."))
    except ValueError:
        raise ValueError(f"Температура «{raw_temp}» не число") from None
    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    """Разбирает строки журнала, пропуская пустые и негодные."""
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records


def average_by_city(records: list[dict]) -> dict:
    """Средняя температура по каждому городу, округлённая до десятых."""
    totals: dict[str, float] = {}
    counts: dict[str, int] = {}
    for record in records:
        city = record["city"]
        totals[city] = totals.get(city, 0.0) + record["temperature"]
        counts[city] = counts.get(city, 0) + 1
    return {city: round(totals[city] / counts[city], 1) for city in totals}


def warmest_city(records: list[dict]) -> str:
    """Город с наибольшей средней температурой. При равенстве — первый по алфавиту."""
    means = average_by_city(records)
    if not means:
        return ""
    return sorted(means, key=lambda city: (-means[city], city))[0]
