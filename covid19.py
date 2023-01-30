import turtle
import csv

screen = turtle.Screen()
screen.title("Covid-19 Research")
pen_ontario = turtle.Turtle()
pen_ontario.color("red")
 
rows = []
with open("covid19-download.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
row_i = 0
data_counter = 0
ontario = []
while data_counter < 20:
    if rows[row_i][1] == "Ontario":
       row = rows[row_i]
       ontario.append(float(row[7]))
       data_counter = data_counter + 1 
    row_i = row_i + 1

print(ontario)

startx = -450
starty = -290

turtle.penup()
turtle.goto(-450, -350)
turtle.pendown()
turtle.forward(980)
turtle.penup()
turtle.goto(-450, 330)
turtle.pendown()
turtle.right(1)
turtle.goto(-450, -350)
turtle.penup()

pen_ontario.penup()
pen_ontario.goto(startx, starty)
pen_ontario.pendown()

for i in range(len(ontario)):
    x = (i + 1) * 20
    y = ontario[i] / 50
    print(f"({x}, {y})")
    pen_ontario.goto(x, y)

pen_quebec = turtle.Turtle()
pen_quebec.color("blue")

rows = []
with open("covid19-download.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
row_i = 0
data_counter = 0
quebec = []
while data_counter < 20:

    if rows[row_i][1] == "Quebec":
       row = rows[row_i]
       quebec.append(float(row[7]))
       data_counter = data_counter + 1 
    row_i = row_i + 1

print(quebec)

startx = -400
starty = -350

pen_quebec.penup()
pen_quebec.goto(startx, starty)
pen_quebec.pendown()

for i in range(len(quebec)):
    x = (i + 1) * 20
    y = quebec[i] / 50
    print(f"({x}, {y})")
    pen_quebec.goto(x, y)

turtle.exitonclick()