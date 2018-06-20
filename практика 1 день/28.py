import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

print("Оберіть день: ")
print("1. Робчий день")
print("2. Вихідний день")
print("3. Відпустка")
choice = input("Обретіть цифру(1/2/3): ")

if choice == '1':
   print("Потрібно ввімкнути будильник")

elif choice == '2':
   print("Будильник вимкнено")

elif choice == '3':
   print("Взагалі не потрібен")
else:
    print("Помилка")
printTimeStamp("Злочевська Д. С. Притула В. О.")
