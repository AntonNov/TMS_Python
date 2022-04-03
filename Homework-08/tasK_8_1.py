"""Описать функцию fact2(n), вычисляющую двойной факториал:
n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 — параметр целого типа.
С помощью этой функции найти двойные факториалы пяти данных целых чисел"""

from random import randint


def fact2(n):
    return 1 if n < 2 else n * fact2(n - 2)


my_list = [randint(0, 10) for _ in range(5)]
print(my_list)
for el in my_list:
    print(fact2(el))
