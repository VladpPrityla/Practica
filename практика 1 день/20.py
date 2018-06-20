import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

bread = int(input("Скільки вчорашнього хліба потрібно? "))
new_bread = bread * 8.5
print("Якщо купити свіжий хліб = %.2f $" % new_bread)
znizhka = new_bread * 0.60
print("Знижка на вчорашній хліб = %.2f $" % znizhka)
good_bread = new_bread - znizhka
print("Потрібно заплатити за покупку = %.2f $" % good_bread)

printTimeStamp("Злочевська Д. С. Притула В. О.")
