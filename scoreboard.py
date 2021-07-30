FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.score()


    def score(self):
        self.reset()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increaselevel(self):
        self.level += 1
        self.score()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)
