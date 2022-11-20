from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pencolor("white")
        self.penup()
        self.goto(x=0, y=240)
        self.pendown()
        self.user1_score = 0
        self.user2_score = 0

    def start(self):
        self.write(f"{self.user1_score}        {self.user2_score}", move=False, align='center',
                   font=('Courier', 33, 'bold'))

    def create(self):
        self.st()
        self.shape("square")
        self.shapesize(stretch_wid=300, stretch_len=0.8)
        self.color("white")
        self.penup()
        self.speed(0)
        self.setpos(x=0, y=0)

    def update_score(self, user_score):
        if user_score == 1:
            self.user1_score += 1
            self.clear()
        elif user_score == 2:
            self.user2_score += 1
            self.clear()
        else:
            self.game_over()
            return False
        self.write(f"{self.user1_score}        {self.user2_score}", move=False, align='center',
                   font=('Courier', 33, 'bold'))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", move=False, align='center', font=('Arial', 33, 'bold'))
