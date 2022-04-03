# Даны 2 действительных числа a и b. Получить их сумму, разность и произведение.

x, y = map(float, input("Введите x и y через пробел: ").split())

dict1 = {"Сумма": x + y, "Разность": x - y, "Произведение": x * y}
for key, value in dict1.items():
    print(f"{key}: {value}")
