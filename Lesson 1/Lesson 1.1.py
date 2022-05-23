while True:
    duration = int(input('Введите время в секундах или команду стоп: '))
    if duration == 'стоп':
        break
    elif duration <= 60:
        print(duration, 'cек')
    elif 3600 > duration > 60:
        minutes = duration // 60
        seconds = duration % 60
        print(f'{minutes} минут {seconds} секунд')
    elif 86400 > duration >= 3600:
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        seconds = duration % 60
        print(f'{hours} час {minutes} минут {seconds} секунд')
    else:
        days = duration // 86400
        hours = (duration - 86400) // 3600
        minutes = ((duration - 86400) % 3600) // 60
        seconds = ((duration - 86400) % 3600) % 60
        print(f'{days} день {hours} час {minutes} минут {seconds} секунд')