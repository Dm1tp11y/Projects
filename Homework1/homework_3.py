# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число3.
# Считаем 3 + 33 + 333 = 369.

n = input('Введите число?: ')

s1 = (n)
s2 = (n+n)
s3 = (n+n+n)

s4 = int(s1) + int(s2) + int(s3)

print(s4)