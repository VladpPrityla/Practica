import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

print(GCD(100, 300))

printTimeStamp("Злочевська Д. С. Притула В. О.")
