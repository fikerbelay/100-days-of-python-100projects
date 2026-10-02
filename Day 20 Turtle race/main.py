from random import choice
from turtle import Screen, Turtle

screen = Screen()
screen.tracer(0)
screen.title("Turtle Race")
screen.setup(width=700, height=600)

turtles = []
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

START_X = -300
START_Y = 250

user_bet = screen.textinput("Bet Input", "Which Turtle Do You Think Will Win?")


for i in range(6):
    t = Turtle()
    t.penup()
    t.shape('turtle')
    t.color(colors[i])
    t.goto(START_X, START_Y)
    turtles.append(t)
    START_Y -= 100


screen.update()


GAME = True
while GAME:
    picked_turtle = choice(turtles)
    picked_turtle.forward(2)

    screen.update()

    if picked_turtle.xcor() > 310:
        GAME = False
        if user_bet == picked_turtle.pencolor():
            print("You Win!")
        else:
            print(f"You Lose! {picked_turtle.pencolor()} won the race")

screen.exitonclick()