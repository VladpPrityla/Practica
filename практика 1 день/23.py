import datetime
import math
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

s = a + b
r = b - a
d = a * b
ch = a / b
o = a % b
lg = math.log10( a )
lg2 = math.log10( b )
z = a ** b

print("Сума " + str(s) + "\nРізниця " + str(r) + "\nДобуток " + str(d) + "\nЧастка " + str(ch) + "\nОстача від ділення " + str(o) + "\nЛогарифм " + str(lg) + "\n Логарифм2 " + str(lg2) + "\nПерша змінна в степені другої " + str(z))


printTimeStamp("Злочевська Д. С. Притула В. О.")
