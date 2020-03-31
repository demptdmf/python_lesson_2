# Динамическая типизация ----------
# --------------------------------



temp_var_1 = input('Input smth: ')
print(temp_var_1, type(temp_var_1), id(temp_var_1))

temp_var_2 = input('Input smth 2: ')
print(temp_var_2, type(temp_var_2), id(temp_var_2))

#temp_var_1 = temp_var_2
temp_var_1 = int(temp_var_2)

print(temp_var_1, type(temp_var_1), id(temp_var_1))
print()

# Приведение типов

def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


temp_float = input('Input float number: ')
print('Here is string: ', temp_float, type(temp_float), id(temp_float))
print()
if is_digit(temp_float):
    temp_float = float(temp_float)
    print('GRATZ! HERE IS FLOAT!!!', temp_float, type(temp_float), id(temp_float))
else:
    print('This is not number :(')