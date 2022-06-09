
def odd_to(n):
    for num in range(1, n + 1, 2):
        yield num
if __name__ == "__main__":
    gen = odd_to(15)
    for odd in gen:
        odd_list = list(gen)
        print('odd numbers: ', *odd_list)