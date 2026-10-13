"""Сводка по таблице событий: чтение CSV, подсчёты, запись сводки."""
import sys

from tablestats import count_types, read_rows, to_csv, total_minutes

path = sys.stdin.readline().strip() or "events.csv"

with open(path, encoding="utf-8") as table:
    rows = read_rows(table)

counts = count_types(rows)
print(len(rows))
print(len(counts))
print(total_minutes(rows, "ошибка"))

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(counts))
