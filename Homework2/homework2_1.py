# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


my_int = 1
my_float = 1.2
my_str = 'Строка'
my_list = ['a', '2']
my_dict = {'город': 'Ульяновск', 'страна': 'Россия'}
my_bool = False
my_NoneType = None

type_list = [my_int, my_float, my_str, my_list, my_dict, my_bool, my_NoneType]
for i in type_list:
    print(f'{i} is {type(i)}')


