import random
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))



a = 0
phone = []
def number():
    global phone
    global a

    tel = '+38(0'
    tel += str(random.randint(0, 99))
    tel += ')'
    tel += str(random.randint(0, 999))
    tel += '-'
    tel += str(random.randint(0, 99))
    tel += '-'
    tel += str(random.randint(0, 99))
    phone.append(tel)
    a += 1
    if a < 3:
        number()

number()
print(phone)

printTimeStamp("Злочевська Д. С. Притула В. О.")
