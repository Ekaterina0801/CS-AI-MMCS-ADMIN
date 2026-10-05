"""Образцовое решение практики lab04 (ФИИТ): Функции и списки.

Сгенерировано из tests/reference_lib.py. Студентам не выдаётся — это эталон
для проверки того, что задание собрано согласованно.
"""
from __future__ import annotations


def winner(names: list[str], scores: list[float]) -> str:
    """Имя участника с наибольшим результатом. При равенстве — тот, кто раньше в списке."""
    best = 0
    for i in range(1, len(names)):
        if scores[i] > scores[best]:
            best = i
    return names[best]


def average(scores: list[float]) -> float:
    """Средний результат, округлённый до сотых. Для пустого списка — 0.0."""
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def ranking(names: list[str], scores: list[float]) -> list[str]:
    """Имена по убыванию результата. При равенстве — в исходном порядке."""
    order = sorted(range(len(names)), key=lambda i: -scores[i])
    return [names[i] for i in order]


def above_average(names: list[str], scores: list[float]) -> list[str]:
    """Имена тех, чей результат строго выше среднего. Порядок — как в списке."""
    mean = average(scores)
    return [name for name, score in zip(names, scores) if score > mean]
