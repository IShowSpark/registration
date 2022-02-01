import random
def isUserUnic(usernamesList,vxod): #тут проверка идет если пользователь такой уже в базе
    for i in range (len(usernamesList)):
        if usernamesList[i]==vxod:
            isUnic=False
            return isUnic
            break
    isUnic=True
    return isUnic




def autorize(pas_user:list,log_user:list): #сделал отдельную команду на авторизацию чтоб не писать по 20 раз одно и тоже, тут думаю логично как работает
    user=input("Введите логин: ") #просто спрашивает данные
    pas=input("Введите пароль: ") #просто спрашивает данные
    if pas_user.index(pas)==log_user.index(user): #если пароль и логин совпадают, то входит 
        print()
        print("Вы вошли в систему!")
        print()


def faillist_read(f:str,l:list):
    '''Информация ф сохранена в список л
    '''
    fail=open(f,'r')
    for line in fail:
        l.append(line.strip())
    fail.close()
    return l

def failsalve(f:str,l:list):
    fail=open(f,'w')
    for el in l:
        fail.write(el+'\n')
    fail.close()


    def readsalve(f:str,rida:str):
        fail=open(f,'a')
        fail.write(rida+'\n')
        fail.close()
            
