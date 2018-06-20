import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a, b, c = list(map(int, input("Введіть 3 числа: ").split()))
l = [" " for i in range(a+b+c)]
l[a] = a
l[b] = b
l[c] = c
print(" ".join(str(i) for i in l[::+1]))

printTimeStamp("Злочевська Д. С. Притула В. О.")
