import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a = int(input("Введіть перше додатнє ціле число: "))
b = int(input("Введіть друге додатнє ціле число: "))
d = 0
if a > b:
    d = b
else:
    d = a

while True:
    if a % d == 0 and b % d == 0:
        break
    d -= 1

print("Найбільший спільний дільник: " + str(d))


printTimeStamp("Злочевська Д. С. Притула В. О.")
