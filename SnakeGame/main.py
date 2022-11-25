import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

user = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(user.up, "Up")
screen.onkey(user.down, "Down")
screen.onkey(user.left, "Left")
screen.onkey(user.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    user.move()
    if user.head.distance(food) < 15:
        user.grow()
        food.new_pos()
        scoreboard.update_score()

    for index in range(4, len(user.snake) - 1):
        if user.head.distance(user.snake[index]) < 20:
            scoreboard.restart()
            user.restart()

    border = [290, -290]
    if user.head.xcor() in border or user.head.ycor() in border:
        scoreboard.restart()
        user.restart()

screen.exitonclick()
