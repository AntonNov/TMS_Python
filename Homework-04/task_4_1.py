""" 1) Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2 """

from random import randint

my_list = [randint(-20, 20) for _ in range(20)]
print(my_list)

print([num * -2 for num in my_list])

new_list2 = list()
cnt = 0
while cnt < len(my_list):
    new_list2.append(-2 * my_list[cnt])
    cnt += 1
print(new_list2)
