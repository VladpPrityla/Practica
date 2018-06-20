import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

add = 0
while True:
    try:
        a = input()
        if a == '':
            break
        add += int(a)
        print("Сума: " + str(add))
    except:
        print("Введіть дані")
        print("Сума: " + str(add))
print("Сума: " + str(add))


printTimeStamp("Злочевська Д. С. Притула В. О.")
