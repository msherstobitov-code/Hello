list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
string = ' '.join(list)
name_1 = string[20:25]
print(f"Привет! {name_1}")
name_2 = string[44:50]
print(f'Привет! {name_2.capitalize()}')
name_3 = string[74:81]
print(f'Привет! {name_3.title()}')