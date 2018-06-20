import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))


name = str(input("Введіть ваше ім’я: "))
print("Привіт, ", name)

printTimeStamp("Злочевська Д. С. Притула В. О.")
