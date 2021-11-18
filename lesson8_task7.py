class ComplexNumber:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __add__(self, other):
        return f'Сумма равна: {self.arg1 + other.arg1} + {self.arg2 + other.arg2}j'

    def __mul__(self, other):
        return f'Произведение равно: {self.arg1 * other.arg1 - (self.arg2 * other.arg2)} + {self.arg2 * other.arg1}j'


num_1 = ComplexNumber(126, -83)
num_2 = ComplexNumber(57, 89)
print(num_1 + num_2)
print(num_1 * num_2)
