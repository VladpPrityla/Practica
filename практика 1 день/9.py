import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Введіть вік собаки: "))

if a <= 2:
    print("Вік людини: " , a*5.25)
elif a > 2:
    print("Вік людини: " , ((a-2)*4)+10.5)
printTimeStamp("Злочевська Д. С. Притула В. О.")
