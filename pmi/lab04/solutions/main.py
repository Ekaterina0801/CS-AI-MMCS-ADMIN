"""Отчёт по журналу наблюдений: разбор входа и печать итогов."""
import sys

from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
records = read_valid(lines)
# пустые строки не ошибка: их не считаем ни тем, ни другим
skipped = sum(1 for line in lines if line.strip()) - len(records)

print(len(records))
print(skipped)
means = average_by_city(records)
if means:
    print(f"{means[warmest_city(records)]:.1f}")
else:
    print("0.0")
