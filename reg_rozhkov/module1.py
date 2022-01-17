import random
def isUserUnic(usernamesList,vxod):
    for i in range (len(usernamesList)):
        if usernamesList[i]==vxod:
            isUnic=False
            return isUnic
            break
    isUnic=True
    return isUnic




def autorize(pas_user:list,log_user:list):
    user=input("Введите логин: ")
    pas=input("Введите пароль: ")
    if pas_user.index(pas)==log_user.index(user):
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
            