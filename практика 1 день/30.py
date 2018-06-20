import datetime
import math
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))


print("Оберіть якої температури велике яйце: ")
print("1. Кімнатна температура")
print("2. Температура яйця взятого з холодильника")
choice = input("Оберіть цифру(1/2): ")

if choice == '1':
    print((67**(2/3))*3.7*(1.038**(1/3))/(5.4*(10**3))*(math.pi**2)*(4*math.pi/3)**(2/3))*math.log(2.02666667)
elif choice == '2':
    print((67**(2/3))*3.7*(1.038**(1/3))/(5.4*(10**3))*(math.pi**2)*(4*math.pi/3)**(2/3))*math.log(2.432)

printTimeStamp("Злочевська Д. С. Притула В. О.")
