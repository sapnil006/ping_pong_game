import turtle
from turtle import Turtle
direction = [-490, 0, 480]


class Pong(Turtle):

    def __init__(self, x):
        super().__init__()
        turtle.tracer(0)
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.color("black")
        self.resizemode("user")
        self.shapesize(5, 1, 0)
        self.location(x)
        self.showturtle()
        turtle.update()

    def location(self, arg):
        self.goto(direction[arg], 0)

    def moveup(self):
        turtle.tracer(0)
        current_y_cor = self.ycor()
        updated_y_cor = current_y_cor + 100
        self.goto(self.xcor(), updated_y_cor)
        turtle.update()

    def movedown(self):
        turtle.tracer(0)
        current_y_cor = self.ycor()
        updated_y_cor = current_y_cor - 100
        self.goto(self.xcor(), updated_y_cor)
        turtle.update()
