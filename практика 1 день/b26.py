import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Введіть рівень шуму: "))
if 106 < a < 130:
    print("between Jackhammer and Gas lawnmower")
elif a == 130:
    print("Jackhammer")
elif 70 <= a < 106:
    print("between Alarm clock and Gas lawnmower")
elif a == 106:
    print("Gas lawnmower")
elif 40 <= a < 70:
    print("between Alarm clock and Quiet room")
elif a == 70:
    print("Alarm clock")
elif a < 40:
    print("lower Quiet room")
elif a == 40:
    print("Quiet room")
elif a > 130:
    print("get older Jackhammer")
else:
    print("Помилка")



printTimeStamp("Злочевська Д. С. Притула В. О.")
