"""2) В семье N свадьба. Они решили выбрать заведение, где будут праздновать в зависимости от количества людей,
которое прибудет к утру. Если их будет больше 50 - закажут ресторан, если от 20 до 50 -то кафе, а если меньше 20 то
отпраздную дома. Вывести "ресторан", "кафе", "дом" в зависимости от количества гостей (прочитать переменную с
консоли) """

num = -1
while not num >= 0:
    num = int(input("Input your number: "))

if num > 50:
    print("ресторан")
elif 20 <= num <= 50:
    print("кафе")
else:
    print("дом")
