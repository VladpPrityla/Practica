import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

storona1 = int(input("1 сторона: "))
storona2 = int(input("2 сторона: "))
storona3 = int(input("3 сторона: "))

if storona1 != storona2 and storona1 != storona3 and storona2 != storona3:
    print("Нерівносторонній трикутник")
elif storona1 == storona2 and storona1 == storona3 and storona2 == storona3:
    print("Рівносторонній трикутник")
else:
    print("Рівнобедрений трикутник")

printTimeStamp("Злочевська Д. С. Притула В. О.")
