import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

n = input("Введіть чотирьохзначне число: ")
n = int(n)
 
d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
d3 = n % 10
n = n // 10
d4 = n % 10
 
print("Сума цифр числа: ", d1 + d2 + d3 + d4)
printTimeStamp("Злочевська Д. С. Притула В. О.")
