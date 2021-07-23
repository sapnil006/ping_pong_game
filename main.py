import time
from body import Pong
from line import Line
from ball import Ball
from scoreboard import Scoreboard
from turtle import *


screen = Screen()
screen.title("Pongpong")
screen.bgcolor("pink")
screen.setup(width=1000, height=600, startx=None, starty=None)

scoreboard = Scoreboard()
line1 = Line()
pong1 = Pong(0)
pong2 = Pong(2)
ball = Ball()

is_game_on = True
screen.onkeyrelease(pong2.moveup, "Up")
screen.onkeyrelease(pong2.movedown, "Down")
screen.onkey(pong1.moveup, "w")
screen.onkey(pong1.movedown, "s")
screen.listen()
scoreboard.display()
while is_game_on:

    ball.ball_move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if ball.distance(pong2.xcor(), pong2.ycor()) < 60 and ball.xcor() > 490:
        ball.x_bounce()
    if ball.distance(pong1.xcor(), pong1.ycor()) < 50 and ball.xcor() < -490:
        ball.x_bounce()

    if ball.xcor() > 500:
        ball.reset_pos()
        ball.x_bounce()
        scoreboard.score1 += 1
        scoreboard.display()

    if ball.xcor() < -500:
        ball.reset_pos()
        ball.x_bounce()
        scoreboard.score2 += 1
        scoreboard.display()


screen.exitonclick()
