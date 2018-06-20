import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))


x = int (input ("Введіть кількість штучок: "))
y = int (input ("введіть кількість штукенцій: "))
print (x * 75 + y * 112 , "г")

printTimeStamp("Злочевська Д. С. Притула В. О.")
