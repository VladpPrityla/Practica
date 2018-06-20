import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

print(factorial(10))
printTimeStamp("Злочевська Д. С. Притула В. О.")
