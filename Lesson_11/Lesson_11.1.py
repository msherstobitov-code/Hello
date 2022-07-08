from datetime import datetime

format = "%d-%m-%Y"


class Data:
    def __init__(self, data_str):
        self.data_str = data_str

    @classmethod
    def get_date(cls, data_str):
        data_str = data_str.split('-')
        ints = [(int(s)) for s in data_str]
        print(ints[0], ints[1], ints[2])

    @staticmethod
    def validation_data(data_str):
        try:
            res = True
            if res == bool(datetime.strptime(data_str, format)):
                print('correct date format')
        except Exception:
            print('incorrect date format')


Data.get_date("02-05-2021")
Data.validation_data("07-07-2022")
Data.validation_data("07+07-2022")