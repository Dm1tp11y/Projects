# 2.Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def div(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(div(surname='Trusov', name='Dmitriy', year='1993', city='Ulyanovsk', email='ul@mail.ru',
              telephone='8-903-300-00-00'))


