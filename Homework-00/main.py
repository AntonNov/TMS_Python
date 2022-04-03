a, b = 0.1, 0.2

dict1 = {
    "Sum": a + b,
    "Difference": a - b,
    "Multiplication": a * b,
    "Degree": a ** b,
    "Division": a / b,
}
for key, value in dict1.items():
    print(key, value)
