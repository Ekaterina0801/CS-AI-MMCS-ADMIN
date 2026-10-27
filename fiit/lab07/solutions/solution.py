"""Образцовое решение практики lab07 (ФИИТ): NumPy I.

Сгенерировано из tests/reference_lib.py. Студентам не выдаётся — это эталон
для проверки того, что задание собрано согласованно.
"""
from __future__ import annotations

import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    """Плоский список измерений в таблицу по width значений в строке.

    Если длина не делится на ширину нацело, возвращается пустой список:
    форма должна совпадать с данными, иначе это ошибка в самих данных.
    """

    if width <= 0 or not values or len(values) % width:
        return []
    arr = np.asarray(values, dtype="float64").reshape(-1, width)
    return [[round(float(v), 6) for v in row] for row in arr]


def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    """Участок таблицы: строки rows и столбцы columns в указанном порядке."""

    arr = np.asarray(matrix, dtype="float64")
    if arr.size == 0 or not rows or not columns:
        return []
    picked = arr[np.ix_(rows, columns)]
    return [[round(float(v), 6) for v in row] for row in picked]


def column_means(matrix: list[list[float]]) -> list[float]:
    """Среднее по каждому столбцу. Результат округляется до шести знаков."""

    if not matrix:
        return []
    return [round(float(v), 6) for v in np.asarray(matrix, dtype="float64").mean(axis=0)]


def column_range(matrix: list[list[float]], column: int) -> float:
    """Размах значений в столбце: разница наибольшего и наименьшего, до шести знаков."""

    arr = np.asarray(matrix, dtype="float64")
    if arr.size == 0:
        return 0.0
    values = arr[:, column]
    return round(float(values.max() - values.min()), 6)
