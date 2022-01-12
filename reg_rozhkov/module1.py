import random
def isUserUnic(usernamesList,vxod):
    for i in range (len(usernamesList)):
        if usernamesList[i]==vxod:
            isUnic=False
            return isUnic
            break
    isUnic=True
    return isUnic



log_user=['Artjom']
pas_user=['Rozhkov']
def autorize():
    user=input("Введите логин: ")
    pas=input("Введите пароль: ")
    if pas_user.index(pas)==log_user.index(user):
        print()
        print("Вы вошли в систему!")
        print()
