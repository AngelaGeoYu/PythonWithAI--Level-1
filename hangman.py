import turtle
from functions import *

menu_pen = turtle.Turtle()
menu_pen.speed(0)


def button(length):
    for i in range(4):
        menu_pen.forward(length)
        menu_pen.left(90)

def column(n, length):
    menu_pen.left(270)
    for i in range(3):
        button(length)
        menu_pen.forward(length)
    menu_pen.penup()
    menu_pen.left(90)
    menu_pen.forward(n * length)
    menu_pen.left(180)
    menu_pen.pendown()
def menu():
    column(5, 100)
    menu_pen.penup()
    menu_pen.goto(-250, 150)
    menu_pen.write("HANGMAN", font = ("Courier", 80, "bold"))
    menu_pen.penup()
    menu_pen.goto(-130, 100)
    menu_pen.write("MENU", font = ("Courier", 50, "bold"))
    menu_pen.penup()
    menu_pen.goto(8, -46)
    menu_pen.write("START GAME!", font = ("Courier",10,"normal"))

    menu_pen.penup()
    menu_pen.goto(6, -145)
    menu_pen.write("RULES", font = ("Courier",15,"normal"))


    menu_pen.penup()
    menu_pen.goto(3, -248)
    menu_pen.write("QUIT GAME", font = ("Courier",12,"normal"))
    turtle.onscreenclick(btnclick, 1)
    turtle.listen()

    turtle.done()

def btnclick(x,y):
    if 0 < x < 101 and 0 > y > -101:
        print("Start Game")
        print(x, y)
        turtle.clearscreen()
        start_hangman()
    elif 0 < x < 101 and -101 > y > -201:
        print("Rules")
        print(x, y)
        turtle.clearscreen()
        turtle.pencolor("red")
        turtle.penup()
        turtle.goto(-380,-100)
        turtle.pendown()
        turtle.write("1.Do not repeat letters", font = ("Courier", 22, "bold"))
        turtle.penup()
        turtle.goto(-470,-200)
        turtle.pendown()
        turtle.write("2.Only type 1 letter at a time or else it will be wrong", font = ("Courier", 22, "bold"))
        time.sleep(4)
        turtle.clear()
        turtle.pencolor("black")
        column(5, 100)
        menu()
    elif 0 < x < 101 and -201 > y > -301:
        print("Quit")
        print(x, y)
        turtle.clearscreen()
    else:
        print("Click One Of The Options!")
        print(x, y)
        btnclick(x, y)
menu()