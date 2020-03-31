#Задание №1 Введение

import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
print('My', response, 'so its ok, and Hello World! :)')