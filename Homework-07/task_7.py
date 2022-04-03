while True:
    num = None
    print(
        "1. Дюймы в сантиметры\n"
        "2. Сантиметры в дюймы\n"
        "3. Мили в километры\n"
        "4. Километры в мили\n"
        "5. Фунты в килограммы\n"
        "6. Килограммы в фунты\n"
        "7. Унции в граммы\n"
        "8. Граммы в унции\n"
        "9. Галлон в литры\n"
        "10. Литры в галлоны\n"
        "11. Пинты в литры\n"
        "12. Литры в пинты\n"
    )
    options = {
        "1": lambda: print(
            f"{n} дюймов - это {(lambda inches: inches * 2.54)(n)} сантиметров "
        ),
        "2": lambda: print(
            f"{n} сантиметров - это {(lambda centimeters: centimeters / 2.54)(n)} дюймов "
        ),
        "3": lambda: print(
            f"{n} миль - это {(lambda miles: miles * 1.609)(n)} километров "
        ),
        "4": lambda: print(
            f"{n} километров - это {(lambda kilometers: kilometers / 1.609)(n)} миль "
        ),
        "5": lambda: print(
            f"{n} фунтов - это {(lambda pounds: pounds / 2.205)(n)} килограммов "
        ),
        "6": lambda: print(
            f"{n} килограммов - это {(lambda kilograms: kilograms * 2.205)(n)} фунтов "
        ),
        "7": lambda: print(
            f"{n} унций - это {(lambda ounces: ounces / 28.35)(n)} граммов "
        ),
        "8": lambda: print(
            f"{n} граммов - это {(lambda grams: grams * 28.35)(n)} унций "
        ),
        "9": lambda: print(
            f"{n} галлонов - это {(lambda gallons: gallons / 3.7854)(n)} литров "
        ),
        "10": lambda: print(
            f"{n} литров - это {(lambda liters: liters * 3.7854)(n)} галлонов "
        ),
        "11": lambda: print(
            f"{n} пинт - это {(lambda pints: pints / 2.113)(n)} литров "
        ),
        "12": lambda: print(
            f"{n} литров - это {(lambda liters: liters * 2.113)(n)} пинт "
        ),
    }
    while num not in options.keys():
        num = input("Введите, что вы хотите перевести: ")
    n = float(input("Введите число для конвертации: "))
    options[num]()
    if input("Если хотите выйти из программы, нажмите 0: ") == "0":
        break
