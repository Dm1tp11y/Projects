# 3. Реализовать функцию my_func(), которая принимает три позиционных
# аргумента и возвращает сумму наибольших двух аргументов.

def my_func(a,b,c):
        my_el = [a,b,c]
        my_list = []
        max1 = max(my_el)
        my_list.append(max1)
        my_el.remove(max1)
        max2 = max(my_el)
        my_list.append(max2)
        print(sum(my_list))
my_func(3, 2, 1)

def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("Введите первый аргумент ")), int(input("Введите второй аргумент ")), int(input("Введите третий аргумент ")))}')
