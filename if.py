brand = 'volvo'              # Бренд
engine_volume = 1.5          # Объем двигателя
horsepower = 180             # Мощность
sunroof = True              # Наличие люка

# Проверка условия IF
#if horsepower < 80: print('No Tax')
#else: print('Alert! Tax!')


# Проверка условия if/elif/elif/else
if horsepower < 80:
    tax = 0
elif horsepower < 100:
    tax = 10000
elif horsepower < 150:
    tax = 20000
else:
    tax = 50000
print('You have tax amount:', tax)


# Проверка условия if для присваивания:

supercar = 0

supercar = 1 if sunroof == 1 else 0
if supercar == 1:
    print('Supercar!')
else:
    print('Badcar...!')

# Или можно в конце просто написать один текст
print('Your supercar = ',supercar)