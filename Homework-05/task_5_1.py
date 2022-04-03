"""1) Написать программу, в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *). Вычислить
результат Z в зависимости от знака. Предусмотреть реакции на возможный неверный знак операции,
а также на ввод Y=0 при делении.
Организовать возможность многократных вычислений без перезагрузки программа (т.е. построить бесконечный цикл).
В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0')."""

sign = None
X, Y = 0, 0
while Y == 0:
    X, Y = map(float, input("Введите X и Y через пробел: ").split())
operations = {"+": X + Y, "-": X - Y, "*": X * Y, "/": X / Y}
while True:
    sign = input("Введите знак операции: ")
    if sign in operations:
        print(operations[sign])
    elif sign == "0":
        break
    else:
        print("Неверный знак операции!")
