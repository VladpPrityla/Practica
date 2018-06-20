import datetime
import math
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

s = int(input("Введіть довжину сторони: "))
n = int(input("Введіть к-ть сторін:"))

print((n*(s**2))/(4*math.tan(math.pi/n)))

printTimeStamp("Злочевська Д. С. Притула В. О.")
