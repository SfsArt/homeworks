input_password = input("Введіть пароль:")

password = "2g52"

auth_status = False

#    if password == input_password:
#        print("Вхід є")
#    else:
#        print("Входу немає")



def get_auth_sucess():
    print("Вхід є")

def get_auth_failed():
    print("Входу немає")

def tries_left(count):
    print("У вас залишилося", count, "спроби")

def check_input_pass():
    if password == input_password:
        auth_status = True
        

for i in range(3, 0, -1):
    check_input_pass(input_password)
        
    if password == input_password:
        auth_status = True
        get_auth_sucess()
        break
    else:
        get_auth_failed()
        print("Спробуйте ще раз")
        tries_left(i)
        input_password = input("Введіть пароль:")
        if password == input_password:
            get_auth_sucess()
            break
        elif i == 2:
            print("Залишилася остання спроба!")
        elif i == 1:
            break


