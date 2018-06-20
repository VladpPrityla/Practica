import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Введіть к-ть днів: "))
b = float(input("Введіть к-ть годин: "))
c = float(input("Введіть к-ть хвилин: "))
d = float(input("Введіть к-ть секунд: "))

print((86400*a)+(3600*b)+(60*c)+d)
printTimeStamp("Злочевська Д. С. Притула В. О.")
