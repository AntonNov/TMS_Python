"""6) Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число больше предыдущего)."""

from random import randint

array = [randint(-100, 100) for _ in range(10)]
print(array)

number_of_ranges, cols_item = 0, 0
prev_item = None
for item in array:
    try:
        if item < prev_item and cols_item >= 1:
            number_of_ranges += 1
            cols_item = 0

        if item > prev_item:
            cols_item += 1

    except:
        prev_item = item

if cols_item:
    number_of_ranges += 1
print(number_of_ranges)
