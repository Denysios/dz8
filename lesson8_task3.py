class IntNumberErr(Exception):
    """
    Функция заполняет пустой список числами, которые вводит пользователь.
    Если введено не целое число, значение не добавится.
    Для остановки ввода, нужно ввести "stop" и нажать Enter.
    """

    def __init__(self):
        self.lst_user = []

    def input_user(self):
        while True:
            num = input('Введите число. Для завершения ввода введите "stop": ')
            if num == 'stop':
                break
            try:
                num = int(num)
            except ValueError as v_err:
                print(f'Вы ввели не число. {v_err}')
            else:
                self.lst_user.append(num)
        print(self.lst_user)


a = IntNumberErr()
a.input_user()
