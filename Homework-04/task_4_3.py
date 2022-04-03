"""3) Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
Чтобы получить список ключей - использовать метод .keys()
(подсказка: создается новый ключ с цифрой в конце, старый удаляется)"""

my_dict = {"test": "test_value", "europe": "eur", "dollar": "usd", "ruble": "rub"}
my_dict2 = dict(my_dict)
for key in list(my_dict.keys()):
    my_dict[key + str(len(key))] = my_dict.pop(key)
print("with for: ", my_dict)

keys = list(my_dict2.keys())
i = 0
while i < len(keys):
    my_dict2[keys[i] + str(len(keys[i]))] = my_dict2.pop(keys[i])
    i += 1
print("with while: ", my_dict2)
