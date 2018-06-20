import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

d = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":"-.-.","K":"-.-","L":".-..","M":"--",
          "N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":".-..","Y":"-.--","Z":"--..",
         "0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}
def change():
    global d
    crypt = ""
    text = input("Введіть текст: ")
    for i in text:
        b = i.upper()
        for j in d:
            if b == " ":
                crypt += " "
            elif b == j:
                crypto = ''.join([d.get(c.upper(), ' ') for c in text])
    print("Отриманий код: " + str(crypto))
change()

printTimeStamp("Злочевська Д. С. Притула В. О.")
