#Задание №1 Введение

import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
print('My', response, 'so its ok, and Hello World! :)')

# Добавить папку в игнор-лист гита
echo
'.idea' >>.gitignore

# Удалить папку из стейджинга
git
rm - r - -cached.idea

# Добавить файл в гит
git
add.gitignore

# Зафиксировать изменения
git
commit - m
'Удалил папку .idea из репозитория'

# Запушить в репу
git
push