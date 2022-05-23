for percent in range(1,101):
    if 1 < percent < 5 or 22 <= percent < 25 or 32 <= percent < 35:
        print(f'{percent} процента')
    elif 42 <= percent < 45 or 52 <= percent < 55 or 62 <= percent < 65:
        print(f'{percent} процента')
    elif 72 <= percent < 75 or 82 <= percent < 85 or 92 <= percent < 95:
        print(f'{percent} процента')
    elif percent in range(21,92,10) or percent ==1:
        print(f'{percent} процент')
    else:
        print(f'{percent} процентов')