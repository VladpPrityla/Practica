import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = ["January", "March", "May", "July", "August", "October", "December"]
b = ["April", "June", "September", "November"]
c = "February"

mount = input("Введіть місяць (англійською): ")

if mount == c:
    mount = "28 або 29 днів"
elif mount in b:
    mount = "30 днів"
elif mount in a:
    mount = "31 день"
else:
    print("Помилка")
print("В місяці " + str(mount))

printTimeStamp("Злочевська Д. С. Притула В. О.")
