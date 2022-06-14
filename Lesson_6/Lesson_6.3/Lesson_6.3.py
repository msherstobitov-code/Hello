import json
def gen(x, y):
    len_y = len(y)
    return ((elem, y[i]) if i < len_y else (elem, None)
            for i, elem in enumerate(x))
def groping(users,hobby,out):

    with open(users, "r", encoding="utf-8") as f:
        user_lines = f.readlines()

    with open(hobby, "r", encoding="utf-8") as f:
        hobby_lines = f.readlines()

    group = {}

    for fio, hobby in gen(user_lines, hobby_lines):
        fio = fio.replace("\n", "").replace(",", " ")
        group[fio] = hobby.replace("\n", "") if hobby else None

    with open(out, "w+", encoding="utf-8") as out_file:
        out_file.writelines(json.dumps(group))
    print(group)
if __name__ == "__main__":
    groping("./users.csv", "./hobby.csv", "./out.txt")


