"""4. Создать универсальный декоратор, который меняет порядок аргументов в функции на противоположный."""


def my_decorator(my_func):
    def wrapper(*args):
        my_func(args[::-1])  # Меняем порядок аргументов

    return wrapper


@my_decorator
def print_args(*args):
    for arg in args:
        print(*arg)


args = ("first", 1, [4], 6, 8, {1: True}, "a", "last")
print(*args)
print_args(*args)

# Спасибо, Шломчик
