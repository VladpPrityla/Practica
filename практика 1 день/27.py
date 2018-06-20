import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

time = [22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8]

papu = input("Якщо папуга говорить: ")
my_time = int(input("Котра година? "))
if papu == 'Спить':
    print("Якщо папуга мовчить, значить все добре")
elif papu == 'Кричить' and my_time not in time:
    print("Папуга говорить, тому що день")
else:
    print("Потрібно накрити клітку")


printTimeStamp("Злочевська Д. С. Притула В. О.")
