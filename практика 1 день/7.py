import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))


x = int(input("Введіть градуси в цельсія: "))
print((x * 1.8) + 32, "по Фаренгейту")
print(x + 273.15 , "в кельвинах")

printTimeStamp("Злочевська Д. С. Притула В. О.")
