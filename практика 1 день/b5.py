import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


puk = input("Введіть 13-цифровий ISBN: ")

a = int(puk[0]*1) + int(puk[1]*3) + int(puk[2]*1) + int(puk[3]*3) + int(puk[4]*1) + int(puk[5]*3) + int(puk[6]*1) + int(puk[7]*3) + int(puk[8]*1) + int(puk[9]*3) + int(puk[10]*1) + int(puk[11]*3)

b = 10 - (a % 10)
if b == puk[12]:
    print("Ви ввели правильний ISBN")
else:
    print("Помилка ISBN")


printTimeStamp("Злочевська Д. С. Притула В. О.")
