from turtle import *
import random

lala = Turtle()
lala.shape("turtle")
lala.color("aquamarine", "gold")
lala.pensize(3)
lala.resizemode("auto")
lala.speed(0)
colormode(255)
colors = ["coral", "DeepPink3", "red", "DarkSlateGray", "DarkSeaGreen1", "DeepSkyBlue", "DeepPink", "DarkViolet",
          "DarkOrchid", "DarkMagenta", "cyan3", "chartreuse3", "blue3", "coral"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    lala.pencolor(r, g, b)


# Option 1
for _ in range(50):
    lala.forward(11)
    lala.penup()
    lala.forward(11)
    lala.pendown()

# Option 2
"""
for _ in range(333):
    action = [0, 90, 180, 270 ]
    random_color()
    lala.forward(33)
    lala.setheading(random.choice(action))
    """

# Option 3:
"""
for _ in range(120):
    random_color()
    lala.circle(100, 360)
    lala.right(3)
    """

screen = Screen()
screen.exitonclick()
