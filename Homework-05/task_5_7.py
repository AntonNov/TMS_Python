"""7) Дана целочисленная квадратная матрица. Найти в каждой строке наибольший элемент
и поменять его местами с элементом главной диагонали. """

from random import randint

n = 5
matrix = [[randint(-10, 10) for _ in range(n)] for _ in range(n)]

print("Исходная матрица: ")
for line in matrix:
    print(*line, sep="\t\t")

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == max(matrix[i]):
            matrix[i][j], matrix[i][i] = matrix[i][i], matrix[i][j]

print("Полученная матрица: ")
for line in matrix:
    print(*line, sep="\t\t")
