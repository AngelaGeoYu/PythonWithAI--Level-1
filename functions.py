from random import randint
import turtle as tu1
import time

tu2 = tu1.Turtle()

words = ["arm","age","rat","dog","cat",'rest',"kids","pool","swim","cool","guess","sweet","black","learn","study","begin"]
computer = words[randint(0,len(words)-1)]

blank_pos = []

def blank(size):
    i = 0
    str=""
    dash ="_ "
    while i < size:
        str = str+ dash
        i = i+1
    blank_pos = tu1.pos()  
    tu2.penup()
    tu2.goto(0,-200)
    tu2.write(str, font=("Courier", 40, "bold"))
    

def draw_hangman(step):
    if step == 1:
        tu1.goto(160,110)
        tu1.pendown()
        tu1.circle(40)
    if step == 2:
        tu1.penup()
        tu1.goto(200,70)
        tu1.pendown()
        tu1.forward(100)
    if step == 3:
        tu1.penup()
        tu1.goto(200,50)
        tu1.pendown()
        tu1.right(30)
        tu1.forward(70)
        tu1.backward(70)
    if step == 4:
        tu1.goto(200,50)
        tu1.left(60)
        tu1.forward(70)
    if step == 5:
        tu1.penup()
        tu1.goto(200,-30)
        tu1.pendown()
        tu1.forward(70)
        tu1.backward(70)
    if step == 6:
        tu1.right(67)
        tu1.forward(75)
        time.sleep(2)
        tu1.clear()
        tu2.clear()
        tu1.penup()
        tu1.goto(-200,100)
        tu1.pendown()
        tu1.write('SORRY YOU LOST', font = ("Courier", 40, "bold"))
        tu2.penup()
        tu2.goto(-200,-200)
        tu2.pendown()
        tu2.write(f'The word was {computer}', font = ("Courier", 40, "bold"))
        tu1.exitonclick()
    
corrects = []
for i in range(len(computer)):
    corrects.append(False)
       
def isAllCorrect():
    for element in corrects:
        if element == False:
           return False 
    return True

def check(computer, guess):
        guess_correct = False
        for i in range(len(computer)):
            if guess == computer[i]:
                corrects[i] = True
                guess_correct = True
        str = "" 
        for i in range(len(corrects)):
            if corrects[i] == True: 
                str = str + computer[i] + " "
            else: 
                str = str + "_ "
        tu2.clear()
        tu2.write(str, font=("Courier", 40, "bold"))   

        return guess_correct
            
def fill():
    tu1.clear

def start_hangman():
    step = len(computer)
    tu1.penup()
    tu1.goto(-100,-100)
    tu1.pendown()
    tu1.forward(200)
    tu1.backward(100)
    tu1.left(90)
    tu1.forward(300)
    tu1.right(90)
    tu1.forward(200)
    tu1.right(90)
    tu1.forward(50)
    tu1.penup()
    tu1.goto(0,-200)
    blank(step)
    tu1.goto(-100,250)
    tu1.pendown()
    tu1.write("PICK A LETTER", font = ("Courier", 30, "bold"))
    tu1.penup()
    wrong = 0
    while wrong <= 7:
        guess = tu1.textinput('Hangman', 'Please enter a letter: ')
        check_result =  check(computer,guess)
        if isAllCorrect() == True:
            tu1.clear()
            tu2.clear()
            tu1.penup()
            tu1.goto(-200,-200)
            tu1.pendown()
            tu1.write('YOU WON GOOD JOB', font=("Arial", 40, "bold"))
            break
        if check_result == False:
            wrong = wrong + 1
            draw_hangman(wrong)
    tu1.exitonclick()