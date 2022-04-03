# 2) Дано число. Найти сумму и произведение его цифр.
from numpy import product

my_list = list(map(int, input()))

print("Сумма:", sum(my_list))
print("Произведение: ", product(my_list))
