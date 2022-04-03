"""5) Составить список чисел Фибоначчи содержащий 15 элементов.
(Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны 1 и 1, а каждое последующее
 число равно сумме двух предыдущих чисел. Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
"""


def fibonacci(n):
    return 1 if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(n):
    my_new_list = [1, 1]
    i = 2
    while i < n:
        my_new_list.append(my_new_list[i - 1] + my_new_list[i - 2])
        i += 1
    return my_new_list


def fibonacci3(n):
    my_new_list = [1, 1]
    for i in range(2, n):
        my_new_list.append(my_new_list[i - 1] + my_new_list[i - 2])
    return my_new_list


num = 15
print("Первая попытка:")
print([fibonacci(i) for i in range(num)])

print("Вторая попытка:")
print(fibonacci2(num))

print("Третья попытка:")
print(fibonacci3(num))
