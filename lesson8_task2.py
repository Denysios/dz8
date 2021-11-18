class ZeroErr(Exception):

    @staticmethod
    def div_func(n1, n2):
        try:
            n1, n2 = int(n1), int(n2)
            if n2 != 0:
                return int(n1 / n2)
            else:
                raise ZeroErr(f'На ноль делить нельзя.')
        except ZeroErr:
            return ZeroErr(f'На ноль делить нельзя.')
        except ValueError as err:
            return f'Вы ввели не число: {err}'


num1 = input('Введите число которое хотите разделить: ')
num2 = input('Введите число на которое хотите разделить: ')
div = ZeroErr
print(div.div_func(num1, num2))
