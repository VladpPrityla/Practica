import datetime
import  math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

r = int(input('Введіть радіус: '))

s = math.pi * r ** 2  

v = 4 / 3 * math.pi * r ** 3  

print("Площа круга = {}, Об'єм кулі = {}".format(s, v))
printTimeStamp("Злочевська Д. С. Притула В. О.")
