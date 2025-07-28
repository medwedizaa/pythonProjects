from turtle import Screen
from control import Paddle
from scoreboard import ScoreBoard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong game')
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
right_score = ScoreBoard((70, 230))
left_score = ScoreBoard((-70, 230))
screen.update()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    # detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # detect collision with a paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detect miss behavior
    if ball.xcor() > 400:
        left_score.increase_score()
        ball.restart()
    if ball.xcor() < -400:
        right_score.increase_score()
        ball.restart()

    ball.move()

screen.exitonclick()
