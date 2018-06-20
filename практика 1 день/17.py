import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

summ = int(input("Скільки грошей ви хочете покласти: "))
god1 = summ + summ * 0.14
print("Прибуток за один рік: %.2f $" % god1)
god2 = god1 + god1 * 0.14
print("Прибуток за два роки: %.2f $" % god2)
god3 = god2 + god2 * 0.14
print("Прибуток за три роки: %.2f $" % god3)


printTimeStamp("Злочевська Д. С. Притула В. О.")
