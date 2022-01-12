from random import *
from module1 import *
log_user=['Artjom']
pas_user=['Rozhkov']

vxod=''
user=''
new_user=''
login=''
pas=''
new_pas=''
str0=".,:;!_*-+()/#¤%&"
str1 = '0123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()


while vxod not in ["Да","Нет","да","нет"]:
    vxod=input("У вас имеется аккаунт?: ")
    print()
    if vxod=="Да" or vxod=="да":
        autorize()
    if vxod=="Нет" or "нет":
        login=input("Придумайте логин не длинее 12 символов: ")
        if len(login)>12:
            print("Логин слишком длинный. Попробуйте ещё раз!")
        elif isUserUnic(log_user,login)==False:
            print("Пользователь существует. Придумайте новый логин")
        else:
            print("Логин подошел, ваш логин -", login)
            print("--------------------------------------")
        while new_pas not in ["y","Y","n","N"]:
            new_pas=input("Вы хотите сгенерировать пароль или придумать сами?(y/n): ")
        if new_pas in ['Y','y']:
            str4 = str0+str1+str2+str3
            ls = list(str4)
            random.shuffle(ls)
            new_pas = ''.join([random.choice(ls) for x in range(12)])
            print("Ваш пароль -", new_pas)
            autorize()
        else:
            new_pas=input("Придумайте пароль не менее 8 символов: ")
            if len(new_pas)<8:
                print("Пароль слишком короткий. Попробуйте еще раз!")
            else:
                print("Пароль подошел, ваш пароль -", new_pas)
                print()
                new_pas=''
                while new_pas not in ['n','N','Y','y']:
                    new_pas=input("Ваш аккаунт был успешно создан! Хотите войти в него?(y/n): ")
                if new_pas in ['Y','y']:
                    autorize()
                   

                

                
                



        



























































#welcome=''
#answer_pass=''
#passTry=1
#a=False
#while welcome not in ['y','n','Y','N']:
#    welcome=input("Добро пожаловать! У вас уже есть аккаунт?(y/n): ")
#if welcome in ['N','n']:
#    while a==False:
#        welcome=input("Создайте логин не длинее 12 символов: ")
#        if len(welcome)>12:
#            print("Слишком большой логин, попробуйте еще раз!")
#        elif isUserUnic(usernames,welcome)==False:
#            print("Пользователь существует. Придумайте новый логин")
#        elif welcome=input("Создайте пароль не менее 8 символов: ")
#    if len(welcome)<8:
#        print("Слишком ненадежный пароль. Попробуйте еще раз!")
#        elif isUserUnic(usernames,welcome)==True and len(welcome)<=12:
#            break
#while answer_pass not in ['y','n','Y','N']:
#    answer_pass=input("Вам помочь сгенерировать надежный пароль?(y/n): ")
#while 1:
#    if passTry==0 and answer_pass in ['n','N']:
#        break
#    elif answer_pass in ['y','Y']:
#        number=input('количество паролей?'+ "\n")
#        length=input('длина пароля?'+ "\n")
#        number=int(number)
#        length=int(length)
#        for n in range(number):
#            password =''
#            for i in range(length):
#                password+=random.choice(chars)
#            print("Ваш пароль -", password)
#    if welcome in ['n','N']:
#        break

















    #    number = input('количество паролей?'+ "\n")
    #    length = input('длина пароля?'+ "\n")
    #    number = int(number)
    #    length = int(length)
    #    for n in range(number):
    #        password =''
    #        for i in range(length):
    #            password += random.choice(chars)
    #        print(password)
    #if welcome in ['n','N']:
    #    break



    



