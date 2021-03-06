# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
#
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Программа работает с действительными х и целыми у')
        return
    if x <=0 or y >= 0:
        print('Программа работает с положительными х и отрицательными у')
        return
    return 1 / x ** abs(y)

print(my_func(input('Введите положительный х: '), input('Введите отрицательный у: ')))
