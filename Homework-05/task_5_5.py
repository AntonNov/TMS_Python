"""5) В массиве целых чисел с количеством элементов 19 определить максимальное число и
заменить им все четные по значению элементы."""

from random import randint

my_list = [randint(0, 100) for _ in range(20)]
print("Исходный список:\n", my_list)

for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        my_list[i] = max(my_list)
print("Изменённый список:\n", my_list)
