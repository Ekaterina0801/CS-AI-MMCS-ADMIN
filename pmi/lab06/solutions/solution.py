"""Образцовое решение практики lab06 (ПМИ): Файловая система в Python.

Сгенерировано из tests/reference_lib.py. Студентам не выдаётся — это эталон
для проверки того, что задание собрано согласованно.
"""
from __future__ import annotations


def count_by_extension(paths: list[str]) -> dict[str, int]:
    """Сколько файлов каждого расширения. Расширение — в нижнем регистре, без точки."""
    counts: dict[str, int] = {}
    for path in paths:
        name = path.rstrip("/").split("/")[-1]
        ext = name.rsplit(".", 1)[1].lower() if "." in name[1:] else ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    """Путь с наибольшей вложенностью. При равенстве — первый по алфавиту."""
    if not paths:
        return ""
    return sorted(paths, key=lambda p: (-p.strip("/").count("/"), p))[0]


def human_size(n_bytes: int) -> str:
    """Размер в удобных единицах: 1536 -> «1.5 КБ». Один знак после запятой."""
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.1f} {unit}" if unit != "Б" else f"{int(size)} {unit}"
        size /= 1024
    return f"{size:.1f} ТБ"
