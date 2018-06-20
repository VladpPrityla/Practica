import random
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

def password():
    pin = ' '
    for a in range(random.randint(8, 17)):
        pin += chr(random.randint(33, 127))
    print(pin.encode("ASCII"))

for a in range(10):
    password()


printTimeStamp("Злочевська Д. С. Притула В. О.")
