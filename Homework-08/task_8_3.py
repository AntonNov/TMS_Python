"""Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε — вещественные, ε > 0),
находящую приближенное значение функции sin( x ):
sin(x) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε .
С помощью Sin1 найти приближенное значение синуса для данного x при шести данных ε """

from math import sin, factorial, pi
from random import uniform


def sin1(x, eps):
    summa, n = 0, 0
    while True:
        to_add = (-1) ** n * x ** (2 * n + 1) / factorial(2 * n + 1)
        if abs(to_add) < eps:
            return summa
        summa += to_add
        n += 1


eps = 0.1
random_value = uniform(-pi, pi)
print(f"Случайная величина: {random_value}\t Значение синуса: {sin(random_value)}")
for _ in range(6):
    print("Разница: ", abs(sin(random_value) - sin1(random_value, eps)))
    eps /= 10
