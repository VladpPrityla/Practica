import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


a = int(input("Введіть рік: "))
b = int(input("Введіть місяць: "))
c = int(input("Введіть число: "))
today = datetime.date(a, b, c)
tomorrow = today + datetime.timedelta(days=1)

print("Наступний день: " + str(tomorrow))

printTimeStamp("Злочевська Д. С. Притула В. О.")
