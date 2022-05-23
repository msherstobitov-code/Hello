numbers = list(range(1,1001,2))
number_cube = [i ** 3 for i in numbers]
print (number_cube)
total = 0
for i in number_cube:
    if sum([int(j) for j in str(i)]) % 7 == 0:
        total += i
print(total)
number_17 = [i + 17 for i in number_cube]
print(number_17)
total_1 = 0
for i in number_17:
    if sum([int(j) for j in str(i)]) % 7 == 0:
        total_1 += i
print(total_1)







