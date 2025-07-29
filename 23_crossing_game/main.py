from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("Crossing game")

player = Player()
scoreboard = Scoreboard()
manager = CarManager()

screen.onkey(player.move, "Up")
screen.listen()

is_game_on = True

while is_game_on:
    time.sleep(manager.move_speed)
    screen.update()
    manager.move()
    manager.generate_car()

    if player.is_finished():
        player.restart_position()
        scoreboard.increase_score()
        manager.increase_speed()

    if manager.have_collision(player.xcor(), player.ycor()):
        scoreboard.game_over()
        is_game_on = False

screen.exitonclick()