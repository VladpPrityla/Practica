import re
import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

alpha = 'abcdefghijklmnopqrstuvwxyz'
n = int(input("Ключ: "))
s = input("Введіть текст для зашифровування: ").rstrip()
res = ''
for c in s:
   res += alpha[(alpha.index(c) + n) % len(alpha)]
print('Шифр: ' + res)

printTimeStamp("Злочевська Д. С. Притула В. О.")
