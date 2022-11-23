from turtle import Screen
from user import UserTurtle
from cars import Car
from scoreboard import Level
from time import sleep

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing 🐢")
screen.tracer(0)

levelboard = Level()

user = UserTurtle()
car = Car()
game_on = True
screen.listen()
screen.onkeypress(user.move, "Up")


while game_on:
    sleep(0.1)
    screen.update()
    car.create()
    car.move()
    if user.ycor() > 200:
        levelboard.update_level()
        user.setpos(x=0, y=-250)
        car.level_up()
    for i in range(0, len(car.cars) - 1):
        if user.distance(car.cars[i]) < 22:
            levelboard.game_over()
            game_on = False








screen.exitonclick()



