def my_sum(x, y):
    return x+y, False, x - y

print(my_sum(7,8))
h = my_sum(5, 8)[0] * 3 + 98
print(h)
