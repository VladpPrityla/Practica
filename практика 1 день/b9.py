import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


nomer = input("Номер: ")

b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']
n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

if len(nomer) == 6:
    if nomer[0] in b and nomer[1] in b and nomer[2] in b and nomer[3] in n and nomer[4] in n and nomer[5] in n:
        print("Старий формат")
    else:
        print("Новий формат")
if len(nomer) == 7:
    if nomer[0] in b and nomer[1] in b and nomer[2] in b and nomer[3] in b and nomer[4] in n and nomer[5] in n and nomer[6] in n:
        print("Старий формат")
    else:
        print("Новий формат")


printTimeStamp("Злочевська Д. С. Притула В. О.")
