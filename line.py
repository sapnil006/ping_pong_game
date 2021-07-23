from turtle import Turtle
import turtle
direction = [-290]


class Line(Turtle):
    def __init__(self):
        super().__init__()
        turtle.tracer(0)
        self.hideturtle()
        self.penup()
        self.goto(0, direction[0])
        self.pendown()
        self.pensize(2)
        self.showturtle()
        self.move()
        turtle.update()

    def move(self):
        self.left(90)
        for i in range(14):
            self.forward(25)
            self.penup()
            self.forward(25)
            self.pendown()
