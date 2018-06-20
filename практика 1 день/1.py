import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

 
a = float(input("Введіть об'єм вашого контейнера: "))
b = int(input("Введіть кількість ваших контейнерів: "))
if a < 1:
    c = b * 0.10
    template = '{:.' + str(2) + 'f}'
    print(template.format(c), "$")
elif a > 1:
    c = b * 0.25
    template = '{:.' + str(2) + 'f}'
    print(template.format(c), "$")
else:
    print(error)
    
printTimeStamp("Злочевська Д. С. Притула В. О.")
