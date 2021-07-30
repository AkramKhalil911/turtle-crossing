import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
class CarManager():
    def __init__(self):
        self.randomcars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def spawncars(self):
        random_chance = random.randint(0,5)
        if random_chance == 5:
            self.randomcar = Turtle("square")
            self.randomcar.speed("fastest")
            self.randomcar.penup()
            self.randomcar.shapesize(1, 2)
            self.randomcar.color(random.choice(COLORS))
            self.randomcar.goto(300, random.randint(-250, 250))
            self.randomcars.append(self.randomcar)

    def movecars(self):
        for car in self.randomcars:
            car.backward(self.carspeed)

    def levelup(self):
        self.carspeed += MOVE_INCREMENT