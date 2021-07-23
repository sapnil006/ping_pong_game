from turtle import Turtle
import turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        turtle.tracer(0)
        self.penup()
        self.shape("circle")
        self.color("black")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        turtle.update()

    def ball_move(self):
        xcor = self.xcor() + self.x_move
        ycor = self.ycor() + self.y_move
        self.goto(xcor, ycor)
        turtle.update()

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        turtle.update()
