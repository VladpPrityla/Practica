import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

year = int(input("Введіть рік: "))
month = int(input("Введіть місяць: "))
day = int(input("Введіть день: "))
def magic(year, month, day):
    year = str(year)
    year2 = year[-2] + year[-1]
    if month * day == int(year2):
        print("Магічна дата")
    else:
        print("Не магічна дата")

magic(year, month, day)


printTimeStamp("Злочевська Д. С. Притула В. О.")
