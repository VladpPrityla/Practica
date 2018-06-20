import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

dollar = int(input("Введіть ціле число: "))
nominals = [1,2,5,10,50]

nominals.sort()
nominals.reverse()
a = 0
print (dollar, 'коп')

for k in nominals:
    d = dollar//k
    dollar = dollar -d*k
    print (k,'коп: ',int(d))
    a += d

print ('Сума: ', a)


printTimeStamp("Злочевська Д. С. Притула В. О.")
