from turtle import Turtle
import random


class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("gold", "purple")
        self.speed(0)
        self.new_pos()

    def new_pos(self):
        x = random.randint(-270, 240)
        y = random.randint(-270, 270)
        self.goto(x, y)

