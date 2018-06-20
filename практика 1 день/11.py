import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Введіть свій зріс в сантиметрах: "))

print("Обчислення зросту в футах та дюймах: ",("%.0f" % (a*0.0328095), "%.0f" %(a*0.25)))

printTimeStamp("Злочевська Д. С. Притула В. О.")
