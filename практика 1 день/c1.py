import datetime
import random
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
a = random.randint(1, 38)
if a == 38:
    a = "00"
if a == 0 and a == "00":
    print("На рулеткі випало: " + str(a) + "\nВиплатити: " + str(a))
else :
    print("На рулеткі випало: " + str(a) + "\nВиплатити: " + str(a))
    if a != "00":
        if a in red:
            print("Виплатити Red")
        else:
            print("Виплатити Black")
        if a != "00" and a % 2 == 0:
            print("Виплатити Парне")
        else:
            print("Виплатити Непарне")
        if a != "00" and a <= 19:
           print("Виплатити 1 - 18")
        else:
            print("Виплатити 19 - 36")

printTimeStamp("Злочевська Д. С. Притула В. О.")
