#Вариант 1
#list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#list[1] = '"05"'
#list[3] = '"17"'
#list[8] = '"+05"'
#string = ' '.join(list)
#print(string)

#Вариант 2
list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(list))
list_length = len(list)
for i in range(list_length):
    elem = list.pop(0)
    if elem.isdigit():
        list.append(f'"{int(elem):02d}"')
    elif elem[0] == "+" and elem[1].isdigit():
        list.append(f'"+{int(elem):02d}"')
    else:
        list.append(elem)
print(' '.join(list))
print(id(list))

