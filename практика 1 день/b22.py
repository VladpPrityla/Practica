import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


a = input("Введіть оцінку: ")
if a == ">4":
    print("A+")
elif a == "4":
    print("A")
elif a == "3.7":
    print("A-")
elif a == "3.3":
    print("B+")
elif a == "3":
    print("B")
elif a == "2.7":
    print("B-")
elif a == "2.3":
    print("C+")
elif a == "2":
    print("C")
elif a == "1.7":
    print("C-")
elif a == "1.3":
    print("D+")
elif a == "1":
    print("D")
elif a == "0":
    print("F")
else:
    print("Помилка")
printTimeStamp("Злочевська Д. С. Притула В. О.")
