import turtle
my_screen = turtle.Screen()
my_screen.title("Python with AI Level 1")
n = 10

while n <= 100 :
    turtle.circle(n)
    n += 10

turtle.exitonclick()