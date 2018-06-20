import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Введіть магнітуду: "))
if 0< a < 2.0:
    print("Мікро")
elif 2.0 <= a < 3.0:
    print("Дуже слабкий")
elif 3.0 <= a < 4.0:
    print("Слабкий")
elif 4.0 <= a < 5.0:
    print("Легкий")
elif 5.0 <= a < 6.0:
    print("Помірний")
elif 6.0 <= a < 7.0:
    print("Сильний")
elif 7.0 <= a < 8.0:
    print("Дуже сильний")
elif 8.0 <= a < 10.0:
    print("Великий")
elif a>10:
    print("Рідкісно великий")
else:
    print("Помилка")



printTimeStamp("Злочевська Д. С. Притула В. О.")
