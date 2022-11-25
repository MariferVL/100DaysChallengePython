from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pencolor("white")
        self.penup()
        self.goto(x=0, y=260)
        self.pendown()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.restart()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}        High Score: {self.high_score}", move=False, align='center',
                   font=('Courier', 22, 'bold'))

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.clear()
        self.score = 0
        self.write(f"Score: {self.score}        High Score: {self.high_score}", move=False, align='center',
                   font=('Courier', 22, 'bold'))





