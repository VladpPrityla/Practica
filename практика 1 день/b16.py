import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Введіть температуру в С: "))
b = float(input("Введіть швидкість вітру: "))

if 0 < a <= 10 and 0 < b <= 4.8:
    print(13.12 + (0.6215*a)-(11.37*(b**0.16))+(0.3965*a*(b**0.16)))
else:
    print("Помилка")
          
printTimeStamp("Злочевська Д. С. Притула В. О.")
