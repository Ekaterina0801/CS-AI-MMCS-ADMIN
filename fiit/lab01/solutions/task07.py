number = int(input())
thousands = number // 1000
hundreds = number // 100 % 10
tens = number // 10 % 10
units = number % 10
print(thousands)
print(hundreds)
print(tens)
print(units)
print(thousands + hundreds + tens + units)
print(units * 1000 + tens * 100 + hundreds * 10 + thousands)
