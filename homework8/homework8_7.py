# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.v = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма v1 и v2 равна')
        return f'v = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение v1 и v2 равно')
        return f'v = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'v = {self.a} + {self.b} * i'


v_1 = ComplexNumber(1, -2)
v_2 = ComplexNumber(3, 4)
print(v_1)
print(v_1 + v_2)
print(v_1 * v_2)