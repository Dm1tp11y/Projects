# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

my_list = ['Зима', 'Весна', 'Лето', 'Осень']
my_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите месяц: "))
if month == 1 or month == 12 or month == 2:
        print(my_dict.get(1))
        print(my_list[0])
elif month == 3 or month == 4 or month == 5:
    print(my_dict.get(2))
    print(my_list[1])
elif month == 6 or month == 7 or month == 8:
    print(my_dict.get(3))
    print(my_list[2])

elif month == 9 or month == 10 or month == 11:
    print(my_dict.get(4))
    print(my_list[3])
else:
    print("Такого месяца не существует")