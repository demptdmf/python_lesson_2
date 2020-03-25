import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
print('My', response, 'so its ok, and Hello World! :)')

#1. Почему-то не всегда создаются импорты и требуется настраивать под каждый проект их повторно, скрин: https://prnt.sc/rmfnjs
#2. почему-то в гит улетела папка .idea, хотя отмечался только мейн.ру — как удалить это из гита?