import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

def Fibonacci(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 1            
   else:                      
      return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(15))
printTimeStamp("Злочевська Д. С. Притула В. О.")
