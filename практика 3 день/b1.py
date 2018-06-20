import datetime
import math
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

def gen(n,r=[]):
    for x in range(n):
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l+1)]
        yield r

def draw(n):
    for p in gen(n):
        print(' '.join(map(str,p)).center(n*2)+'\n')
print(draw(5))
printTimeStamp("Злочевська Д. С. Притула В. О.")
