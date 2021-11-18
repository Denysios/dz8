class Date:

    def __init__(self, dmy):
        self.dmy = dmy

    @classmethod
    def method1(cls, dmy: str):
        lst = [int(i) for i in dmy.split('-')]
        dt, mon, year = lst[0], lst[1], lst[2]
        return dt, mon, year

    @staticmethod
    def method2(dt: int, mon: int, year: int) -> str:
        dt_res = dt if 0 < dt < 32 else print('Некорректно введено число')
        mon_res = mon if 0 < mon < 13 else print('Некорректно введен месяц')
        year_res = year if year > 0 and 5 > len(str(year)) > 2 else print('Некорректно введен год')
        return f'{dt_res}.{mon_res}.{year_res} г.'


a = '14-11-2021'
data = Date
print(Date(a))
print(Date.method1(a))
print(Date.method2(14, 11, 2021))
