STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def moveUp(self):
        new_ycor = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_ycor)

    def finished(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False