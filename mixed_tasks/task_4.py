users = {
 "admin": "1234",
 "pass": "qwerty"
}




while True:
    login = input("Введіть логін: ")

    if login == users["admin"]:
        password = input("Введіть пароль: ")
        if password == users["pass"]:
            print("Вхід успішний")
            break
        else:
            print("Спробуйте увійти ще раз")

    else:
        print("Неправильний логін, спробуйте ще раз")