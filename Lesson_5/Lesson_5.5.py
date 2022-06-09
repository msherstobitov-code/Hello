
def more_than(*argv):
    result = set()
    for elem in argv:
        if not elem in result:
            result.add(elem)
        else:
            result.remove(elem)
    return [x for x in argv if x in result]
if __name__ == "__main__":
    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    x = more_than(*src)
    print(type(x))
    print(x)
    
    
    
    
