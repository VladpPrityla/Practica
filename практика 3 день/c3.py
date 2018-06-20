import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


import turtle

def paint(points,color,picture):
    picture.fillcolor(color)
    picture.up()
    picture.goto(points[0][0],points[0][1])
    picture.down()
    picture.begin_fill()
    picture.goto(points[1][0],points[1][1])
    picture.goto(points[2][0],points[2][1])
    picture.goto(points[0][0],points[0][1])
    picture.end_fill()

def middle(a , b):
    return ( (a[0]+b[0]) / 2, (a[1] + b[1]) / 2)

def pouring(points,degree,picture):
    colormap = ['teal','firebrick','yellow','pink', 'blueviolet']
    paint(points,colormap[degree],picture)
    if degree > 0:
        pouring([points[0],
                        middle(points[0], points[1]),
                        middle(points[0], points[2])],
                   degree-1, picture)
        pouring([points[1],
                        middle(points[0], points[1]),
                        middle(points[1], points[2])],
                   degree-1, picture)
        pouring([points[2],
                        middle(points[2], points[1]),
                        middle(points[0], points[2])],
                   degree-1, picture)

def main():
   picture = turtle.Turtle()
   display = turtle.Screen()
   points = [[-100,-50],[0,100],[100,-50]]
   pouring(points,4,picture)
   display.exitonclick()

main()
printTimeStamp("Злочевська Д. С. Притула В. О.")
