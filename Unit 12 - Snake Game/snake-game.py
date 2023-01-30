import turtle
import time
import random

def go_up():
    if head.direction != "down":
        head.direction= "up"

def go_down():
    if head.direction != "up":
        head.direction= "down"

def go_right():
    if head.direction != "left":
        head.direction= "right"

def go_left():
    if head.direction != "right":
        head.direction= "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def hide_body_parts(body_parts):
    head.color("red")
    for part in body_parts:
        part.color("red")
    time.sleep(2)
    for part in body_parts:
        part.goto(1000, 1000)
    body_parts.clear()
    head.color("green")
    head.goto(0, 0)
    head.direction = "stop"

def update_score(score, high_score):
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
update_score(0,0)

win = turtle.Screen()
win.title("Python with AI - Snake Game")
win.setup(width = 600, height = 600)
win.bgcolor('turquoise')

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.shapesize(0.80, 0.80)


win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")

delay = 0.09
body_parts = []
score = 0
high_score = 0

while True:
    win.update()
    move()

    if head.distance(apple) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        apple.goto(x, y)
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("square")
        new_part.color("lime")
        new_part.penup()
        body_parts.append(new_part)
        score = score + 10
    if score > high_score:
        high_score = score
    update_score(score,high_score)

    if len(body_parts) > 0:
        last_part = body_parts.pop()
        body_parts.insert(0,last_part)
        x = head.xcor()
        y = head.ycor()
        last_part.goto(x, y)
        last_part.showturtle()
    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        hide_body_parts(body_parts)
        score = 0
        update_score(score,high_score)

    for index in range(len(body_parts)-1,1,-1):
        if body_parts[index].distance(head) < 20:
            hide_body_parts(body_parts)
            score = 0
            update_score(score,high_score)
            break
    
    time.sleep(delay)