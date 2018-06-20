import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

def taxi(meter, money):
   a = 25 + money  * (meter//140)
   return a

print(taxi(25 , 2))


printTimeStamp("Злочевська Д. С. Притула В. О.")
