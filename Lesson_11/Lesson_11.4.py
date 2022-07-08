class Warehouse_equipment:
    pass


class Office_equipment:  # base class
    def __init__(self, common_param_1, common_param_2):
        self.common_param_1 = common_param_1
        self.common_param_2 = common_param_2


class Printer(Office_equipment):  # child class
    def __init__(self, printer_param=None):
        self.printer_param = printer_param  # unique_parameter

    def print_func(self, common_param_2=None):
        return self.printer_param + common_param_2


class Scanner(Office_equipment):  # child class
    def __init__(self, scanner_param=None):
        self.scanner_param = scanner_param  # unique_parameter

    def scan_func(self, common_param_1=None):
        return self.scanner_param + common_param_1


class Xerox(Office_equipment):  # child class
    def __init__(self, xerox_param=None):
        self.xerox_param = xerox_param  # unique_parameter

    def xer_func(self, common_param_2=None):
        return self.xerox_param + common_param_2


a = Printer(3)
print(a.print_func(5))

c = Xerox(2)
print(c.xer_func(3))
