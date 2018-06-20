import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))


x = int(input("Введіть тиск у кілопаскалях: "))
y = x * 0.14503773773022
print(y, "фт/дм^2")
z = x * 7.50062
print(z, "мм.рт.ст.")
d = x * 0.00986923266716013
print(d, "атм")

printTimeStamp("Злочевська Д. С. Притула В. О.")
