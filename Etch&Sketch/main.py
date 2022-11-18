from turtle import Turtle, Screen

nicky = Turtle()
screen = Screen()


def move_forwards():
    nicky.forward(10)

def move_backwards():
    nicky.backward(10)

def turn_left():
    new_heading = nicky.heading() + 10
    nicky.setheading(new_heading)

def turn_right():
    new_heading = nicky.heading() - 10
    nicky.setheading(new_heading)

def clear():
    nicky.clear()
    nicky.penup()
    nicky.home()
    nicky.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()


