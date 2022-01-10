from random import *
from module1 import *
passwords=['A']
usernames=['B']
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


welcome=''
answer_pass=''
passTry=1
a=False
while welcome not in ['y','n','Y','N']:
    welcome=input("Добро пожаловать! У вас уже есть аккаунт?(y/n): ")
if welcome in ['N','n']:
    while a==False:
        welcome=input("Создайте логин не длинее 12 символов: ")
        if len(welcome)>12:
            print("Слишком большой логин, попробуйте еще раз!")
        elif isUserUnic(usernames,welcome)==False:
            print("Пользователь существует. Придумайте новый логин")
        elif isUserUnic(usernames,welcome)==True and len(welcome)<=12:
            break
while answer_pass not in ['y','n','Y','N']:
    answer_pass=input("Вам помочь сгенерировать надежный пароль?(y/n): ")
while 1:
    if passTry==0 and answer_pass in ['n','N']:
        break
    elif answer_pass in ['y','Y']:
        number = input('количество паролей?'+ "\n")
        length = input('длина пароля?'+ "\n")
        number = int(number)
        length = int(length)
        for n in range(number):
            password =''
            for i in range(length):
                password += random.choice(chars)
            print(password)
    if welcome in ['n','N']:
        break















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



    



