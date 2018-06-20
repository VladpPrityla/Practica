import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

P =  int(input("Введіть тиск в Па: "))
T = int(input("Введіть температуру в К: "))
V = int(input("Введіть об'єм: "))

print((P*V)/(8.314*T))

printTimeStamp("Злочевська Д. С. Притула В. О.")
