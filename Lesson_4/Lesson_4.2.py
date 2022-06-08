
def currency_rates(*args):
    import requests
    import json
    import datetime as dt
    import time
    while True:
        URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
        currency_name = input('Введите код валюты: ')
        currency_name = currency_name.upper()
        response = requests.get(URL)
        dict_json = json.loads(response.text)
        current_course = dt.datetime.utcnow() + dt.timedelta(hours=5)
        for key, value in dict_json['Valute'].items():
            if key == 'USD' and key == currency_name:
                x = dict_json['Valute']['USD']['Value']
                x = float(x)
                x = round(x, 2)
                print(f"Курс USD на {current_course.strftime('%d %b %Y')} равен {x}")
            elif key == 'EUR' and key == currency_name:
                y = dict_json['Valute']['EUR']['Value']
                y = float(y)
                y = round(y, 2)
                print(f"Курс EUR на {current_course.strftime('%d %b %Y')} равен {y}")


currency_rates()
