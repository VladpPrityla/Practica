import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

live = input("Де ти живеш? ")
time = input("Скільки часу ти дома? ")
inttime = int(time)
if live == "Будинок":
    if inttime >= 18:
        print("В'єтнамське порося")
    elif inttime < 10:
        print("Змія")
    else:
        print("Собака")
elif live == "Квартира":
    if inttime < 10:
        print("Хом'як")
    else:
        print("Кішка")
elif live == "Гуртожиток":
    if inttime < 6:
        print("Мурашки")
    else:
        print("Рибки")

printTimeStamp("Злочевська Д. С. Притула В. О.")
