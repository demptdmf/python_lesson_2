'''

a = input('Введите значение числа a: ')
b = input('Введите значение числа b: ')

a = int(a)
b = int(b)
print('Ниже приведены результаты математических операций:')
print('a + b = ', a + b,)
print('a - b = ', a - b,)
print('a / b = ', a / b,)
print('a * b = ', a * b,)
print('a ** b = ', a ** b,)     # Возведение в степень
print('a // b = ', a // b,)     # Целочисленное деление
print('a % b = ', a % b,)     # Остаток от деления

# Логические операции
a = True
b = False

# Отрицание
print(not a)

# Логическое И
print(a and b)

# Логическое ИЛИ
print(a or b)

'''

a = int(input('and input A number: '))       # Сразу присваиваем тип "Целое число" + вводим число
print()
if a < 100: print('Your A less than 100')
else: print('Your A more than 100 :)')
print()
print('a > 100 — значение ', a > 100)
print('a < 100 — значение ', a < 100)
print('a >= 100 — значение ', a >= 100)
print('a <= 100 — значение ', a <= 100)
print('a = 100 — значение ', a == 100)
print('a != 100 (не равно) — значение ', a != 100)
