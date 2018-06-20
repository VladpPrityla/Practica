import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

d = int(input("Введіть висоту: "))
print("Остаточна швидкість: ",(0+2*9.8*d)**0.5)

printTimeStamp("Злочевська Д. С. Притула В. О.")
