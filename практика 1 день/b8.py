import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a = input("Введіть місяць народження: ")
b = int(input("Введіть число народження: "))

if a == ("December") and b >= 22:
    print("Capricorn")
elif b <= 21:
    print("Segittarius")

elif a == ("January") and b >= 20:
    print("Aquarius")
elif b <= 19:
    print("Capricorn")

printTimeStamp("Злочевська Д. С. Притула В. О.")
