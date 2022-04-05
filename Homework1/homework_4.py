# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


number = int(input('Введите число: '))
ls = []
while number > 10:
    ls.append(number % 10)
    number //= 10
numbers = max(ls)
print(numbers)


number = input('Введите число: ')
print(max(number))
