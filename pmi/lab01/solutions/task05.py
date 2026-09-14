a = int(input())
b = int(input())
# третья переменная хранит исходное значение a, иначе оно потеряется
temp = a
a = b
b = temp
print(a)
print(b)
