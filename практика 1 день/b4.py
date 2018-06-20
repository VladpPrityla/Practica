import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


hv = int(input("Хвилин: "))
sms = int(input("СМС: "))

a = 15
b = 0

if hv > 200:
    a += hv - (200 * 0.17)
if sms > 50:
    a += sms - (50 * 0.15)

b = a + (a * 0.05) + 0.44

print("Без комісій: %.2f грн" % a)
print("Потрібно заплатити: %.2f грн" % b)


printTimeStamp("Злочевська Д. С. Притула В. О.")
