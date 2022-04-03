"""3. Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка."""

from random import randint


def my_decorator(func):
    def the_wrapper(my_list):
        func([elem for elem in my_list if elem % 2])  # Сама функция

    return the_wrapper  # Вернём эту функцию


@my_decorator
def my_func(my_list):
    print(my_list)


my_list = [randint(-100, 100) for _ in range(20)]
print(my_list)
my_func(my_list)

# Спасибо, Шломчик
