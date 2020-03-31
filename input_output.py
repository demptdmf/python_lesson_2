#Задание 2
'''
тест
многострочного
комментария
'''
print('Hey!')
print('Hey!', 'Ho', 22)
print('Hey!', 'Ho', 22, sep = 'x')      # Разделители "Х", вместо пробела
print('Hey!', 'Ho', 22, end = 'a')      # Окончание строки с символом "А"
print()
print()

# Ввод
name = input('Input your name here: ')
print(name)
print('Это класс', type(name))

age = input('and input your age: ')
print('Это тоже класс STR: ', type(age))
print('А здесь уже будет класс INT: ', type(int(age)),'т.к. мы его поменяли')