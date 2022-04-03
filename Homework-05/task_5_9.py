"""9) Для каждого натурального числа в промежутке от m до n вывести все делители,
 кроме единицы и самого числа. m и n вводятся с клавиатуры."""


def find_divisors(num):
    print(f"{num}:", end=" ")
    print(*[i for i in range(2, num) if num % i == 0])


m, n = map(int, input("Введите m и n через пробел: ").split())
for num in range(m, n + 1):
    find_divisors(num)
