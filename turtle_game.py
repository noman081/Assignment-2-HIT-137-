from turtle import Turtle, Screen, turtles
from random import randint

# Setting up the screen
s = Screen()
s.bgcolor("#25be55")
s.setup(800, 600)
s.title("Turtle Racing Game")
s.setworldcoordinates(-250, -250, 250, 250)

game_on = True
colors = ["red", "yellow", "orange", "blue", "white", "purple"] # color of turtles
ypos = [-100, -60, -20, 20, 60, 100]    # for turtles positions
turtles = []                            
ALIGN = "right"
FONT = ("Courier", 14, "bold")

# Creating Field and finish line
f = Turtle()
f.penup()
f.color("White")
f.pensize(6)
f.goto(230,150)
f.pendown()
f.goto(230,-150)
f.goto(240,-150)
f.goto(240,150)
f.goto(-240,150)
f.goto(-240,-150)
f.goto(240,-150)
f.penup()
f.goto(-240,-120)
f.pendown()
f.goto(240,-120)

# for each turtle create individual lane
for i in range(6):
    y=ypos[i]+20
    f.penup()
    f.goto(-240,y)
    f.pendown()
    f.goto(240,y)
f.ht()
# Creating Turtle Objects
for i in range(6):
    t = Turtle("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-230, ypos[i])
    turtles.append(t)

while game_on:
    for i in turtles:
        if i.xcor() > 220:
            game_on = False
            winner = i.pencolor()
            i.write(f'Winner! {winner} is winner', font=FONT, align=ALIGN)

        i.forward(randint(0, 10))

s.exitonclick()