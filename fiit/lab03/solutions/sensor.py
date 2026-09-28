threshold = float(input())
count = int(input())
errors = 0
above = 0
total = 0.0
valid = 0
maximum = None
for _ in range(count):
    line = input().strip()
    if line == "error":
        errors += 1
        continue
    value = float(line)
    valid += 1
    total += value
    if value > threshold:
        above += 1
    if maximum is None or value > maximum:
        maximum = value
print(count)
print(errors)
print(above)
print(f"{maximum:.1f}")
print(f"{total / valid:.1f}")
