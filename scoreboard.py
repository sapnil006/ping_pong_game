from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score1 = 0
        self.score2 = 0

    def display(self):
        self.clear()
        self.goto(-250, 276)
        self.write(self.score1, move=True, align="Center", font=("Arial", 15, "normal"))
        self.goto(250, 276)
        self.write(self.score2, move=True, align="Center", font=("Arial", 15, "normal"))
