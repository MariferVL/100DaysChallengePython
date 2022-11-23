from turtle import Turtle, colormode
from random import randint, choice

# TODO create cars in pos x= 300 with weight=2 and length=1, different colors, square shape, penup DONE
# TODO cars with random self.car_y between 170 and -170 (divide screen by 25) DONE
# TODO cars move goto x= -300, y= self.car_y


class Car:
    def __init__(self):
        self.cars = []
        self.x_pos = 300
        self.x_steps = 8

    def random_color(self, car):
        colormode(255)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return car.color(r, g, b)

    def random_pos(self, car):
        random_y = choice(range(-160, 180, 50))
        return car.goto(x=self.x_pos, y=random_y)

    def create(self):
        making_car = randint(0, 6)
        if making_car == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.random_color(car)
            self.random_pos(car)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.x_steps)

    def level_up(self):
        self.x_steps += 8


        """for part_index in range(0, len(self.cars) - 1):
            y = self.cars[part_index].ycor()
            new_x = self.cars[part_index].xcor() - 11
            self.cars[part_index].goto(new_x, y)"""


"""        for i in (0, len(self.cars)-1):
            x_space = self.cars[i].xcor() + 100
            if car.xcor() == x_space:
                return car.goto(x=car.xcor() + 100, y=random_y)
            else:"""