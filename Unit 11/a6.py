import turtle
import time

my_screen = turtle.Screen()
my_screen.title("Python with AI - Turtle Moving")
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.penup()

for i in range(1,100):
    x = my_turtle.xcor()
    y = my_turtle.ycor()
    my_turtle.goto(x + 5, y + 5)
    time.sleep(0.05)

turtle.exitonclick()