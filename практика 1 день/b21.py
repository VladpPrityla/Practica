import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


a = input("Введіть буквенну оцінку: ")
if a == "A+":
    print(">4")
elif a == "A":
    print("4")
elif a == "A-":
    print("3.7")
elif a == "B+":
    print("3.3")
elif a == "B":
    print("3")
elif a == "B-":
    print("2.7")
elif a == "C+":
    print("2.3")
elif a == "C":
    print("2")
elif a == "C-":
    print("1.7")
elif a == "D+":
    print("1.3")
elif a == "D":
    print("1")
elif a == "F":
    print("0")

printTimeStamp("Злочевська Д. С. Притула В. О.")
