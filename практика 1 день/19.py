import time
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

x = time.time()
print(x)
print(type(x))
y = time.asctime()
print(y)
printTimeStamp("Злочевська Д. С. Притула В. О.")
