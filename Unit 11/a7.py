import turtle
import time
import random

my_screen = turtle.Screen()
my_screen.title("Python with AI - Turtle Moving")
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.penup()

for i in range(1,100):
    turn_degree = random.randint(1,30)
    turn_direction = random.randint(1,2)
    if turn_direction == 1:
        my_turtle.right(turn_degree)
    else:
        turtle.left(turn_degree)
    my_turtle.forward(10)
    time.sleep(0.2)

turtle.exitonclick()