# Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел

x, y = map(float, input("Введите x и y через пробел: ").split())

print("Среднее арифметическое", (x + y) / 2)
print("Среднее геометрическое", (x * y) ** 0.5)
