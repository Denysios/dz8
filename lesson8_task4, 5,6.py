class WarehouseOfficeEquipment:
    lst_department = ['accounts department', 'it']
    data = {
        'принтеры': [],
        'сканеры': [],
        'ксероксы': []
    }

    def receipt_on(self, arg):
        self.data['принтеры'].append(arg) if 'принтер' in arg.values() else False
        self.data['сканеры'].append(arg) if 'сканер' in arg.values() else False
        self.data['ксероксы'].append(arg) if 'ксерокс' in arg.values() else False
        print(f'На склад добавлена новая позиция: {arg}')

    def transfer_by_department(self):
        pass


class OfficeEquipment:

    def __init__(self, name, model, price, quantity):
        self.name = name
        self.model = model
        self.price = price
        self.quantity = quantity

    @classmethod
    def __dict__(cls):
        return dict(cls)


class Printer(OfficeEquipment):
    data_printer = ['наименование', 'модель', 'цена', 'количество', 'конструкция']

    def __init__(self, name, model, price, quantity, design):
        OfficeEquipment.__init__(self, name, model, price, quantity)
        self.design = design

    def get_dct_printer(self):
        dct_printer = {
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'количество': self.quantity,
            'конструкция': self.design}

        return dct_printer


class Scan(OfficeEquipment):
    data_printer = ['наименование', 'модель', 'цена', 'количество', 'технология']

    def __init__(self, name, model, price, quantity, technology):
        OfficeEquipment.__init__(self, name, model, price, quantity)
        self.technology = technology

    def get_dct_scan(self):
        dct_scan = {
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'количество': self.quantity,
            'технология': self.technology}
        return dct_scan


class Xerox(OfficeEquipment):
    data_printer = ['наименование', 'модель', 'цена', 'количество', 'скорость печати']

    def __init__(self, name, model, price, quantity, speed):
        OfficeEquipment.__init__(self, name, model, price, quantity)
        self.speed = speed

    def get_dct_xerox(self):
        dct_xerox = {
            'наименование': self.name,
            'модель': self.model,
            'цена': self.price,
            'количество': self.quantity,
            'скорость печати': self.speed}
        return dct_xerox

# Цикл запрашивает у пользователя какую технику описать и составляет словарь с параметрами
# data_obj = ['бренд', 'модель', 'цена', 'количество']
# data_printer, data_scan, data_xerox = data_obj + ['конструкция'], data_obj + ['технология'], data_obj + ['скорость']
# while True:
#     user_sku = input('Введите название оргтехники, которую нужно описать (принтер, сканер или ксерокс), или "stop": ')
#     if user_sku == 'stop':
#         break
#     elif user_sku == 'принтер':
#         dct_printer = {x: (y := input(f'Введите значение {x}: ')) for x in data_printer}
#         print(dct_printer)
#     elif user_sku == 'сканер':
#         dct_scan = {x: (y := input(f'Введите значение {x}: ')) for x in data_scan}
#         print(dct_scan)
#     elif user_sku == 'ксерокс':
#         dct_xerox = {x: (y := input(f'Введите значение {x}: ')) for x in data_xerox}
#         print(dct_xerox)

dt_obj = ['наименование', 'модель', 'цена', 'количество']
dt_printer, dt_scan, dt_xerox = dt_obj + ['конструкция'], dt_obj + ['технология'], dt_obj + ['скорость']
#printer = ['принтер', 'nb123', 10000, 5, 'laser']
printer = [(x := input(f'Введите {el}: ')) for el in dt_printer]
try:
    printer.extend[2:3] = map(float, printer[2:3])
except:
    print(f'Значения {printer[3]} и {printer[2]} должны быть числами')

scan = ['сканер', 'khj56', 8000, 3, 'latbed_scan']
xerox = ['ксерокс', 'sad55', 9000, 10, '100/m']
a = Printer(*printer)
b = Scan(*scan)
c = Xerox(*xerox)

# print(a.get_dct_printer())
# print(b.get_dct_scan())
# print(c.get_dct_xerox())

ware_house = WarehouseOfficeEquipment()
ware_house.receipt_on(a.get_dct_printer())
ware_house.receipt_on(b.get_dct_scan())
ware_house.receipt_on(c.get_dct_xerox())
print(f'{WarehouseOfficeEquipment.data}')
