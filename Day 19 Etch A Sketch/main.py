from turtle import Turtle,Screen

tim = Turtle()

def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def to_the_right():
    tim.right(10)

def to_the_left():
    tim.left(10)





screen = Screen()

screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(to_the_right, "a")
screen.onkey(to_the_left, "d")


screen.listen()
screen.exitonclick()