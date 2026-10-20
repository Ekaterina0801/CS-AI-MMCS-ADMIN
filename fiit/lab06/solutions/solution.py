"""Образцовое решение практики lab06 (ФИИТ): Словари и множества.

Сгенерировано из tests/reference_lib.py. Студентам не выдаётся — это эталон
для проверки того, что задание собрано согласованно.
"""
from __future__ import annotations


def count_items(values: list) -> dict:
    """Сколько раз встречается каждое значение."""
    counts: dict = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


def unique_sorted(values: list) -> list:
    """Уникальные значения по возрастанию."""
    return sorted(set(values))


def common(first: list, second: list) -> list:
    """Значения, которые есть в обоих списках, по возрастанию."""
    return sorted(set(first) & set(second))


def only_in_first(first: list, second: list) -> list:
    """Значения, которые есть в первом списке и отсутствуют во втором, по возрастанию."""
    return sorted(set(first) - set(second))
