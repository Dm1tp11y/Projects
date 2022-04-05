# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные,
# затем выведите на экран.
numbers = 100
result = numbers ** 2
print(result)
number = 2
number_1 = 5
print(number_1 - number)
name = 'Дмитрий'
print('Ваше имя:', name)
name = 'Дмитрий'
city = 'Ульяновск'
age = 28
info = f'Привет я {name}, живу в городе {city} мне {age}'
print(info)
name = input('Как тебя зовут?: ')
city = input('В каком городе ты живешь?: ')
age = int(input('Сколько тебе лет?: '))

print(f'Привет {name}, ты живешь в {city}, у тебя очень красивый город, тебе {age} года(лет). ')
print(type(name))
print(type(city))
print(type(age))
