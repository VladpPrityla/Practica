import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

n = int(input("Введіть ціле число: "))
a = float(n*(n + 1) / 2)
print (a)

printTimeStamp("Злочевська Д. С. Притула В. О.")
