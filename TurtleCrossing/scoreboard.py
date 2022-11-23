from turtle import Turtle
# TODO level up or game over


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pencolor("gold")
        self.penup()
        self.goto(x=-260, y=260)
        self.pendown()
        self.level = 0
        self.write(f"Level : {self.level}", move=False, align='right', font=('Courier', 22, 'bold'))

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", move=False, align='right', font=('Courier', 22, 'bold'))

    def game_over(self):
        self.penup()
        self.goto(x=0, y=0)
        self.pendown()
        self.write("Game Over", move=False, align='center', font=('Courier', 44, 'bold'))


