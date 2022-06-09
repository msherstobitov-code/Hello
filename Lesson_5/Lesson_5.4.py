

def more_than(*argv):
    return (argv[i] for i in range(1, len(argv)) if argv[i] > argv[i - 1])
if __name__ == "__main__":
    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = more_than(*src)
    print(type(result))
    print(list(result))
