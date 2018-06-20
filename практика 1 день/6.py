import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))


a = int(input("Введіть вартість замовлення: "))
b = a / 100 * 14
c = a / 100 * 18
f = a + b + c
template = '{:.' + str(2) + 'f}'
print(template.format(f))

printTimeStamp("Злочевська Д. С. Притула В. О.")
