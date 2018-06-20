import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a = int(input("Введіть рік: "))

if a % 12 == 0:
    print("Dragoon")
elif a % 12 == 1:
    print("Shake")
elif a % 12 == 2:
    print("Horse")
elif a % 12 == 3:
    print("Sheep")
elif a % 12 == 4:
    print("Monkey")
elif a % 12 == 5:
    print("Rooster")
elif a % 12 == 6:
    print("Dog")
elif a % 12 == 7:
    print("Pig")
elif a % 12 == 8:
    print("Rat")
elif a % 12 == 9:
    print("Ox")
elif a % 12 == 10:
    print("Tiger")
elif a % 12 == 11:
    print("Hare")

printTimeStamp("Злочевська Д. С. Притула В. О.")
