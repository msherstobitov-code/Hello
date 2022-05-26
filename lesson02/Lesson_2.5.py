price_list =[57.8, 46.51, 97, 72.3, 90.72, 120.54, 170, 208.72, 114.6, 55, 130.24, 330.87, 270.74, 350, 33.56]
print(price_list)
print()
for index, item in enumerate(price_list):
    pricing = str(f"{float(item):.2f}").split(".")
    print(f"{pricing[0]} руб {pricing[1]} коп", end=', ')

print()
print()

print(id(price_list))
price_list.sort()
print((price_list))
print(id(price_list))
print()
price_list.reverse()
print(price_list)
print()

print(price_list[0:4])

