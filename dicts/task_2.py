i = 1
while i > 0:

    names = {
    "Артем": 3,
    "Іван": 15,
    "Сергій": 9
    }


    name = input("Введіть ім'я: ")

    if name in "Артем":
        print(names["Артем"])
    elif name in "Іван":
        print(names["Іван"])
    elif name in "Сергій":
        print(names["Сергій"])
    else:
        print("Такого імені не існує")

