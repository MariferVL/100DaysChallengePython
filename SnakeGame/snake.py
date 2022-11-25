from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.create()
        self.head = self.snake[0]

    def create(self):
        for pos in POSITION:
            self.add_part(pos)

    def add_part(self, pos):
        part = Turtle("square")
        part.color("white")
        part.penup()
        part.goto(pos)
        self.snake.append(part)

    def grow(self):
        self.add_part(self.snake[-1].position())

    def move(self):
        for part_index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[part_index - 1].xcor()
            new_y = self.snake[part_index - 1].ycor()
            self.snake[part_index].goto(new_x, new_y)
        self.head.forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def restart(self):
        for part in self.snake:
            part.goto(800, 800)
        self.snake.clear()
        self.create()
        self.head = self.snake[0]

