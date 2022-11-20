from turtle import Turtle

POSITIONS = [-350, 350]
moving = True


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(x=position, y=0)
        self.y = 0

    def move(self):
        self.speed(9)
        while moving:
            self.goto(self.xcor(), 250)
            self.goto(self.xcor(), -250)

    def up(self):
        if self.ycor() < 150:
            self.y += 33
        else:
            dif = 250 - self.ycor()
            self.y = self.ycor() + dif
        self.goto(x=self.xcor(), y=self.y)

    def down(self):
        if self.ycor() > -150:
            self.y -= 33
        else:
            dif = -250 - self.ycor()
            self.y = self.ycor() + dif
        self.goto(x=self.xcor(), y=self.y)

