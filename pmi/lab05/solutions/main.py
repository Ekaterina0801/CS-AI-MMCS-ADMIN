"""Отчёт по журналу событий: чтение файла, подсчёты, запись отчёта."""
import sys

from logstats import count_levels, format_report, top_errors

path = sys.stdin.readline().strip() or "events.log"

# файл читается построчно и дважды: целиком в память он не попадает
with open(path, encoding="utf-8") as log:
    counts = count_levels(log)
with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

print(sum(counts.values()))
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

with open("report.txt", "w", encoding="utf-8") as out:
    out.write(format_report(counts, errors))
