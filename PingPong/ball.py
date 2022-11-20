from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.ySteps = 10
        self.xSteps = 10
        self.speed_up = 0.1

    def move(self):
        new_x = self.xcor() + self.xSteps
        new_y = self.ycor() + self.ySteps
        self.goto(x=new_x, y=new_y)

    def bounce(self, cor):
        if cor == "y":
            self.ySteps *= -1
            self.speed_up *= 0.9
        elif cor == "x":
            self.xSteps *= -1
            self.speed_up *= 0.9

    def reset_pos(self):
        self.clear()
        self.setpos(x=0, y=0)
        self.xSteps *= -1
        self.speed_up = 0.1











