FILENAME = 'bakery.csv'

with open(FILENAME, "r", encoding="utf-8") as f:
    user_lines = f.readlines()
    for i in user_lines:
        print(i)

x = int(input('введите номер: '))
for i in user_lines:
    if x == 1:
        print(user_lines[0])
        break
    if x == 2:
        print(user_lines[1])
        break
    if x == 3:
        print(user_lines[2])
        break