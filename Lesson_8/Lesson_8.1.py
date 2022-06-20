import re
email = input('Введите адрес электронной почты: ')
VALID_RE = re.compile(
    r"(?P<username>([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+)@(?P<domain>[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)")
def email_parse(email):
    try:
        test = list(map(lambda x: x.groupdict(), VALID_RE.finditer(email)))
        print(test[0])
    except:
        raise ValueError from ValueError
email_parse(email)