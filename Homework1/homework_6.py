# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчёте на одного сотрудника.

profit = int(input('Введите значение прибыли: '))
cost = int(input('Введите значение издержек: '))
people = int(input('Ввдите количество работников: '))
if profit > cost:
     print('Выручка больше издержек')
     clear_plus = profit - cost
     rent = clear_plus/profit
     print('Рентабельность {} выручки {}: {:.2f}' .format('нашей','составила',rent))
     clear_for_person = float(clear_plus/people)
     print('Прибыль фирмы в расчете на одного сотрудника: %s'%clear_for_person)