import datetime
import random
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

t = open("Boom.txt", 'r')
text = t.readlines()

password = text[random.randint(0, len(text) - 1)].title() + text[random.randint(0, len(text) - 1)]
print(password)
t.close()
printTimeStamp("Злочевська Д. С. Притула В. О.")
