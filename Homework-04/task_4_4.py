# 4) Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример: 12345-> 23451

my_list = list(range(1, 6))
my_list2 = list(my_list)
my_list2.append(my_list2.pop(0))

print("Было: ", my_list)
print("Стало: ", my_list2)
