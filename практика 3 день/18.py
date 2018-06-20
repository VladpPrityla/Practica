import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

def sum(a):
    if a == 1:
        return 1
    else:
        return (1 / a) + sum(a - 1)

print(sum(17))
printTimeStamp("Злочевська Д. С. Приитула В.О.")
