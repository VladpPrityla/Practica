import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

y = int(input("Введіть рік: "))
if y % 400 == 0:
    print("Високосний")
elif y % 100 == 0:
    if y % 4 != 0:
        print("Невисокосний")
    else:
        print("Високосний")
else:
    print("Невисокосний")

printTimeStamp("Злочевська Д. С. Притула В. О.")
