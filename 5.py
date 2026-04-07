input_password = input("Введіть пароль:")

password = "2g52"

tries = 3


def get_auth_sucess():
    print("Вхід є")

def get_auth_failed():
    print("Входу немає")

def tries_left(count):
    print("У вас залишилося", count, "спроби")

def get_auth_status(input_password, password):
    if password == input_password:
        return True
    else:
        return False
        

# if get_auth_status(input_password, password):    
#     get_auth_sucess()
# else:
#     get_auth_failed()


for i in range(3, 0, -1):
    print(tries)
    if get_auth_status(input_password, password):    
        get_auth_sucess()
        break    
    else:
        get_auth_failed()
        tries_left(i)
        input_password = input("Введіть пароль:")
        tries -= 1
        
if tries == 0:
    print("Ліміт вичерпано")