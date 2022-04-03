# Структура взята у shloma, заранее спасибо, решение понял

from datetime import datetime, timedelta

trains = {
    "№ 228": {
        "From": "Брест",
        "T_start": datetime(2021, 12, 25, 10, 55),
        "To": "Москва",
        "T_finish": datetime(2021, 12, 25, 20, 30)
    },
    "№ 999": {
        "From": "Минск",
        "T_start": datetime(2021, 12, 25, 6, 4),
        "To": "Литва",
        "T_finish": datetime(2021, 12, 25, 17, 40)
    },
    "№ 666": {
        "From": "Борисов",
        "T_start": datetime(2021, 12, 25, 8, 4),
        "To": "Минск",
        "T_finish": datetime(2021, 12, 25, 10, 4)
    },
    "№ 777": {
        "From": "Москва",
        "T_start": datetime(2021, 12, 25, 8, 4),
        "To": "Владивосток",
        "T_finish": datetime(2021, 12, 27, 20, 30)
    },
    "№ 888": {
        "From": "Борисов",
        "T_start": datetime(2021, 12, 25, 6, 15),
        "To": "Гомель",
        "T_finish": datetime(2021, 11, 25, 10, 4)
    },
    "№ 1234": {
        "From": "Минск",
        "T_start": datetime(2021, 11, 12, 8, 4),
        "To": "Заславль",
        "T_finish": datetime(2021, 11, 12, 9, 4)
    },
}

for key in trains.keys():
    travel_time = trains[key]["T_finish"] - trains[key]["T_start"]

    if travel_time > timedelta(hours=7, minutes=20):
        print(f"Поезд {key} {trains[key]['From']} - {trains[key]['To']} был в пути {travel_time}")
