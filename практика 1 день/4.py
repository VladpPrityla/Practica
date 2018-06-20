import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))


a = ["a", "e", "i", "o", "u"]
b = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
c = "y"

mount = input("Введіть англійську літеру: ")

if mount == c:
    mount = "голосна, а інколи - приголосна"
elif mount in b:
    mount = "приголосна"
elif mount in a:
    mount = "голосна"
else:
    print("Помилка")
print("Літера - " + str(mount))

printTimeStamp("Злочевська Д. С. Притула В. О.")
