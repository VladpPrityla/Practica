import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))



def GCD(a, b):
    if a == b:
        return a
    elif a > b:
        return GCD(a - b, b)
    elif a < b:
        return GCD(a, b - a)

print(GCD(500, 150))

printTimeStamp("Злочевська Д. С. Притула В. О.")
