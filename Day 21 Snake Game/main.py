import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

STARTING_X = 0
STARTING_Y = 0
body = []

for i in range(3):
    segment = Turtle('square')
    segment.color('white')
    segment.goto(STARTING_X, STARTING_Y)
    STARTING_X -= 20
    body.append(segment)

def move(body):
    for part in body:
        part.forward(10)



screen.exitonclick()