import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.moveUp, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawncars()
    car_manager.movecars()
    for number in range(0, len(car_manager.randomcars)):
        if car_manager.randomcars[number].distance(player.pos()) < 20:
            game_is_on = False
            scoreboard.gameover()

    if player.finished() == True:
        print('ello level 1')
        car_manager.levelup()
        scoreboard.increaselevel()


screen.exitonclick()