# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('Указать время в секундах:'))

a = (seconds // 3600)
b = ((seconds % 3600) // 60)
c = ((seconds % 3600) % 60)
time = ['{:02d}:{:02d}:{:02d}'.format(a, b, c)]

print(time)