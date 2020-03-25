import requests   №импорт оранжевый, а ниже нет
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
print('My', response, 'so its ok, and Hello World! :)')

# Почему-то не всегда создаются импорты и требуется настраивать под каждый проект их повторно, скрин: https://prnt.sc/rmfnjs
