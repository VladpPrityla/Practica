import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

t = open("ПІП 21.txt", 'a')
t.write("Злочевська Дарина Семенівна, Притула Владислав Олегович")

t.close()
printTimeStamp("Злочевська Д. С. Притула В. О.")
