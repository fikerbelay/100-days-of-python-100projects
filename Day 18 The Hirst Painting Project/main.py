import turtle
from random import randint
tim = turtle.Turtle()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tup = (r, g, b)
    return tup

tim.setheading(0)
tim.pensize(40)
turtle.colormode(255)
tim.speed("fastest")

tim.penup()
tim.goto(-300,250)

def paint():
    for _ in range(16):
        tim.color(random_color())
        tim.pendown()
        tim.forward(0)
        tim.penup()
        tim.forward(40)



def turn():
    paint()
    tim.back(40)
    tim.right(90)
    tim.forward(40)
    tim.right(90)
    paint()
    tim.back(40)
    tim.left(90)
    tim.forward(40)
    tim.left(90)


for i in range(7):
    turn()


screen = turtle.Screen()
screen.exitonclick()