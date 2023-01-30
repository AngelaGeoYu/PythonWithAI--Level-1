import turtle
turtle.pencolor('white')
turtle.bgcolor('black')
turtle.pensize(3)
turtle.up()
turtle.rt(45)
turtle.fd(90)
turtle.rt(135)
turtle.down()

length = 200
x = 0

while x < 30:
#draw a hexagon
    turtle.fd(length)
    turtle.rt(61)
    turtle.fd(length)
    turtle.rt(61)
    turtle.fd(length)
    turtle.rt(61)
    turtle.fd(length)
    turtle.rt(61)
    turtle.fd(length)
    turtle.rt(61)
    turtle.fd(length)
    turtle.rt(61)
    turtle.rt(11.1111)
    x = x+1

turtle.exitonclick()