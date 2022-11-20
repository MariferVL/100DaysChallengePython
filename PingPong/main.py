from turtle import Screen
from paddle import Paddle
from scoreboard import Score
from ball import Ball
import time

screen = Screen()
scoreboard = Score()
middle_line = Score()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Ping Pong")

paddle1 = Paddle(-350)
paddle2 = Paddle(350)
ball = Ball()
screen.listen()
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.speed_up)
    scoreboard.start()
    middle_line.create()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("y")

    if ball.distance(paddle1) < 40 or ball.distance(paddle2) < 40:
        ball.bounce("x")
        if ball.distance(paddle1) < 40:
            scoreboard.update_score(1)
        else:
            scoreboard.update_score(2)

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.update_score(1)
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.update_score(2)

screen.exitonclick()

