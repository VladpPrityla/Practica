
import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

x = (1,'a',2,'b',3,'c') 
d = dict(x[i:i+2] for i in range(0, len(x), 2))
print (d)


printTimeStamp("Злочевська Д. С. Притула В. О.")
