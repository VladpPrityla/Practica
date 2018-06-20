import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))



def hotel(days, price):
    return days * price

def travel(city):
    if city == "Львів":
        return 3
    elif city == "Китай":
        return 5

def car(day):
    sum = day * 20
    if day >= 7:
        sum -= 25
    elif 3 < day < 7:
        sum -= 10
    return sum

def calculate(day, city, money):
    must_pay = travel(city) + hotel(day, 200) + car(day) + money
    return must_pay

print(calculate(3, "Львів", 5))


printTimeStamp("Злочевська Д. С. Притула В. О.")
