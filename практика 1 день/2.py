import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))


a = float(input("Введіть масу свого тіла: "))
b = float(input("Введіть ваш зріст: "))
c = a / b ** 2
print (c)

printTimeStamp("Злочевська Д. С. Притула В. О.")
