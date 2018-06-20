import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Введіть частоту радіації: "))
if 0< a < 3*(10**9):
    print("Radio waves")
elif 3*(10**9) <= a < 3*(10**12):
    print("Microwaves")
elif 3*(10**12) <= a < 4.3*(10**14):
    print("Infrared light")
elif 4.3*(10**14) <= a < 7.5*(10**14):
    print("Visible light")
elif 7.5*(10**14) <= a < 3*(10**17):
    print("Ultraviolet light")
elif 3*(10**17) <= a < 3*(10**19):
    print("X-rays")
elif a>3*(10**19):
    print("Gamma rays")
else:
    print("Error")



printTimeStamp("Злочевська Д. С. Притлуа В. О.")
