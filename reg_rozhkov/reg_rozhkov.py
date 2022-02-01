from random import *
from module1 import *

log_user=[]
pas_user=[]


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


while vxod not in ["Да","Нет","да","нет"]: #Пока Вход, то есть vxod=input("У вас имеется аккаунт?: ") не будет Да нет и т.д
    log_user=faillist_read('Logins.txt', log_user) #Это читает файлы, функция списана с доски 
    pas_user=faillist_read('passwords.txt', pas_user) #Тоже самое
    vxod=input("У вас имеется аккаунт?: ")
    print() #просто пустое место для красоты
    if vxod=="Да" or vxod=="да": #Если вход то есть vxod=input("У вас имеется аккаунт?: ") будет ДА, то оно запросит авторизацию autorize() это тоже в модуле есть
        autorize(pas_user,log_user)
    if vxod=="Нет" or "нет": #Если вход то есть vxod=input("У вас имеется аккаунт?: ") будет нет, то оно запросит у тебя регистрацию
        login=input("Придумайте логин не длинее 12 символов: ") #Здесь соответственно вписываешь пароль 
        if len(login)>12: #тут стоит чтоб не было больше 12 символов
            print("Логин слишком длинный. Попробуйте ещё раз!") #если больше 12, то пишет ну нельзя типо
        elif isUserUnic(log_user,login)==False: #Тут функция опять же в модуле, если аккаунт с таким же именем и паролем уже в базе есть, то оно отказывает тебе и пишет пользователь существует
            print("Пользователь существует. Придумайте новый логин") #после оно тебе снова запрашивает регистрацию типо новый логин пароль и если подходит, то переходит на следующий этап
        else:
            print("Логин подошел, ваш логин -", login) #значит работает
            print("--------------------------------------") #для красоты
        while new_pas not in ["y","Y","n","N"]: #new pas это новый пароль то есть для нового акка пароль, тут написано пока new pas не будет Y n и т.д
            new_pas=input("Вы хотите сгенерировать пароль или придумать сами?(y/n): ") #Если будет Y n и т.д, то оно задаст тебе вопрос написанный на этой строчке, если не будет Y n и т.д, то оно будет бесконечно спрашивать, то есть это проверка которая реагирует только на Y n и т.д
        if new_pas in ['Y','y']: #тут если выбираешь Y то оно генерирует тебе пароль само, нижние 5 строчек взяты с мудла и autorize() мой взят из модуля
            str4 = str0+str1+str2+str3
            ls = list(str4)
            random.shuffle(ls)
            new_pas = ''.join([random.choice(ls) for x in range(12)])
            print("Ваш пароль -", new_pas)
            autorize()
        else:
            new_pas=input("Придумайте пароль не менее 8 символов: ") #else идет то есть если не Y, то получается N и получается сам придумываешь пароль не менее 8 символов
            if len(new_pas)<8: #Это идет значение чтоб не было меньше 8 символов
                print("Пароль слишком короткий. Попробуйте еще раз!") #Если пароль меньше 8 символов, то оно ругается 
            else:
                print("Пароль подошел, ваш пароль -", new_pas) #Если все подходит, то идешь на следующий этап уже авторизация
                print()
                new_pas=''
                while new_pas not in ['n','N','Y','y']: #очередная проверка чтоб ничего не мог написать кроме этого что в скобках квадратных
                    new_pas=input("Ваш аккаунт был успешно создан! Хотите войти в него?(y/n): ") #сам вопрос
                if new_pas in ['Y','y']: #тут если Y, то оно просто входит в него, а дальше я не доделал :(
                    autorize(pas_user,log_user)
                   


                

                
                



        



























































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



    



