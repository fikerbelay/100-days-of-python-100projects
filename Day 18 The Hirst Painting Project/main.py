import turtle
from random import randint

tim = turtle.Turtle()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


turtle.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

DOT_SIZE = 30
SPACING = 30
DOTS_PER_ROW = 21
ROWS = 18
START_X = -300
START_Y = 250


def paint_row(start_x, y):
    tim.penup()
    tim.goto(start_x, y)
    for _ in range(DOTS_PER_ROW):
        tim.color(random_color())
        tim.dot(DOT_SIZE)
        tim.forward(SPACING)


for row in range(ROWS):
    y = START_Y - (row * SPACING)
    paint_row(START_X, y)


screen = turtle.Screen()
screen.exitonclick()