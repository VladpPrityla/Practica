import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

d = int(input("Довжина поля: "))
sh = int(input("Ширина поля: "))
Sa = d * sh / 100
Sg = d * sh / 10000

print("Площа поля: \n" + str(Sa) + " в Арах\n" + str(Sg) + " в Гектарах")

printTimeStamp("Злочевська Д. С. Притула В. О.")
