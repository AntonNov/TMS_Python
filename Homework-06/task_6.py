from random import randint

a, b = 0, 20
dimensions = 4, 5
n, m = dimensions


def make_matrix(n, m) -> list[list[int]]:
    return [[randint(a, b) for _ in range(m)] for _ in range(n)]


def print_matrix(matrix) -> None:
    for line in matrix:
        print(*line, sep="\t\t")


# 1) Создать матрицу случайных чисел от a до b, размерность матрицы n*m
matrix = make_matrix(*dimensions)
print(matrix)
print("Исходная матрица: ")
print_matrix(matrix)

# 2) Найти максимальный элемент матрицы.
print("Максимальный элемент матрицы:", max(max(line) for line in matrix))

# 3) Найти минимальный элемент матрицы.
print("Минимальный элемент матрицы:", min(min(line) for line in matrix))

# 4) Найти сумму всех элементов матрицы.
print("Сумма элементов матрицы:", sum(sum(line) for line in matrix))
summ = [sum(line) for line in matrix]

# 5) Найти индекс ряда с максимальной суммой элементов.
for index, sum_of_row in enumerate(summ):
    if sum_of_row == max(summ):
        print(f"{index} ряд с максимальной суммой элементов")

# 6) Найти индекс колонки с максимальной суммой элементов.
matrix2 = [[matrix[i][j] for i in range(n)] for j in range(m)]
print("Новая матрица: ")
print_matrix(matrix2)

print("Сумма по колонкам:", [sum(line) for line in matrix2])
summ2 = [sum(line) for line in matrix2]

for index, sum_of_column in enumerate(summ2):
    if sum_of_column == max(summ2):
        print(f"{index} колонка с максимальной суммой элементов")

# 7) Найти индекс ряда с минимальной суммой элементов.
minimum = min(summ)
for index, sum_of_row in enumerate(summ):
    if sum_of_row == minimum:
        print(f"{index} ряд с минимальной суммой элементов")

# 8) Найти индекс колонки с минимальной суммой элементов.
minimum = min(summ2)
for index, sum_of_column in enumerate(summ2):
    if sum_of_column == minimum:
        print(f"{index} колонка с минимальной суммой элементов")

# 9) Обнулить все элементы выше главной диагонали.
for i in range(n):
    for j in range(m):
        if j > i:
            matrix[i][j] = 0
print("Обнулили все элементы выше главной диагонали")
print_matrix(matrix)

# 10) Обнулить все элементы ниже главной диагонали.
for i in range(n):
    for j in range(m):
        if i > j:
            matrix[i][j] = 0
print("Обнулили все элементы ниже главной диагонали")
print_matrix(matrix)

# 11) Создать две новые матрицы matrix_a, matrix_b случайных чисел
# размерностью n*m.
matrix_a = make_matrix(n, m)
matrix_b = make_matrix(n, m)
print("Матрица А: ")
print_matrix(matrix_a)
print("Матрица B: ")
print_matrix(matrix_b)

# 12)Создать матрицу равную сумме matrix_a и matrix_b.
matrix_c = [[matrix_a[i][j] + matrix_b[i][j] for j in range(m)] for i in range(n)]
print("Матрица C: ")
print_matrix(matrix_c)

# 13)Создать матрицу равную разности matrix_a и matrix_b.
matrix_d = [[matrix_a[i][j] - matrix_b[i][j] for j in range(m)] for i in range(n)]
print("Матрица D: ")
print_matrix(matrix_d)

# 14)Создать новую матрицу равную matrix_a умноженной на g. g вводится с
# клавиатура"""
g = float(input("Введите g: "))
matrix_e = [[matrix_a[i][j] * g for j in range(m)] for i in range(n)]
print("Матрица E: ")
print_matrix(matrix_e)
