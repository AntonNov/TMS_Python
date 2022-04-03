"""3) Два натуральных числа называют дружественными, если каждое из них равно сумме всех делителей другого, кроме
самого этого числа. Найти все пары дружественных чисел, лежащих в диапазоне от 200 до 300. """


def foo(num):
    return sum(n for n in range(1, num) if num % n == 0)


my_dict = dict()
for i in range(200, 301):
    for j in range(201, 301):
        if i == foo(j) and j == foo(i):
            my_dict[i] = j
            print(f"Дружеская пара {i} - {my_dict[i]}")
print(my_dict)
