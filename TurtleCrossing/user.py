from turtle import Turtle


# TODO Turtle cross the screen: setheading(90), turtle shape, penup, move() DONE
class UserTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("gold", "violet")
        self.setheading(90)
        self.setpos(x=0, y=-250)

    def move(self):
        self.forward(11)
