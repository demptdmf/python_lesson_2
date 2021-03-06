# Задачи на циклы и оператор условия------
# ----------------------------------------
#
# '''
# Задача 1
# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
# '''
# print('Задача 1. Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.')
# n = 0
# line = int(input('Введите количество строк для нумерации: '))
# if line > 0:
#     for i in range(1, line + 1):
#         n = n + 1
#         print(n, '0000000000')
#     print()
# else:
#     print('Число строк должно быть больше 0')
#
#
# # ——————————— ВОПРОС К №1 ———————————
# # Решил сделать ручную возможность ввода количества необходимых строчек.
# # 1. Но пока не знаю как сделать условие, чтобы число было только положительное такое условие не помогает:
# #    if line >= 0: — на 11 строку
# #    else: print('Число строк должно быть больше 0') — на 14 строку
# # 2. При этом else показывается, если даже line > 0. Выводится и ответ, и еррор.
#
# # Вот код строго для 5 строчек по заданию:
# # n = 0
# # for i in range(1, 6):
# #     n = n + 1
# #     print(n, '0000000000')
#
# '''
# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
# '''
# print('Задача 2. Найти количество введеных пользователем цифр 5')
# count = 0
# for i in range(10):
#     n = int(input('Введите число: '))
#     if n == 5:                                  # если число равно 5,
#         count += 1                              # увеличиваем счетчик на +1
# print('Ответ:', count)
# print()
#
# # ——————————— ВОПРОС К №2 ———————————
# # 1. Считается наличие 5ки в самой строчки, но  не считается количество 5ки в строчке. Памагите :)
#
# # 2я задача обратите внимание на условие, мы вводим не число а цифры в цикле(т.е от 0 до 9),
# # так что операции с дроблением числа избыточны, достаточно if n == 5:
#
# '''
# Задача 3
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
# '''
# print('Задача 3. Найти сумму ряда чисел от 1 до 100.')
# sum = 0
# for i in range(1,101):          # 1. Для ряда числе от 1 до 100
#     sum += i                    # 2. Производить суммы каждого числа друг с другом: 0 (это sum) +1+2+3..+100 (это range)
# print('Ответ:', sum)
# print()
#
# '''
# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
# '''
# print('Задача 4. Найти произведение ряда чисел от 1 до 10.')
#
# n = 1                           # 1. Создаем переменную для результата.
# for i in range(1,11):           # 2. Для ряда числе i в диапазоне от 1 до 10
#     n *= i                      # 3. Умножать переменную (1) на числа в диапазоне до 10. 1*1=1, далее N=1*2=2, 2*3=6, 6*4=24, 24*5=120 ит.д. (цикл повторяется и каждый раз N становится тем числом, которое мы получили до этого после умножения.
# print('Ответ:', n)
# print()
#
#
# '''Задача 5
# Вывести цифры числа на каждой строчке.
# '''
# print('Задача 5. Вывести цифры числа на каждой строчке.')
# n = int(input('Напишите число: '))
#
# while n > 0:                        # 1. Открываем цикл, когда число больше 0
#     print(n % 10)                   # 2. Выводим остаток от деления N на 10 ("последняя цифра" или "цифра после запятой", 4)
#     n = n // 10                     # 3. Отрезаем последюю цифру. Выводим количество десятков (123), после чего снова выводим остаток из п2 (3). Снова отрезаем этот остаток, получаем десятки (12) и остаток (2) итд
# print()                             # На каждой строке — оно само так делается?) Ведь в коде нет для этого ничего, просто цифру делим и выводим целые
#
# '''
# Задача 6
# Найти сумму цифр числа.
# '''
# print('Задача 6. Найти сумму цифр числа.')
# n = int(input('Напишите число: '))
#
# sum = 0
# while n > 0:                        # 1. Пока введенное число N больше 0,
#    sum = sum + (n % 10)             # 2. в переменную sum добавляем крайнюю правую цифру числа N
#    n = n // 10                      # 3. затем эту цифру отсекаем (ее мы уже отработали), далее цикл заново идет и уже работает с 2, добавляет ее к sum по такому же принципу
# print('Ответ:', sum)
# print()
#
#
# '''
# Задача 7
# Найти произведение цифр числа.
# '''
# print('Задача 7. Найти произведение цифр числа.')
# n = int(input('Напишите число: '))
#
# mult = 1
# while n > 0:                        # 1. Пока введенное число N больше 0,
#    mult = mult * (n % 10)           # 3. переменную mult умножаем на крайнюю правую цифру числа N
#    n = n // 10                      # 4. затем эту цифру отсекаем (ее мы уже отработали), далее цикл заново идет и уже работает с 2, добавляет ее к sum по такому же принципу
# print('Ответ:', mult)
# print()
#
#
# '''
# Задача 8
# Дать ответ на вопрос: есть ли среди цифр числа 5?
# '''
# print('Задача 8. Есть ли среди цифр числа 5?')
# n = int(input('Напишите число: '))
#
# while n > 0:                                # 1. Открываем цикл, когда число больше 0
#     if n % 10 == 5:                         # 2. Если остаток от деления = 5, пишем: "ДА!"
#         print('Ответ: Да')
#         break                               # 3. Выходим из цикла после успешно найденной пятерки
#     n = n // 10                             # 4. Делим наше число на 10 и пока не увидим 5 — делим дальше
# else:
#     print('Ответ: Нет')                     # 5. Если цифры 5 нет — пишем "нет".
# print()

'''
Задача 9
Найти максимальную цифру в числе
'''
print('Задача 9. Найти максимальную цифру в числе')
n = int(input('Напишите число: '))
max_digit = 0

while n > 0:
    if n % 10 >= max_digit:             # 1. и если краяняя цифра числа N больше или равна переменной (if 25 % 10 >= 0 или if 5 >= 0)
        max_digit = n % 10              # 2. то применять к переменной значение крайней цифры числа N (max_digit = 5)
    n = n // 10                         # 3. и задаваем N новое значение — применяем остаток от деления на 10 (n = 25 // 10 = 2) и повторяем цикл с п.2, Это будет выполняться, пока не закончатся целые десятки.
else:
    print('Ошибка')
print('Ответ:', max_digit)
print()

# ——————————— ВОПРОС К №9 ———————————
# 1. Как сделать цикл, чтобы при нулевом значении max_digit выводился ошибка else? Что-то у меня с ними проблема.

'''
Задача 10
Найти количество цифр 5 в числе
'''
print('Задача 10. Найти количество цифр 5 в числе')
count = 0
n = int(input('Напишите число: '))

while n > 0:                                    # пока вводимое число больше нуля
    if n % 10 == 5:                             # если последня цифра равна 5,
        count += 1                              # увеличиваем счетчик на +1
    n = n // 10                                 # избавляемся от последней цифры числа, после чего повторяем цикл
else:
    print('Введите число с пятеркой')
print('Ответ:', count)


# ——————————— ВОПРОС К №10 ———————————
# 1. Если добавить дальше:
#    else:
#    print('Такой цифры нет')
# то else не отрабаетывается отдельно, а выводится всегда + дублируется ответ, если цифры в числе две.
# почему так? предполагаю, что просто не в той строчке пишу и/или не внутри нужного цикла, но перебрал разные комбо уже :(
# Пробовал добавлять break — но что-то никуда он не подошел.

# 2. Как сделать цикл, чтобы пока в числе не будет 5, то просить ввод числа снова? Пытался взять простейшую тему с Volvo — но не получается додумать.
